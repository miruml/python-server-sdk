# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigInstanceRejectParams", "Error"]


class ConfigInstanceRejectParams(TypedDict, total=False):
    errors: Required[Iterable[Error]]

    message: Required[str]
    """A high level error message displayed to the user"""

    expand: List[Literal["content", "config_schema", "device", "config_type"]]
    """The fields to expand in the config instance"""


class Error(TypedDict, total=False):
    message: Required[str]
    """A detailed message explaining why the parameter is causing the error"""

    parameter_path: Required[List[str]]
