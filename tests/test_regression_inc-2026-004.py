from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_run_returns_empty_string_for_out_of_range_index():
    controller = IndexErrorIncident()

    result = controller.run()

    assert result == ""


def test_fetch_record_at_index_returns_empty_string_for_out_of_range_index():
    controller = IndexErrorIncident()

    result = controller.fetch_record_at_index(["only-one"], 10)

    assert result == ""


def test_fetch_record_at_index_returns_empty_string_for_empty_list():
    controller = IndexErrorIncident()

    result = controller.fetch_record_at_index([], 0)

    assert result == ""


def test_fetch_record_at_index_returns_record_for_valid_index():
    controller = IndexErrorIncident()

    result = controller.fetch_record_at_index(["first", "second"], 1)

    assert result == "second"