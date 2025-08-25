# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .device import Device
from .._models import BaseModel

__all__ = ["ConfigInstance"]


class ConfigInstance(BaseModel):
    id: str
    """ID of the config instance"""

    activity_status: Literal["created", "validating", "validated", "queued", "deployed", "removed"]
    """Last known activity state of the config instance

    - Created: config instance has been created but no deployment attempt has been
      made
    - Validating: config instance is being validated with user's custom validation
    - Validated: config instance has been validated with user's custom validation
    - Queued: config instance will be deployed as soon as the device is back online
    - Deployed: config instance is currently available on the device
    - Removed: the config instance is no longer available on the device
    """

    config_schema: Optional["ConfigSchema"] = None
    """Expand the config schema using 'expand[]=config_schema' in the query string"""

    config_schema_id: str
    """ID of the config schema which the config instance must adhere to"""

    config_type: Optional["ConfigType"] = None
    """Expand the config type using 'expand[]=config_type' in the query string"""

    config_type_id: str
    """ID of the config type which the config instance (and its schema) is a part of"""

    content: Optional[object] = None
    """The configuration values associated with the config instance.

    Expand the content using 'expand[]=content' in the query string
    """

    created_at: datetime
    """The timestamp of when the config instance was created"""

    device: Optional[Device] = None

    device_id: str
    """ID of the device which the config instance is deployed to"""

    error_status: Literal["none", "failed", "retrying"]
    """Last known error state of the config instance deployment

    - None: there are no errors with the config instance deployment
    - Retrying: an error has been encountered and the agent is attempting to try
      again to reach the target status
    - Failed: an error has been encountered but no more retries are left; the config
      instance is removed (if deployed)
    """

    object: Literal["config_instance"]

    relative_filepath: str
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`
    """

    status: Literal["created", "validating", "validated", "queued", "deployed", "removed", "failed", "retrying"]
    """
    This status merges the 'activity_status' and 'error_status' fields, with error
    states taking precedence over activity states when errors are present. For
    example, if the activity status is 'deployed' but there's an error, the overall
    status will be 'failed' or 'retrying' depending on the error state.
    """

    target_status: Literal["created", "validated", "deployed", "removed"]
    """Desired state of the config instance

    - Created: config instance desires not to be deployed but can be deployed in the
      future
    - Validated: config instance desires user's custom validation before deployment
      can begin
    - Deployed: config instance desires to be available on the device
    - Removed: config instance desires to no longer be available on the device
    """

    updated_at: datetime
    """The timestamp of when the config instance was last updated"""


from .config_type import ConfigType
from .config_schema import ConfigSchema
