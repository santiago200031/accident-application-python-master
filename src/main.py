"""Application entry point with graceful client-disconnect handling.

A client disconnect is a normal lifecycle event for an HTTP server.  In
particular, it can occur while the application is reading the request body or
writing the response.  This module deliberately treats that event as a
successful cancellation rather than allowing it to escape as an application
error.
"""

from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict, Optional


ASGIMessage = Dict[str, Any]
ASGIReceive = Callable[[], Awaitable[ASGIMessage]]
ASGISend = Callable[[ASGIMessage], Awaitable[None]]


def _is_client_disconnect(error: BaseException) -> bool:
    """Return whether *error* represents a disconnected client.

    Starlette/FastAPI use ``ClientDisconnect``, while other ASGI servers may
    expose the same condition as a connection-reset or broken-pipe error.
    Checking the exception name keeps this module independent of an optional
    framework dependency.
    """

    if error.__class__.__name__ == "ClientDisconnect":
        return True
    return isinstance(error, (BrokenPipeError, ConnectionResetError))


async def _discard_request_body(receive: ASGIReceive) -> bool:
    """Consume the request body until completion.

    Returns ``False`` when the peer has already disconnected.  A disconnect
    exception is intentionally converted into the same safe result.
    """

    try:
        while True:
            message = await receive()
            message_type = message.get("type")
            if message_type == "http.disconnect":
                return False
            if message_type == "http.request" and not message.get("more_body", False):
                return True
    except Exception as error:
        if _is_client_disconnect(error):
            return False
        raise


async def app(scope: Dict[str, Any], receive: ASGIReceive, send: ASGISend) -> None:
    """Minimal ASGI application with safe disconnect semantics.

    A disconnected client does not require an error response: there is no
    connected peer to receive one.  Consequently, all disconnect paths return
    quietly and never propagate ``ClientDisconnect`` to the server.
    """

    if scope.get("type") != "http":
        return

    connected = await _discard_request_body(receive)
    if not connected:
        return

    try:
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [(b"content-type", b"text/plain; charset=utf-8")],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"0",
                "more_body": False,
            }
        )
    except Exception as error:
        if _is_client_disconnect(error):
            return
        raise


async def main(scope: Dict[str, Any], receive: ASGIReceive, send: ASGISend) -> None:
    """Compatibility entry point for ASGI servers that import ``main``."""

    await app(scope, receive, send)


__all__ = ["app", "main"]