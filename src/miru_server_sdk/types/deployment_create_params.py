# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeploymentCreateParams", "NewConfigInstance"]


class DeploymentCreateParams(TypedDict, total=False):
    description: Required[str]
    """The description of the deployment."""

    device_id: Required[str]
    """The ID of the device that the deployment is being created for."""

    new_config_instances: Required[Iterable[NewConfigInstance]]
    """The _new_ config instances to create for this deployment.

    A deployment must have exactly one config instance for each config schema in the
    deployment's release. If less config instances are provided than the number of
    schemas, the deployment will 'transfer' config instances from the deployment it
    is patched from. Archived config instances cannot be transferred.
    """

    release_id: Required[str]
    """The release ID which this deployment adheres to."""

    target_status: Required[Literal["staged", "deployed"]]
    """Desired state of the deployment.

    - Staged: ready for deployment. Deployments can only be staged if their release
      is not the current release for the device.
    - Deployed: deployed to the device. Deployments can only be deployed if their
      release is the device's current release.

    If custom validation is enabled for the release, the deployment must pass
    validation before fulfilling the target status.
    """

    expand: List[Literal["device", "release", "config_instances"]]
    """The fields to expand in the deployment."""

    patch_source_id: str
    """The ID of the deployment that this deployment was patched from."""


class NewConfigInstance(TypedDict, total=False):
    config_schema_id: Required[str]
    """The ID of the config schema which this config instance must adhere to.

    This schema must exist in the deployment's release.
    """

    content: Required[object]
    """The configuration data."""

    relative_filepath: Required[str]
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`.
    """
