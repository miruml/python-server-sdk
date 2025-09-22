# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Device"]


class Device(BaseModel):
    id: str
    """ID of the device."""

    created_at: datetime
    """Timestamp of when the device was created."""

    last_connected_at: Optional[datetime] = None
    """
    Timestamp of when the device was last made an initial connection (this is not
    the same as the last time the device was seen).
    """

    last_disconnected_at: Optional[datetime] = None
    """
    Timestamp of when the device was last disconnected (this is not the same as the
    last time the device was seen).
    """

    name: str
    """Name of the device."""

    object: Literal["device"]

    status: Literal["inactive", "activating", "online", "offline"]
    """The status of the device.

    - Inactive: The miru agent has not yet been installed / authenticated
    - Activating: The miru agent is currently being installed / authenticated
      (should only last for a few seconds)
    - Online: The miru agent has successfully pinged the server within the last 60
      seconds.
    - Offline: The miru agent has not successfully pinged the server within the last
      60 seconds (e.g. network issues, device is powered off, etc.)
    """

    updated_at: datetime
    """Timestamp of when the device was last updated."""
