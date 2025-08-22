# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConfigSchema"]


class ConfigSchema(BaseModel):
    id: str
    """ID of the config schema"""

    config_type: Optional["ConfigType"] = None
    """Expand the config type using 'expand[]=config_type' in the query string"""

    config_type_id: str
    """ID of the config type"""

    content: Optional[object] = None
    """The config schema's JSON Schema definition"""

    created_at: datetime
    """Timestamp of when the config schema was created"""

    digest: str
    """Hash of the config schema contents"""

    object: Literal["config_schema"]

    relative_filepath: str
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`
    """

    updated_at: datetime
    """Timestamp of when the config schema was last updated"""

    version: int
    """Config schema version for the config type"""


from .config_type import ConfigType
