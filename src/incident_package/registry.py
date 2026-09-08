from __future__ import annotations

from incident_package.base import Incident

# Synthetic Scenarios (A1 to A8)
from incident_package.controllers.indexing_controller import IndexErrorIncident
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident
from incident_package.repositories.file_storage_repository import MissingFileIncident
from incident_package.services.command_executor_service import BranchChaosIncident
from incident_package.services.external_api_service import NetworkChaosIncident
from incident_package.services.user_context_service import NoneDereferenceIncident
from incident_package.utils.data_parser import BadCastIncident
from incident_package.utils.math_calculator import DivideByZeroIncident

# Anonymized Real-World Scenarios from systemsengineeringcopilotv3 (R1 to R8)
from incident_package.services.streaming_pipeline_service import StreamingExceptionReraiseIncident
from incident_package.repositories.blob_storage_repository import StorageContainerConflictIncident
from incident_package.controllers.queue_consumer_controller import MalformedQueuePayloadIncident
from incident_package.utils.cloud_config_loader import MissingConfigEnvironmentIncident
from incident_package.services.infra_metadata_service import NullInfraOutputIncident
from incident_package.controllers.alert_deduplicator_controller import DuplicateAlertRemediationIncident
from incident_package.services.api_boundary_service import ServiceErrorBoundaryIncident
from incident_package.utils.telemetry_metric_calculator import MetricRateZeroDivisionIncident

# Anonymized Customer Exception Scenarios (C1 to C6)
from incident_package.customer_exceptions.broken_alert_scoping import BrokenAlertScopingIncident
from incident_package.customer_exceptions.malformed_json_body import MalformedJsonBodyIncident
from incident_package.customer_exceptions.none_dereference_missing_doc import NoneDereferenceMissingDocIncident
from incident_package.customer_exceptions.nosql_injection import NosqlInjectionIncident
from incident_package.customer_exceptions.path_traversal_idor import PathTraversalIdorIncident
from incident_package.customer_exceptions.unauthenticated_api import UnauthenticatedApiIncident

SYNTHETIC_INCIDENTS: list[type[Incident]] = [
    DivideByZeroIncident,
    BadCastIncident,
    MissingFileIncident,
    IndexErrorIncident,
    NetworkChaosIncident,
    NoneDereferenceIncident,
    BranchChaosIncident,
    RemediationWorkflowIncident,
]

REAL_INCIDENTS: list[type[Incident]] = [
    StreamingExceptionReraiseIncident,
    StorageContainerConflictIncident,
    MalformedQueuePayloadIncident,
    MissingConfigEnvironmentIncident,
    NullInfraOutputIncident,
    DuplicateAlertRemediationIncident,
    ServiceErrorBoundaryIncident,
    MetricRateZeroDivisionIncident,
]

CUSTOMER_INCIDENTS: list[type[Incident]] = [
    UnauthenticatedApiIncident,
    MalformedJsonBodyIncident,
    PathTraversalIdorIncident,
    NosqlInjectionIncident,
    NoneDereferenceMissingDocIncident,
    BrokenAlertScopingIncident,
]

INCIDENTS: list[type[Incident]] = SYNTHETIC_INCIDENTS + REAL_INCIDENTS + CUSTOMER_INCIDENTS
