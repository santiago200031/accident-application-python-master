import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


@pytest.fixture
def incident() -> IndexErrorIncident:
    return IndexErrorIncident()


def test_run_returns_empty_string_for_out_of_range_requested_index(
    incident: IndexErrorIncident,
) -> None:
    assert incident.run() == ""


@pytest.mark.parametrize(
    ("records", "target_index", "expected"),
    [
        ([], 0, ""),
        (["first", "last"], 0, "first"),
        (["first", "last"], 1, "last"),
        (["first", "last"], 2, ""),
        (["first", "last"], -1, ""),
        (["first", "last"], -3, ""),
    ],
)
def test_fetch_record_at_index_handles_bounds(
    incident: IndexErrorIncident,
    records: list[str],
    target_index: int,
    expected: str,
) -> None:
    assert incident.fetch_record_at_index(records, target_index) == expected


@pytest.mark.parametrize("invalid_index", [None, "0", 0.0, True, False])
def test_fetch_record_at_index_rejects_non_integer_indices(
    incident: IndexErrorIncident,
    invalid_index: object,
) -> None:
    assert incident.fetch_record_at_index(["record"], invalid_index) == ""


def test_fetch_record_at_index_returns_record_for_valid_index(
    incident: IndexErrorIncident,
) -> None:
    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"