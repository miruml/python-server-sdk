# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import release, deployment, config_type, config_schema, config_instance, deployment_validate_response
from .. import _compat
from .device import Device as Device
from .release import Release as Release
from .deployment import Deployment as Deployment
from .config_type import ConfigType as ConfigType
from .config_schema import ConfigSchema as ConfigSchema
from .paginated_list import PaginatedList as PaginatedList
from .config_instance import ConfigInstance as ConfigInstance
from .config_schema_list import ConfigSchemaList as ConfigSchemaList
from .device_list_params import DeviceListParams as DeviceListParams
from .release_list_params import ReleaseListParams as ReleaseListParams
from .device_create_params import DeviceCreateParams as DeviceCreateParams
from .device_list_response import DeviceListResponse as DeviceListResponse
from .device_update_params import DeviceUpdateParams as DeviceUpdateParams
from .release_list_response import ReleaseListResponse as ReleaseListResponse
from .deployment_list_params import DeploymentListParams as DeploymentListParams
from .device_delete_response import DeviceDeleteResponse as DeviceDeleteResponse
from .release_retrieve_params import ReleaseRetrieveParams as ReleaseRetrieveParams
from .deployment_create_params import DeploymentCreateParams as DeploymentCreateParams
from .deployment_list_response import DeploymentListResponse as DeploymentListResponse
from .deployment_retrieve_params import DeploymentRetrieveParams as DeploymentRetrieveParams
from .deployment_validate_params import DeploymentValidateParams as DeploymentValidateParams
from .config_instance_list_params import ConfigInstanceListParams as ConfigInstanceListParams
from .deployment_validate_response import DeploymentValidateResponse as DeploymentValidateResponse
from .config_instance_list_response import ConfigInstanceListResponse as ConfigInstanceListResponse
from .config_instance_retrieve_params import ConfigInstanceRetrieveParams as ConfigInstanceRetrieveParams
from .device_create_activation_token_params import (
    DeviceCreateActivationTokenParams as DeviceCreateActivationTokenParams,
)
from .device_create_activation_token_response import (
    DeviceCreateActivationTokenResponse as DeviceCreateActivationTokenResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    config_instance.ConfigInstance.update_forward_refs()  # type: ignore
    config_schema.ConfigSchema.update_forward_refs()  # type: ignore
    config_type.ConfigType.update_forward_refs()  # type: ignore
    deployment.Deployment.update_forward_refs()  # type: ignore
    deployment_validate_response.DeploymentValidateResponse.update_forward_refs()  # type: ignore
    release.Release.update_forward_refs()  # type: ignore
else:
    config_instance.ConfigInstance.model_rebuild(_parent_namespace_depth=0)
    config_schema.ConfigSchema.model_rebuild(_parent_namespace_depth=0)
    config_type.ConfigType.model_rebuild(_parent_namespace_depth=0)
    deployment.Deployment.model_rebuild(_parent_namespace_depth=0)
    deployment_validate_response.DeploymentValidateResponse.model_rebuild(_parent_namespace_depth=0)
    release.Release.model_rebuild(_parent_namespace_depth=0)
