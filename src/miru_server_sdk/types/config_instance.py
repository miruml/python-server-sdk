# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .device import Device
from .._models import BaseModel
from .config_type import ConfigType
from .config_schema import ConfigSchema

__all__ = ["ConfigInstance"]


class ConfigInstance(BaseModel):
    id: str
    """ID of the config instance."""

    activity_status: Literal["created", "queued", "deployed", "removed"]
    """Last known activity state of the config instance.

    - Created: config instance has been created and can be deployed in the future
    - Queued: config instance is waiting to be received by the device; will be
      deployed as soon as the device is online
    - Deployed: config instance is currently available for consumption on the device
    - Removed: the config instance is available for historical reference but cannot
      be deployed and is not active on the device
    """

    config_schema: Optional[ConfigSchema] = None
    """Expand the config schema using 'expand[]=config_schema' in the query string."""

    config_schema_id: str
    """ID of the config schema which the config instance must adhere to."""

    config_type_id: str
    """ID of the config type which the config instance (and its schema) is a part of."""

    content: Optional[object] = None
    """The configuration values associated with the config instance.

    Expand the content using 'expand[]=content' in the query string.
    """

    created_at: datetime
    """The timestamp of when the config instance was created."""

    device: Optional[Device] = None

    device_id: str
    """ID of the device which the config instance is deployed to."""

    error_status: Literal["none", "failed", "retrying"]
    """Last known error state of the config instance deployment.

    - None: there are no errors with the config instance deployment
    - Retrying: an error has been encountered and the agent is attempting to try
      again to reach the target status
    - Failed: a fatal error has been encountered; the config instance is archived
      and (if deployed) removed from the device
    """

    object: Literal["config_instance"]

    relative_filepath: str
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`.
    """

    status: Literal["created", "queued", "deployed", "removed", "failed", "retrying"]
    """
    This status merges the 'activity_status' and 'error_status' fields, with error
    states taking precedence over activity states when errors are present. For
    example, if the activity status is 'deployed' but the error status is 'failed',
    the status is 'failed'. However, if the error status is 'none' and the activity
    status is 'deployed', the status is 'deployed'.
    """

    target_status: Literal["created", "deployed", "removed"]
    """Desired state of the config instance.

    - Created: config instance is created and can be deployed in the future
    - Deployed: config instance is available for consumption on the device
    - Removed: config instance is available for historical reference but cannot be
      deployed and is not active on the device
    """

    updated_at: datetime
    """The timestamp of when the config instance was last updated."""

    config_type: Optional[ConfigType] = None
    """Expand the config type using 'expand[]=config_type' in the query string."""
