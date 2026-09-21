import pytest
from incident_package.controllers.indexing_controller import IndexErrorIncident

def test_fetch_record_at_index_within_bounds():
    controller = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = 1
    assert controller.fetch_record_at_index(records_list, target_index) == "record2"

def test_fetch_record_at_index_out_of_bounds():
    controller = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = 5
    assert controller.fetch_record_at_index(records_list, target_index) == "Default Value"

def test_fetch_record_at_index_negative_index():
    controller = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = -1
    assert controller.fetch_record_at_index(records_list, target_index) == "Default Value"

def test_run_method_with_out_of_bounds_index():
    controller = IndexErrorIncident()
    assert controller.run() == "Default Value"