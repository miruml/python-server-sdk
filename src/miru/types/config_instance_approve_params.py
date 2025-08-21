# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigInstanceApproveParams"]


class ConfigInstanceApproveParams(TypedDict, total=False):
    message: Required[str]
    """A high level success message displayed to the user"""

    expand: List[Literal["content", "config_schema", "device", "config_type"]]
    """The fields to expand in the config instance"""
