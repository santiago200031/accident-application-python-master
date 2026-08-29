"""Regression tests for incident inc-2026-008: KeyError 'missing_key' in remediation pipeline."""

import pytest

from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


class TestRemediationPipelineNoKeyError:
    """Verify that the remediation pipeline does not raise KeyError for missing keys."""

    def test_execute_remediation_pipeline_returns_default_for_missing_key(self):
        """The pipeline should return 0 (default) instead of raising KeyError when 'missing_key' is absent."""
        incident = RemediationWorkflowIncident()
        result = incident.execute_remediation_pipeline()
        assert result == 0

    def test_run_returns_default_for_missing_key(self):
        """run() delegates to execute_remediation_pipeline and should not raise KeyError."""
        incident = RemediationWorkflowIncident()
        result = incident.run()
        assert result == 0

    def test_aggregate_stats_does_not_contain_missing_key(self):
        """_aggregate_stats returns a dict without 'missing_key', confirming the source of the original bug."""
        stats = RemediationWorkflowIncident._aggregate_stats(
            [{"value": 10}, {"value": 20}, {"value": 30}]
        )
        assert "total" in stats
        assert stats["total"] == 60
        # The original bug: accessing 'missing_key' directly would raise KeyError.
        # The fix uses .get("missing_key", 0) which returns the default.
        assert stats.get("missing_key") is None

    def test_pipeline_config_validation(self):
        """Ensure pipeline config validation works correctly."""
        incident = RemediationWorkflowIncident()
        assert incident.validate_pipeline_config({"enabled": True}) is True
        assert incident.validate_pipeline_config({"enabled": False}) is False
        assert incident.validate_pipeline_config({}) is True  # default enabled

    def test_cluster_health_fetch(self):
        """Ensure cluster health returns expected structure."""
        incident = RemediationWorkflowIncident()
        health = incident.fetch_cluster_health()
        assert health["status"] == "healthy"
        assert health["nodes"] == "3/3"

    def test_filter_valid_metrics_excludes_zero_values(self):
        """Ensure filtering removes rows with zero or negative values."""
        rows = [{"value": 10}, {"value": 0}, {"value": -5}, {"value": 20}]
        filtered = RemediationWorkflowIncident._filter_valid_metrics(rows)
        assert len(filtered) == 2
        assert all(row["value"] > 0 for row in filtered)

    def test_audit_log_format(self):
        """Ensure audit log is formatted correctly."""
        log = RemediationWorkflowIncident._format_audit_log("system", "automated-job")
        assert log["user"] == "system"
        assert log["action"] == "automated-job"
        assert log["status"] == "initiated"

    def test_pipeline_disabled_raises_value_error(self):
        """Ensure disabled pipeline raises ValueError, not KeyError."""
        incident = RemediationWorkflowIncident()
        # Monkey-patch validate to simulate disabled config
        original_validate = incident.validate_pipeline_config
        incident.validate_pipeline_config = lambda config: False
        try:
            with pytest.raises(ValueError, match="Pipeline disabled"):
                incident.execute_remediation_pipeline()
        finally:
            incident.validate_pipeline_config = original_validate

    def test_unhealthy_cluster_raises_runtime_error(self):
        """Ensure unhealthy cluster raises RuntimeError, not KeyError."""
        incident = RemediationWorkflowIncident()
        original_fetch = incident.fetch_cluster_health
        incident.fetch_cluster_health = lambda: {"status": "unhealthy", "nodes": "1/3"}
        try:
            with pytest.raises(RuntimeError, match="Unhealthy cluster"):
                incident.execute_remediation_pipeline()
        finally:
            incident.fetch_cluster_health = original_fetch

    def test_no_keyerror_in_full_pipeline(self):
        """Integration test: full pipeline execution must not raise KeyError."""
        incident = RemediationWorkflowIncident()
        # This would have raised KeyError('missing_key') before the fix.
        result = incident.execute_remediation_pipeline()
        assert isinstance(result, int)
        assert result == 0