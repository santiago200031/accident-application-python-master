from __future__ import annotations

import sys
from pathlib import Path

# Ensure the source root is on the path so imports resolve in any environment.
SRC_ROOT = Path(__file__).resolve().parents[3]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from incident_package.controllers.indexing_controller import IndexErrorIncident


class TestIndexErrorIncidentRegression:
    """Regression tests for inc-2026-004.

    The original bug was an ``IndexError`` raised when accessing a list index
    that is out of range.  The fix adds bounds-checking in
    ``fetch_record_at_index`` so that out-of-range indices return an empty
    string instead of raising.
    """

    def test_run_returns_empty_string_for_out_of_range_index(self) -> None:
        """The incident scenario: requesting index 10 from a single-element list.

        Pre-patch code would raise ``IndexError`` here; the patched code must
        return an empty string.
        """
        controller = IndexErrorIncident()
        result = controller.run()
        assert result == ""

    def test_fetch_record_at_index_valid_index_returns_element(self) -> None:
        """A valid index should still return the correct element."""
        controller = IndexErrorIncident()
        records = ["alpha", "beta", "gamma"]
        assert controller.fetch_record_at_index(records, 0) == "alpha"
        assert controller.fetch_record_at_index(records, 1) == "beta"
        assert controller.fetch_record_at_index(records, 2) == "gamma"

    def test_fetch_record_at_index_negative_index_returns_empty(self) -> None:
        """Negative indices are treated as out-of-range and return ''."""
        controller = IndexErrorIncident()
        records = ["alpha", "beta"]
        assert controller.fetch_record_at_index(records, -1) == ""

    def test_fetch_record_at_index_equal_to_length_returns_empty(self) -> None:
        """Index equal to len(list) is out-of-range and returns ''."""
        controller = IndexErrorIncident()
        records = ["alpha", "beta"]
        assert controller.fetch_record_at_index(records, 2) == ""

    def test_fetch_record_at_index_non_list_returns_empty(self) -> None:
        """Passing a non-list should return '' without raising."""
        controller = IndexErrorIncident()
        assert controller.fetch_record_at_index("not-a-list", 0) == ""
        assert controller.fetch_record_at_index(None, 0) == ""

    def test_fetch_record_at_index_empty_list_returns_empty(self) -> None:
        """An empty list with any index should return ''."""
        controller = IndexErrorIncident()
        assert controller.fetch_record_at_index([], 0) == ""