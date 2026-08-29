import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_run_returns_empty_response_for_out_of_range_requested_index():
    incident = IndexErrorIncident()

    assert incident.run() == ""


@pytest.mark.parametrize(
    ("records", "index"),
    [
        ([], 0),
        (["only-one"], 1),
        (["first", "second"], 2),
        (["first", "second"], -1),
    ],
)
def test_fetch_record_at_index_returns_empty_response_for_invalid_index(
    records: list[str], index: int
):
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(records, index) == ""


def test_fetch_record_at_index_returns_record_for_valid_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"


@pytest.mark.parametrize("invalid_index", [None, "0", 1.5])
def test_fetch_record_at_index_returns_empty_response_for_non_integer_index(
    invalid_index,
):
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["record"], invalid_index) == ""