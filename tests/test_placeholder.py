from __future__ import annotations

import pytest

from incident_package.registry import INCIDENTS


@pytest.mark.parametrize("incident_cls", INCIDENTS)
def test_incident_modes_raise_or_fail_as_expected(incident_cls) -> None:
    incident = incident_cls()

    with pytest.raises(Exception):
        incident.run()
