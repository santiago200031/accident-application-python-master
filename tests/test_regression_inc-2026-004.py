from incident_package.controllers.indexing_controller import IndexErrorIncident


class TestIndexErrorIncidentFix:
    def test_run_returns_empty_string_for_out_of_range_requested_index(self):
        incident = IndexErrorIncident()

        result = incident.run()

        assert result == ""

    def test_fetch_record_at_index_returns_record_for_valid_positive_index(self):
        incident = IndexErrorIncident()
        records = ["first", "second", "third"]

        assert incident.fetch_record_at_index(records, 0) == "first"
        assert incident.fetch_record_at_index(records, 1) == "second"
        assert incident.fetch_record_at_index(records, 2) == "third"

    def test_fetch_record_at_index_returns_record_for_valid_negative_index(self):
        incident = IndexErrorIncident()
        records = ["first", "second", "third"]

        assert incident.fetch_record_at_index(records, -1) == "third"
        assert incident.fetch_record_at_index(records, -2) == "second"
        assert incident.fetch_record_at_index(records, -3) == "first"

    def test_fetch_record_at_index_returns_empty_string_for_out_of_range_positive_index(self):
        incident = IndexErrorIncident()
        records = ["only-one"]

        assert incident.fetch_record_at_index(records, 1) == ""
        assert incident.fetch_record_at_index(records, 10) == ""
        assert incident.fetch_record_at_index(records, 999) == ""

    def test_fetch_record_at_index_returns_empty_string_for_out_of_range_negative_index(self):
        incident = IndexErrorIncident()
        records = ["only-one"]

        assert incident.fetch_record_at_index(records, -2) == ""
        assert incident.fetch_record_at_index(records, -10) == ""
        assert incident.fetch_record_at_index(records, -999) == ""

    def test_fetch_record_at_index_returns_empty_string_for_empty_list(self):
        incident = IndexErrorIncident()

        assert incident.fetch_record_at_index([], 0) == ""
        assert incident.fetch_record_at_index([], -1) == ""