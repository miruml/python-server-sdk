# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    id: str
    """The device ID to filter by"""

    expand: List[Literal["total_count"]]
    """The fields to expand in the device list"""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    name: str
    """The device name to filter by"""

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]
