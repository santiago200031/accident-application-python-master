from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_fetch_record_at_index_returns_controlled_empty_result_for_out_of_range_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["only-one"], 10) == ""


def test_run_handles_stale_requested_index_without_index_error():
    assert IndexErrorIncident().run() == ""


def test_fetch_record_at_index_handles_empty_records_and_invalid_negative_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index([], 0) == ""
    assert incident.fetch_record_at_index(["only-one"], -2) == ""