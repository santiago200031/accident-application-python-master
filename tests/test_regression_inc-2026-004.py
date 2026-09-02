import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


@pytest.fixture
def controller() -> IndexErrorIncident:
    return IndexErrorIncident()


def test_run_returns_empty_string_for_out_of_range_requested_index(
    controller: IndexErrorIncident,
) -> None:
    assert controller.run() == ""


@pytest.mark.parametrize(
    ("records", "target_index"),
    [
        ([], 0),
        (["first", "second"], -1),
        (["first", "second"], 2),
        (["first"], 10),
    ],
)
def test_fetch_record_at_index_returns_empty_string_for_invalid_index(
    controller: IndexErrorIncident,
    records: list[str],
    target_index: int,
) -> None:
    assert controller.fetch_record_at_index(records, target_index) == ""


def test_fetch_record_at_index_returns_record_for_valid_boundary_indices(
    controller: IndexErrorIncident,
) -> None:
    records = ["first", "middle", "last"]

    assert controller.fetch_record_at_index(records, 0) == "first"
    assert controller.fetch_record_at_index(records, len(records) - 1) == "last"