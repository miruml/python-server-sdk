# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    id: str
    """The deployment ID to filter by."""

    activity_status: Literal["validating", "needs_review", "staged", "queued", "deployed", "removing", "archived"]
    """The deployment activity status to filter by."""

    device_id: str
    """The deployment device ID to filter by."""

    error_status: Literal["none", "failed", "retrying"]
    """The deployment error status to filter by."""

    expand: List[Literal["total_count", "device", "release", "config_instances"]]
    """The fields to expand in the deployments list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]

    release_id: str
    """The deployment release ID to filter by."""

    target_status: Literal["staged", "deployed", "archived"]
    """The deployment target status to filter by."""
