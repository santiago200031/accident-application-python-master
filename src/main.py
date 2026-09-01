"""Minimal ASGI application with graceful client-disconnect handling.

A client can close its connection while the application is reading the request or
writing the response.  That condition is not a server failure and must not escape
the request boundary as an unhandled exception.
"""

from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict, Iterable, MutableMapping

try:  # Starlette is optional so this module remains importable in simple tests.
    from starlette.requests import ClientDisconnect  # type: ignore
except ImportError:  # pragma: no cover - used only without Starlette installed
    class ClientDisconnect(Exception):
        """Fallback disconnect exception for environments without Starlette."""


Scope = MutableMapping[str, Any]
Message = Dict[str, Any]
Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]


async def _send_empty_response(send: Send, status: int = 204) -> None:
    """Send a response which does not require a response body."""

    await send(
        {
            "type": "http.response.start",
            "status": status,
            "headers": [(b"content-length", b"0")],
        }
    )
    await send({"type": "http.response.body", "body": b""})


async def request_handler(scope: Scope, receive: Receive, send: Send) -> None:
    """Handle one ASGI request without propagating client cancellation.

    Reading the request body is intentional: a disconnect can be raised by
    ``receive`` before the application has a chance to produce a response.
    Once a disconnect occurs there is no reliable peer to respond to, so the
    correct safe action is to stop processing and return normally.
    """

    if scope.get("type") != "http":
        if scope.get("type") == "lifespan":
            while True:
                message = await receive()
                if message.get("type") == "lifespan.startup":
                    await send({"type": "lifespan.startup.complete"})
                elif message.get("type") == "lifespan.shutdown":
                    await send({"type": "lifespan.shutdown.complete"})
                    return
        return

    try:
        while True:
            message = await receive()
            if message.get("type") == "http.disconnect":
                return
            if message.get("type") == "http.request" and not message.get(
                "more_body", False
            ):
                break

        await _send_empty_response(send)
    except ClientDisconnect:
        # A remote cancellation is expected during normal operation.  Do not
        # re-raise it: doing so turns a harmless disconnect into an application
        # error and can generate noisy 500 responses in server middleware.
        return


# Standard ASGI application name used by ASGI servers and test clients.
app = request_handler
application = app


async def main(scope: Scope, receive: Receive, send: Send) -> None:
    """Compatibility entry point for callers importing ``main`` directly."""

    await request_handler(scope, receive, send)


__all__ = [
    "ClientDisconnect",
    "app",
    "application",
    "main",
    "request_handler",
]