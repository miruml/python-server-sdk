# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DeviceStageParams", "ConfigInstance"]


class DeviceStageParams(TypedDict, total=False):
    config_instances: Required[Iterable[ConfigInstance]]
    """The config instances to stage on the device.

    These config instances will be deployed to the device as soon as it is
    activated.
    """


class ConfigInstance(TypedDict, total=False):
    config_schema_id: Required[str]
    """The id of the config schema which this config instance must adhere to."""

    content: Required[object]
    """The configuration values associated with the config instance."""

    relative_filepath: Required[str]
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`
    """
