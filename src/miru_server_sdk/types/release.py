# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .config_schema import ConfigSchema

__all__ = ["Release"]


class Release(BaseModel):
    id: str
    """ID of the release."""

    config_schemas: Optional[List[ConfigSchema]] = None
    """Expand the config schemas using 'expand[]=config_schemas' in the query string."""

    created_at: datetime
    """Timestamp of when the release was created."""

    object: Literal["release"]

    updated_at: datetime
    """Timestamp of when the release was last updated."""

    version: str
    """The version of the release."""
