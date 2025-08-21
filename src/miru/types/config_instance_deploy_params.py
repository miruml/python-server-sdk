# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConfigInstanceDeployParams"]


class ConfigInstanceDeployParams(TypedDict, total=False):
    dry_run: bool
    """Perform a dry run that simulates the operation without making actual changes"""
