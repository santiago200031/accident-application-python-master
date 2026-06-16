import subprocess
from unittest.mock import patch
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def test_execute_branch_chaos_calls_create_fix_branch_with_hyphenated_branch_name():
    adapter = BrokenMCPAdapter()
    with patch.object(adapter, 'create_fix_branch') as mock_create_fix_branch:
        mock_create_fix_branch.return_value = "fix/critical-hotfix"
        result = adapter.execute(mode='branch-chaos')
        mock_create_fix_branch.assert_called_once_with("fix/critical-hotfix")
        assert isinstance(result, dict)


def test_execute_branch_chaos_propagates_subprocess_error_from_create_fix_branch():
    adapter = BrokenMCPAdapter()
    with patch.object(adapter, 'create_fix_branch') as mock_create_fix_branch:
        mock_create_fix_branch.side_effect = subprocess.CalledProcessError(1, "git checkout -b fix/critical hotfix")
        try:
            adapter.execute(mode='branch-chaos')
            assert False, "Expected subprocess.CalledProcessError"
        except subprocess.CalledProcessError as e:
            assert e.returncode == 1
            assert "fix/critical hotfix" in str(e)
