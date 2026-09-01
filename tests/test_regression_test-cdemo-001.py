import asyncio

from main import app


class ClientDisconnect(Exception):
    pass


def test_client_disconnect_while_reading_request_is_ignored():
    received = []
    sent = []

    async def receive():
        received.append(True)
        raise ClientDisconnect("test")

    async def send(message):
        sent.append(message)

    asyncio.run(app({"type": "http"}, receive, send))

    assert received == [True]
    assert sent == []


def test_client_disconnect_while_sending_response_is_ignored():
    sent = []

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message):
        sent.append(message)
        raise ClientDisconnect("test")

    asyncio.run(app({"type": "http"}, receive, send))

    assert len(sent) == 1
    assert sent[0]["type"] == "http.response.start"


def test_http_disconnect_message_does_not_send_response():
    sent = []

    async def receive():
        return {"type": "http.disconnect"}

    async def send(message):
        sent.append(message)

    asyncio.run(app({"type": "http"}, receive, send))

    assert sent == []


def test_successful_request_sends_response():
    sent = []

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message):
        sent.append(message)

    asyncio.run(app({"type": "http"}, receive, send))

    assert sent == [
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [(b"content-type", b"text/plain; charset=utf-8")],
        },
        {
            "type": "http.response.body",
            "body": b"0",
            "more_body": False,
        },
    ]


def test_non_http_scope_is_ignored():
    sent = []

    async def receive():
        raise AssertionError("receive must not be called")

    async def send(message):
        sent.append(message)

    asyncio.run(app({"type": "lifespan"}, receive, send))

    assert sent == []