import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


@pytest.mark.parametrize(
    ("records", "target_index"),
    [
        ([], 0),
        (["only-one"], -1),
        (["only-one"], 1),
        (["first", "second"], 5),
    ],
)
def test_fetch_record_at_index_returns_empty_string_for_invalid_indexes(
    records: list[str], target_index: int
) -> None:
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(records, target_index) == ""


def test_fetch_record_at_index_returns_record_for_valid_index() -> None:
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"


def test_run_handles_stale_requested_index_without_raising_index_error() -> None:
    incident = IndexErrorIncident()

    assert incident.run() == ""