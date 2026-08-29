from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_fetch_record_at_index_returns_empty_string_for_stale_out_of_range_index():
    incident = IndexErrorIncident()

    result = incident.fetch_record_at_index(["only-one"], 10)

    assert result == ""


def test_fetch_record_at_index_returns_empty_string_for_empty_records():
    incident = IndexErrorIncident()

    result = incident.fetch_record_at_index([], 0)

    assert result == ""


def test_fetch_record_at_index_returns_empty_string_for_negative_index():
    incident = IndexErrorIncident()

    result = incident.fetch_record_at_index(["only-one"], -1)

    assert result == ""


def test_run_handles_requested_index_that_exceeds_active_records():
    incident = IndexErrorIncident()

    assert incident.run() == ""