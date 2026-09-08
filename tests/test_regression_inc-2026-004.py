from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_fetch_record_at_index_returns_empty_string_for_out_of_range_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["only-one"], 10) == ""


def test_run_handles_stale_requested_index_without_index_error():
    incident = IndexErrorIncident()

    assert incident.run() == ""


def test_fetch_record_at_index_returns_empty_string_for_negative_and_non_integer_indices():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["only-one"], -1) == ""
    assert incident.fetch_record_at_index(["only-one"], -2) == ""
    assert incident.fetch_record_at_index(["only-one"], "0") == ""


def test_fetch_record_at_index_returns_record_for_valid_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"