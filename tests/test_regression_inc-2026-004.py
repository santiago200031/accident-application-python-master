"""Regression tests for inc-2026-004."""

from incident_package.controllers.indexing_controller import IndexErrorIncident


def test_run_returns_empty_string_for_out_of_range_index():
    controller = IndexErrorIncident()

    result = controller.run()

    assert result == ""


def test_fetch_record_at_index_returns_empty_string_when_index_is_out_of_range():
    controller = IndexErrorIncident()

    assert controller.fetch_record_at_index(["only-one"], 10) == ""
    assert controller.fetch_record_at_index([], 0) == ""
    assert controller.fetch_record_at_index(["a", "b"], 2) == ""


def test_fetch_record_at_index_returns_value_for_valid_index():
    controller = IndexErrorIncident()
    records = ["zero", "one"]

    assert controller.fetch_record_at_index(records, 0) == "zero"
    assert controller.fetch_record_at_index(records, 1) == "one"