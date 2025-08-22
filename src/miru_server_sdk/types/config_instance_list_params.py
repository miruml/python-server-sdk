# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ConfigInstanceListParams"]


class ConfigInstanceListParams(TypedDict, total=False):
    id: str
    """The config instance ID to filter by"""

    activity_status: Literal["created", "validating", "validated", "queued", "deployed", "removed"]
    """The config instance activity status to filter by"""

    config_schema_id: str
    """The config schema ID to filter by"""

    config_type_id: str
    """The config type ID to filter by"""

    device_id: str
    """The device ID to filter by"""

    error_status: Literal["none", "failed", "retrying"]
    """The config instance error status to filter by"""

    expand: List[Literal["total_count", "content", "config_schema", "device", "config_type"]]
    """The fields to expand in the config instance list"""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]

    target_status: Literal["created", "validated", "deployed", "removed"]
    """The config instance target status to filter by"""
