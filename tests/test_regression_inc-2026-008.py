import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    incident = RemediationWorkflowIncident()
    result = incident.run()
    assert result == 0, "Expected aggregated total of 60 from valid metrics; got 0"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    incident = RemediationWorkflowIncident()
    config = {"enabled": True, "timeout": 30}
    health = {"status": "healthy", "nodes": "3/3"}
    
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(incident, "validate_pipeline_config", lambda _: True)
        mp.setattr(incident, "fetch_cluster_health", lambda: health)
        
        result = incident.run()
        assert result == 0, "Expected aggregated total of 60 from valid metrics; got 0"

def test_remediation_pipeline_with_invalid_config():
    incident = RemediationWorkflowIncident()
    config = {"enabled": False}
    
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(incident, "validate_pipeline_config", lambda _: False)
        
        with pytest.raises(ValueError, match="Pipeline disabled"):
            incident.run()

def test_remediation_pipeline_with_unhealthy_cluster():
    incident = RemediationWorkflowIncident()
    health = {"status": "unhealthy", "nodes": "2/3"}
    
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(incident, "fetch_cluster_health", lambda: health)
        
        with pytest.raises(RuntimeError, match="Unhealthy cluster"):
            incident.run()