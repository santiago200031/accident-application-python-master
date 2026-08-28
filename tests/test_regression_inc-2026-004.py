from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_run_out_of_range_returns_empty_string():
    incident = IndexErrorIncident()

    result = incident.run()

    assert result == ""


def test_fetch_record_at_index_valid_indexes_return_records():
    incident = IndexErrorIncident()
    records = ["first", "second"]

    assert incident.fetch_record_at_index(records, 0) == "first"
    assert incident.fetch_record_at_index(records, 1) == "second"


def test_fetch_record_at_index_out_of_range_returns_empty_string():
    incident = IndexErrorIncident()
    records = ["only-one"]

    assert incident.fetch_record_at_index(records, 10) == ""
    assert incident.fetch_record_at_index(records, -2) == ""
    assert incident.fetch_record_at_index([], 0) == ""