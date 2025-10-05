# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentValidateWebhookEvent", "Data", "DataDeployment"]


class DataDeployment(BaseModel):
    id: str
    """ID of the deployment"""

    created_at: datetime
    """Timestamp of when the device release was created"""

    device_id: str
    """ID of the device"""

    object: Literal["deployment"]

    release_id: str
    """The version of the release"""


class Data(BaseModel):
    deployment: DataDeployment


class DeploymentValidateWebhookEvent(BaseModel):
    data: Data
    """The data associated with the event"""

    object: Literal["event"]
    """The object that occurred"""

    timestamp: datetime
    """The timestamp of the event"""

    type: Literal["deployment.validate"]
    """The type of event"""
