import pytest

from incident_package.controllers.indexing_controller import IndexErrorIncident


@pytest.fixture
def incident() -> IndexErrorIncident:
    return IndexErrorIncident()


@pytest.mark.parametrize(
    ("records", "target_index"),
    [
        ([], 0),
        (["only-one"], -1),
        (["only-one"], 1),
        (["first", "second"], 10),
    ],
)
def test_fetch_record_at_invalid_index_returns_empty_string(
    incident: IndexErrorIncident,
    records: list[str],
    target_index: int,
) -> None:
    assert incident.fetch_record_at_index(records, target_index) == ""


def test_fetch_record_at_valid_index_returns_record(
    incident: IndexErrorIncident,
) -> None:
    assert incident.fetch_record_at_index(["first", "second"], 1) == "second"


def test_run_returns_empty_string_when_requested_index_is_out_of_range(
    incident: IndexErrorIncident,
) -> None:
    assert incident.run() == ""