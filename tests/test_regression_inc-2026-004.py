from incident_package.controllers.indexing_controller import IndexErrorIncident

def test_fetch_record_at_index_out_of_range():
    controller = IndexErrorIncident()
    records_list = ["only-one"]
    target_index = 10
    result = controller.fetch_record_at_index(records_list, target_index)
    assert result == 'default_value', "Should return 'default_value' for out of range index"

def test_fetch_record_at_index_within_range():
    controller = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = 1
    result = controller.fetch_record_at_index(records_list, target_index)
    assert result == "record2", "Should return the correct record for a valid index"

def test_fetch_record_at_index_negative():
    controller = IndexErrorIncident()
    records_list = ["record1", "record2", "record3"]
    target_index = -1
    result = controller.fetch_record_at_index(records_list, target_index)
    assert result == 'default_value', "Should return 'default_value' for negative index"

def test_run_method():
    controller = IndexErrorIncident()
    result = controller.run()
    assert result == 'default_value', "Should return 'default_value' when running the controller"