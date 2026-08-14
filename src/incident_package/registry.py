from __future__ import annotations

from incident_package.base import Incident
from incident_package.controllers.indexing_controller import IndexErrorIncident
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident
from incident_package.repositories.file_storage_repository import MissingFileIncident
from incident_package.services.command_executor_service import BranchChaosIncident
from incident_package.services.external_api_service import NetworkChaosIncident
from incident_package.services.user_context_service import NoneDereferenceIncident
from incident_package.utils.data_parser import BadCastIncident
from incident_package.utils.math_calculator import DivideByZeroIncident

INCIDENTS: list[type[Incident]] = [
    DivideByZeroIncident,
    BadCastIncident,
    MissingFileIncident,
    IndexErrorIncident,
    NetworkChaosIncident,
    NoneDereferenceIncident,
    BranchChaosIncident,
    RemediationWorkflowIncident,
]
