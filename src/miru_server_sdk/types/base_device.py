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

    status: Literal["inactive", "staged", "activated", "online", "offline"]
    """The status of the device

    - Inactive: The miru agent has not yet been installed / authenticated
    - Staged: The device has been staged for activation
    - Activated: The miru agent has been installed and authenticated
    """

    updated_at: datetime
    """Timestamp of when the device was last updated"""
