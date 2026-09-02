from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_fetch_record_at_index_returns_empty_string_for_out_of_range_index():
    incident = IndexErrorIncident()

    result = incident.fetch_record_at_index(["only-one"], 10)

    assert result == ""


def test_fetch_record_at_index_returns_empty_string_for_empty_records():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index([], 0) == ""


def test_fetch_record_at_index_returns_empty_string_for_negative_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["only-one"], -1) == ""


def test_fetch_record_at_index_returns_record_for_valid_index():
    incident = IndexErrorIncident()

    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"


def test_run_handles_stale_requested_index_without_index_error():
    assert IndexErrorIncident().run() == ""