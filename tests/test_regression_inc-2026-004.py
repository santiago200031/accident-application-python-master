import pytest
from incident_package.controllers.indexing_controller import IndexErrorIncident

def test_fetch_record_at_index_within_bounds():
    incident = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = 1
    assert incident.fetch_record_at_index(records_list, target_index) == "record2"

def test_fetch_record_at_index_out_of_bounds():
    incident = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = 5
    assert incident.fetch_record_at_index(records_list, target_index) == "Default Record"

def test_fetch_record_at_index_negative_out_of_bounds():
    incident = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = -1
    assert incident.fetch_record_at_index(records_list, target_index) == "Default Record"

def test_run_method_with_active_records():
    incident = IndexErrorIncident()
    assert incident.run() == "Default Record"