# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConfigType"]


class ConfigType(BaseModel):
    id: str
    """ID of the config type."""

    created_at: datetime
    """Timestamp of when the config type was created."""

    name: str
    """Name of the config type."""

    object: Literal["config_type"]

    slug: str
    """An immutable, code-friendly name for the config type."""

    updated_at: datetime
    """Timestamp of when the config type was last updated."""
