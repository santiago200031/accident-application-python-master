"""Regression tests for inc-2026-004: IndexError in indexing controller."""

import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


class TestIndexErrorIncident:
    """Tests that verify the fixed behavior of IndexErrorIncident."""

    def test_fetch_record_at_index_valid_index(self):
        """Test that a valid index returns the correct record."""
        controller = IndexErrorIncident()
        records = ["first", "second", "third"]
        assert controller.fetch_record_at_index(records, 0) == "first"
        assert controller.fetch_record_at_index(records, 1) == "second"
        assert controller.fetch_record_at_index(records, 2) == "third"

    def test_fetch_record_at_index_out_of_range_returns_empty_string(self):
        """Test that an out-of-range index returns empty string instead of raising IndexError."""
        controller = IndexErrorIncident()
        records = ["only-one"]
        # This would have raised IndexError before the fix
        assert controller.fetch_record_at_index(records, 10) == ""

    def test_fetch_record_at_index_negative_index_returns_empty_string(self):
        """Test that a negative index returns empty string instead of raising IndexError."""
        controller = IndexErrorIncident()
        records = ["only-one"]
        # Negative indices would have raised or behaved unexpectedly before the fix
        assert controller.fetch_record_at_index(records, -1) == ""

    def test_fetch_record_at_index_empty_list_returns_empty_string(self):
        """Test that accessing an empty list returns empty string."""
        controller = IndexErrorIncident()
        records: list[str] = []
        assert controller.fetch_record_at_index(records, 0) == ""

    def test_run_does_not_raise_index_error(self):
        """Regression test: run() should not raise IndexError for out-of-bounds access.
        
        Before the fix, this would have raised:
            IndexError: list index out of range
        """
        controller = IndexErrorIncident()
        # This call previously triggered IndexError because requested_index=10 
        # was used to access a list with only 1 element
        result = controller.run()
        assert result == ""

    def test_run_returns_empty_string_for_out_of_bounds(self):
        """Explicitly verify the fixed behavior of run()."""
        controller = IndexErrorIncident()
        active_records = ["only-one"]
        requested_index = 10
        # Pre-patch: this raised IndexError
        # Post-patch: returns empty string
        assert controller.fetch_record_at_index(active_records, requested_index) == ""

    def test_boundary_index_equal_to_length_returns_empty_string(self):
        """Test that index equal to list length (one past last valid) returns empty string."""
        controller = IndexErrorIncident()
        records = ["a", "b"]
        # Index 2 is out of range for a 2-element list
        assert controller.fetch_record_at_index(records, 2) == ""

    def test_boundary_last_valid_index(self):
        """Test that the last valid index still works correctly."""
        controller = IndexErrorIncident()
        records = ["a", "b"]
        assert controller.fetch_record_at_index(records, 1) == "b"