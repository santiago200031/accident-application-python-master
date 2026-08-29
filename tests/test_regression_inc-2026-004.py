import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_run_returns_controlled_not_found_result_for_out_of_range_request():
    incident = IndexErrorIncident()

    assert incident.run() == ""


@pytest.mark.parametrize(
    ("records", "index"),
    [
        ([], 0),
        (["first"], 1),
        (["first"], -2),
        (["first", "second"], -3),
    ],
)
def test_fetch_record_at_index_returns_empty_string_for_invalid_indices(
    records, index
):
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(records, index) == ""


def test_fetch_record_at_index_returns_record_for_valid_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"