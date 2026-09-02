import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


@pytest.fixture
def controller() -> IndexErrorIncident:
    return IndexErrorIncident()


def test_run_returns_empty_response_for_out_of_range_requested_index(
    controller: IndexErrorIncident,
) -> None:
    assert controller.run() == ""


@pytest.mark.parametrize(
    ("records", "target_index"),
    [
        ([], 0),
        (["first", "second"], 2),
        (["first", "second"], -1),
    ],
)
def test_invalid_index_returns_empty_response_instead_of_raising(
    controller: IndexErrorIncident,
    records: list[str],
    target_index: int,
) -> None:
    assert controller.fetch_record_at_index(records, target_index) == ""


@pytest.mark.parametrize(
    ("records", "target_index", "expected"),
    [
        (["only-one"], 0, "only-one"),
        (["first", "second"], 1, "second"),
    ],
)
def test_valid_index_returns_requested_record(
    controller: IndexErrorIncident,
    records: list[str],
    target_index: int,
    expected: str,
) -> None:
    assert controller.fetch_record_at_index(records, target_index) == expected