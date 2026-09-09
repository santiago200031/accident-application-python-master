import pytest

from incident_package.customer_exceptions.path_traversal_idor import FileStore


def test_get_content_denies_cross_tenant_request_without_disclosing_blob() -> None:
    store = FileStore()

    with pytest.raises(KeyError, match="Document not found"):
        store.get_content(
            "thread_cece7b9f",
            "output/requirements_extracted.json",
        )

    assert store.last_lookup is None


@pytest.mark.parametrize(
    "relative_path",
    [
        "../thread_cece7b9f/output/requirements_extracted.json",
        "output/../requirements_extracted.json",
        "/output/requirements_extracted.json",
        r"..\thread_cece7b9f\output\requirements_extracted.json",
        "output/%2e%2e/requirements_extracted.json",
        "output//requirements_extracted.json",
    ],
)
def test_get_content_rejects_traversal_like_paths_before_lookup(
    relative_path: str,
) -> None:
    store = FileStore()

    with pytest.raises(KeyError, match="Document not found"):
        store.get_content("thread_a1f1c1c8", relative_path)

    assert store.last_lookup is None


def test_get_content_allows_authorized_safe_relative_path() -> None:
    store = FileStore()

    content = store.get_content(
        "thread_a1f1c1c8",
        "output/requirements_extracted.json",
    )

    assert content == {"secret": "thread-A-output"}
    assert (
        store.last_lookup
        == "files/thread_a1f1c1c8/output/requirements_extracted.json"
    )