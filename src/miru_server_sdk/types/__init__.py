# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import config_type, config_schema, config_instance, config_instance_deploy_response
from .. import _compat
from .device import Device as Device
from .config_type import ConfigType as ConfigType
from .config_schema import ConfigSchema as ConfigSchema
from .paginated_list import PaginatedList as PaginatedList
from .config_instance import ConfigInstance as ConfigInstance
from .config_schema_list import ConfigSchemaList as ConfigSchemaList
from .device_list_params import DeviceListParams as DeviceListParams
from .device_stage_params import DeviceStageParams as DeviceStageParams
from .device_create_params import DeviceCreateParams as DeviceCreateParams
from .device_list_response import DeviceListResponse as DeviceListResponse
from .device_update_params import DeviceUpdateParams as DeviceUpdateParams
from .unwrap_webhook_event import UnwrapWebhookEvent as UnwrapWebhookEvent
from .device_delete_response import DeviceDeleteResponse as DeviceDeleteResponse
from .config_instance_list_params import ConfigInstanceListParams as ConfigInstanceListParams
from .config_instance_deploy_params import ConfigInstanceDeployParams as ConfigInstanceDeployParams
from .config_instance_list_response import ConfigInstanceListResponse as ConfigInstanceListResponse
from .config_instance_reject_params import ConfigInstanceRejectParams as ConfigInstanceRejectParams
from .config_instance_approve_params import ConfigInstanceApproveParams as ConfigInstanceApproveParams
from .config_instance_deploy_response import ConfigInstanceDeployResponse as ConfigInstanceDeployResponse
from .config_instance_retrieve_params import ConfigInstanceRetrieveParams as ConfigInstanceRetrieveParams
from .device_create_activation_token_params import (
    DeviceCreateActivationTokenParams as DeviceCreateActivationTokenParams,
)
from .device_create_activation_token_response import (
    DeviceCreateActivationTokenResponse as DeviceCreateActivationTokenResponse,
)
from .config_instance_target_status_validated_webhook_event import (
    ConfigInstanceTargetStatusValidatedWebhookEvent as ConfigInstanceTargetStatusValidatedWebhookEvent,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    config_instance.ConfigInstance.model_rebuild(_parent_namespace_depth=0)
    config_schema.ConfigSchema.model_rebuild(_parent_namespace_depth=0)
    config_type.ConfigType.model_rebuild(_parent_namespace_depth=0)
    config_instance_deploy_response.ConfigInstanceDeployResponse.model_rebuild(_parent_namespace_depth=0)
else:
    config_instance.ConfigInstance.update_forward_refs()  # type: ignore
    config_schema.ConfigSchema.update_forward_refs()  # type: ignore
    config_type.ConfigType.update_forward_refs()  # type: ignore
    config_instance_deploy_response.ConfigInstanceDeployResponse.update_forward_refs()  # type: ignore
