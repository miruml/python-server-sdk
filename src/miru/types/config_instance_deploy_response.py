# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConfigInstanceDeployResponse", "Remove"]


class Remove(BaseModel):
    code: Literal["device_file_path_conflict", "device_config_schema_conflict"]
    """The reason the config instance was removed

    - device_file_path_conflict: the config instance is currently deployed to the
      same device with the same file path as the new config instance to deploy
    - device_config_schema_conflict: the config instance is currently deployed to
      the same device with the same config schema as the new config instance to
      deploy
    """

    config_instance: "ConfigInstance"

    explanation: str
    """
    A human-readable explanation of why the config instance must be removed for the
    new config instance to be able to be deployed
    """


class ConfigInstanceDeployResponse(BaseModel):
    deploy: "ConfigInstance"

    remove: List[Remove]


from .config_instance import ConfigInstance
