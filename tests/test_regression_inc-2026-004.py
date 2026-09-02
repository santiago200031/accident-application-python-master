from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_fetch_record_at_index_returns_empty_string_for_out_of_range_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["only-one"], 10) == ""


def test_fetch_record_at_index_returns_empty_string_for_empty_records():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index([], 0) == ""


def test_fetch_record_at_index_preserves_valid_positive_and_negative_indexes():
    incident = IndexErrorIncident()
    records = ["first", "second"]

    assert incident.fetch_record_at_index(records, 1) == "second"
    assert incident.fetch_record_at_index(records, -1) == "second"


def test_run_handles_requested_index_beyond_available_records():
    assert IndexErrorIncident().run() == ""