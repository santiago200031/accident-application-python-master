import pytest
from unittest.mock import patch, MagicMock
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter, IncidentSummary, RepairPlan


def test_run_end_to_end_remediation_success():
    with patch.object(BrokenMCPAdapter, 'load_incidents_from_jsonl') as mock_load, \
         patch.object(BrokenMCPAdapter, 'summarize_incidents') as mock_summarize, \
         patch.object(BrokenMCPAdapter, 'calculate_composite_risk') as mock_risk, \
         patch.object(BrokenMCPAdapter, 'select_remediation_action') as mock_select, \
         patch.object(BrokenMCPAdapter, 'enforce_policy_gate') as mock_gate, \
         patch.object(BrokenMCPAdapter, 'draft_config_patch') as mock_patch, \
         patch.object(BrokenMCPAdapter, 'create_fix_branch') as mock_branch:

        mock_load.return_value = [{'id': '1'}]
        mock_summarize.return_value = MagicMock(spec=IncidentSummary)
        mock_risk.return_value = 0.75
        mock_select.return_value = 'restart_service'
        mock_gate.return_value = 'gate_passed'
        mock_patch.return_value = 'success_patch_content'
        mock_branch.return_value = 'fix_branch_123'

        adapter = BrokenMCPAdapter()
        result = adapter.run_end_to_end_remediation(
            incidents_path='fake_incidents.jsonl',
            target_config='fake_config.yaml',
            human_approval=True,
            branch_name='test_branch'
        )

        assert result['summary'] == mock_summarize.return_value
        assert result['risk'] == 0.75
        assert result['action'] == 'restart_service'
        assert result['gate'] == 'gate_passed'
        assert result['patch'] == 'success_patch_content'
        assert result['branch'] == 'fix_branch_123'

        mock_load.assert_called_once_with('fake_incidents.jsonl')
        mock_summarize.assert_called_once_with([{'id': '1'}])
        mock_risk.assert_called_once_with(mock_summarize.return_value, sla_score=0.85)
        mock_select.assert_called_once_with(0.75)
        mock_gate.assert_called_once_with(action='restart_service', human_approval=True)
        mock_patch.assert_called_once_with('fake_config.yaml', key='MAX_RETRIES', value='5')
        mock_branch.assert_called_once_with(branch_name='test_branch')


def test_run_end_to_end_remediation_permission_error():
    with patch.object(BrokenMCPAdapter, 'load_incidents_from_jsonl') as mock_load, \
         patch.object(BrokenMCPAdapter, 'summarize_incidents') as mock_summarize, \
         patch.object(BrokenMCPAdapter, 'calculate_composite_risk') as mock_risk, \
         patch.object(BrokenMCPAdapter, 'select_remediation_action') as mock_select, \
         patch.object(BrokenMCPAdapter, 'enforce_policy_gate') as mock_gate, \
         patch.object(BrokenMCPAdapter, 'draft_config_patch') as mock_patch, \
         patch.object(BrokenMCPAdapter, 'create_fix_branch') as mock_branch:

        mock_load.return_value = [{'id': '1'}]
        mock_summarize.return_value = MagicMock(spec=IncidentSummary)
        mock_risk.return_value = 0.75
        mock_select.return_value = 'restart_service'
        mock_gate.return_value = 'gate_passed'
        mock_patch.side_effect = PermissionError('Unable to write to file')
        mock_branch.return_value = 'fix_branch_123'

        adapter = BrokenMCPAdapter()
        result = adapter.run_end_to_end_remediation(
            incidents_path='fake_incidents.jsonl',
            target_config='fake_config.yaml',
            human_approval=True,
            branch_name='test_branch'
        )

        assert result['summary'] == mock_summarize.return_value
        assert result['risk'] == 0.75
        assert result['action'] == 'restart_service'
        assert result['gate'] == 'gate_passed'
        assert isinstance(result['patch'], str)
        assert result['patch'].startswith('PermissionError:')
        assert 'Unable to write to file' in result['patch']
        assert result['branch'] == 'fix_branch_123'

        mock_patch.assert_called_once_with('fake_config.yaml', key='MAX_RETRIES', value='5')
