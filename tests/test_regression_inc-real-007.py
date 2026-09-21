import pytest

from incident_package.services.api_boundary_service import process_inbound_route


@pytest.mark.parametrize(
    "relative_path",
    [
        "../../other-tenant/file",
        "..\\..\\other-tenant\\file",
        "%2e%2e%2fother-tenant%2ffile",
        "%252e%252e%252fother-tenant%252ffile",
        "/other-tenant/file",
        "C:\\other-tenant\\file",
    ],
)
def test_authorized_route_rejects_paths_that_escape_thread_sandbox(relative_path):
    response = process_inbound_route(
        {
            "authorized": True,
            "thread_id": "tenant-a-thread",
            "relative_path": relative_path,
        }
    )

    assert response == {
        "status": 400,
        "error": "Invalid relative path",
    }


def test_authorized_route_accepts_safe_blob_relative_path():
    payload = {
        "authorized": True,
        "thread_id": "tenant-a-thread",
        "relative_path": "attachments/report.pdf",
    }

    response = process_inbound_route(payload)

    assert response == {"status": 200, "data": payload}