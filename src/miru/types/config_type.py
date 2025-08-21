# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConfigType"]


class ConfigType(BaseModel):
    id: str
    """ID of the config type"""

    config_schemas: Optional["ConfigSchemaList"] = None
    """Expand the config schemas using 'expand[]=schemas' in the query string"""

    created_at: datetime
    """Timestamp of when the config type was created"""

    name: str
    """Name of the config type"""

    object: Literal["config_type"]

    slug: str
    """An immutable, code-friendly name for the config type"""

    updated_at: datetime
    """Timestamp of when the config type was last updated"""


from .config_schema_list import ConfigSchemaList
