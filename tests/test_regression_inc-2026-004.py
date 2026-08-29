from incident_package.controllers.indexing_controller import IndexErrorIncident

def test_fetch_record_at_index_within_bounds():
    controller = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = 1
    assert controller.fetch_record_at_index(records_list, target_index) == "record2"

def test_fetch_record_at_index_out_of_bounds():
    controller = IndexErrorIncident()
    records_list = ["only-one"]
    requested_index = 10
    assert controller.fetch_record_at_index(records_list, requested_index) == 'N/A'

def test_run_method_with_active_records():
    controller = IndexErrorIncident()
    assert controller.run() == 'N/A'