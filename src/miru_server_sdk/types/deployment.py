# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .device import Device
from .release import Release
from .._models import BaseModel
from .config_instance import ConfigInstance

__all__ = ["Deployment"]


class Deployment(BaseModel):
    id: str
    """ID of the deployment."""

    activity_status: Literal["validating", "needs_review", "staged", "queued", "deployed", "removing", "archived"]
    """Last known activity state of the deployment.

    - Validating: the deployment's config instances are being validated with user's
      custom validation
    - Needs review: deployment needs to be reviewed before it can be deployed
    - Staged: is ready to be deployed
    - Queued: the deployment's config instances are waiting to be received by the
      device; will be deployed as soon as the device is online
    - Deployed: the deployment's config instances are currently available for
      consumption on the device
    - Removing: the deployment's config instances are being removed from the device
    - Archived: the deployment is available for historical reference but cannot be
      deployed and is not active on the device
    """

    config_instances: Optional[List[ConfigInstance]] = None
    """
    Expand the config instances using 'expand[]=config_instances' in the query
    string.
    """

    created_at: datetime
    """Timestamp of when the device release was created."""

    description: str
    """The description of the deployment."""

    device: Optional[Device] = None
    """Expand the device using 'expand[]=device' in the query string."""

    device_id: str
    """ID of the device."""

    error_status: Literal["none", "failed", "retrying"]
    """Last known error state of the deployment.

    - None: no errors
    - Retrying: an error has been encountered and the agent is retrying to reach the
      target status
    - Failed: a fatal error has been encountered; the deployment is archived and (if
      deployed) removed from the device
    """

    object: Literal["deployment"]

    release: Optional[Release] = None
    """Expand the release using 'expand[]=release' in the query string."""

    release_id: str
    """The version of the release."""

    status: Literal[
        "validating", "needs_review", "staged", "queued", "deployed", "removing", "archived", "failed", "retrying"
    ]
    """
    This status merges the 'activity_status' and 'error_status' fields, with error
    states taking precedence over activity states when errors are present. For
    example, if the activity status is 'deployed' but the error status is 'failed',
    the status is 'failed'. However, if the error status is 'none' and the activity
    status is 'deployed', the status is 'deployed'.
    """

    target_status: Literal["staged", "deployed", "archived"]
    """Desired state of the deployment.

    - Staged: is ready to be deployed
    - Deployed: all config instances part of the deployment are available for
      consumption on the device
    - Archived: the deployment is available for historical reference but cannot be
      deployed and is not active on the device
    """

    updated_at: datetime
    """Timestamp of when the device release was last updated."""
