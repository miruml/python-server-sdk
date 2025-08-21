# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["DeviceCreateActivationTokenResponse"]


class DeviceCreateActivationTokenResponse(BaseModel):
    token: str
    """The token"""

    expires_at: datetime
    """The expiration date and time of the token"""
