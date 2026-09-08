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
    ("records", "target_index"),
    [
        ([], 0),
        (["only-one"], 1),
        (["first", "second"], 2),
        (["first", "second"], -1),
    ],
)
def test_invalid_indexes_return_empty_string(
    incident: IndexErrorIncident,
    records: list[str],
    target_index: int,
) -> None:
    assert incident.fetch_record_at_index(records, target_index) == ""


def test_valid_index_returns_requested_record(incident: IndexErrorIncident) -> None:
    records = ["first", "second", "third"]

    assert incident.fetch_record_at_index(records, 0) == "first"
    assert incident.fetch_record_at_index(records, 2) == "third"


@pytest.mark.parametrize("target_index", [None, "1", 1.0])
def test_non_integer_indexes_return_empty_string(
    incident: IndexErrorIncident,
    target_index: object,
) -> None:
    assert incident.fetch_record_at_index(["record"], target_index) == ""