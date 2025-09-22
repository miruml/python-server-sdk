# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeviceUpdateParams"]


class DeviceUpdateParams(TypedDict, total=False):
    name: str
    """The new name of the device.

    If excluded from the request, the device name is not updated.
    """
