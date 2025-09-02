# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeviceCreateActivationTokenParams"]


class DeviceCreateActivationTokenParams(TypedDict, total=False):
    allow_reactivation: bool
    """Whether this token can reactivate already activated devices.

    If false, the token is unable to activate devices which are already activated.
    """
