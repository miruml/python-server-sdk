# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BaseDevice"]


class BaseDevice(BaseModel):
    id: str
    """ID of the device"""

    created_at: datetime
    """Timestamp of when the device was created"""

    name: str
    """Name of the device"""

    object: Literal["device"]

    status: Literal["inactive", "activated", "provisioned"]
    """The status of the device

    - Inactive: The miru agent has not yet been installed / authenticated
    - Activated: The miru agent has been installed and authenticated
    - Provisioned: The device has been optionally initialized with config instances
    """

    updated_at: datetime
    """Timestamp of when the device was last updated"""
