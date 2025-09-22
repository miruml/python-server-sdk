# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DeploymentRetrieveParams"]


class DeploymentRetrieveParams(TypedDict, total=False):
    expand: List[Literal["device", "release", "config_instances"]]
    """The fields to expand in the deployment."""
