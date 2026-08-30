import pytest
from incident_package.controllers.indexing_controller import IndexErrorIncident

def test_fetch_record_at_index_within_bounds():
    controller = IndexErrorIncident()
    records = ["record1", "record2", "record3"]
    index = 1
    assert controller.fetch_record_at_index(records, index) == "record2"

def test_fetch_record_at_index_out_of_bounds():
    controller = IndexErrorIncident()
    records = ["record1", "record2", "record3"]
    index = 5
    assert controller.fetch_record_at_index(records, index) == '0'

def test_fetch_record_at_index_negative():
    controller = IndexErrorIncident()
    records = ["record1", "record2", "record3"]
    index = -1
    assert controller.fetch_record_at_index(records, index) == '0'

def test_run_method():
    controller = IndexErrorIncident()
    assert controller.run() == '0'