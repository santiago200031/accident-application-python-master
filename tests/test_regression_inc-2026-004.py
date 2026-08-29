from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_fetch_record_at_index_returns_empty_string_for_stale_out_of_range_index():
    incident = IndexErrorIncident()
    active_records = ["only-one"]

    result = incident.fetch_record_at_index(active_records, 10)

    assert result == ""


def test_run_returns_empty_string_when_requested_index_exceeds_active_records():
    incident = IndexErrorIncident()

    assert incident.run() == ""


def test_fetch_record_at_index_rejects_negative_and_boolean_indices():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["only-one"], -1) == ""
    assert incident.fetch_record_at_index(["only-one"], True) == ""


def test_fetch_record_at_index_returns_record_for_valid_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"