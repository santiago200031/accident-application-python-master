import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


@pytest.fixture
def incident():
    return IndexErrorIncident()


@pytest.mark.parametrize(
    ("records", "target_index"),
    [
        ([], 0),
        (["first"], -1),
        (["first"], 1),
        (["first", "second"], 2),
    ],
)
def test_fetch_record_at_index_returns_empty_string_for_invalid_indexes(
    incident, records, target_index
):
    assert incident.fetch_record_at_index(records, target_index) == ""


def test_fetch_record_at_index_returns_records_at_valid_boundary_indexes(incident):
    records = ["first", "last"]

    assert incident.fetch_record_at_index(records, 0) == "first"
    assert incident.fetch_record_at_index(records, 1) == "last"


def test_run_handles_requested_index_beyond_available_records(incident):
    assert incident.run() == ""