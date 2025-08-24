# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DeviceStageParams", "ConfigInstance"]


class DeviceStageParams(TypedDict, total=False):
    config_instances: Required[Iterable[ConfigInstance]]


class ConfigInstance(TypedDict, total=False):
    config_schema_id: Required[str]

    content: Required[object]

    relative_filepath: Required[str]
