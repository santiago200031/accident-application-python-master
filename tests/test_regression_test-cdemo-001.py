import asyncio

from main import ClientDisconnect, request_handler


def test_client_disconnect_during_request_read_is_handled_without_response():
    sent_messages = []

    async def receive():
        raise ClientDisconnect("test")

    async def send(message):
        sent_messages.append(message)

    asyncio.run(
        request_handler(
            {"type": "http", "method": "GET", "path": "/"},
            receive,
            send,
        )
    )

    assert sent_messages == []


def test_client_disconnect_while_writing_response_is_handled():
    received = False

    async def receive():
        nonlocal received
        if not received:
            received = True
            return {"type": "http.request", "body": b"", "more_body": False}
        raise AssertionError("receive should not be called again")

    async def send(message):
        raise ClientDisconnect("test")

    asyncio.run(
        request_handler(
            {"type": "http", "method": "GET", "path": "/"},
            receive,
            send,
        )
    )