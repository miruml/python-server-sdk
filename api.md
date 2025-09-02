# ConfigInstances

Types:

```python
from miru_server_sdk.types import (
    ConfigInstance,
    ConfigSchema,
    ConfigSchemaList,
    ConfigType,
    PaginatedList,
    ConfigInstanceListResponse,
    ConfigInstanceDeployResponse,
)
```

Methods:

- <code title="get /config_instances/{config_instance_id}">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">retrieve</a>(config_instance_id, \*\*<a href="src/miru_server_sdk/types/config_instance_retrieve_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance.py">ConfigInstance</a></code>
- <code title="get /config_instances">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">list</a>(\*\*<a href="src/miru_server_sdk/types/config_instance_list_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance_list_response.py">ConfigInstanceListResponse</a></code>
- <code title="post /config_instances/{config_instance_id}/approve">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">approve</a>(config_instance_id, \*\*<a href="src/miru_server_sdk/types/config_instance_approve_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance.py">ConfigInstance</a></code>
- <code title="post /config_instances/{config_instance_id}/deploy">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">deploy</a>(config_instance_id, \*\*<a href="src/miru_server_sdk/types/config_instance_deploy_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance_deploy_response.py">ConfigInstanceDeployResponse</a></code>
- <code title="post /config_instances/{config_instance_id}/reject">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">reject</a>(config_instance_id, \*\*<a href="src/miru_server_sdk/types/config_instance_reject_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance.py">ConfigInstance</a></code>

# Devices

Types:

```python
from miru_server_sdk.types import (
    Device,
    DeviceListResponse,
    DeviceDeleteResponse,
    DeviceCreateActivationTokenResponse,
)
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">create</a>(\*\*<a href="src/miru_server_sdk/types/device_create_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/device.py">Device</a></code>
- <code title="get /devices/{device_id}">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">retrieve</a>(device_id) -> <a href="./src/miru_server_sdk/types/device.py">Device</a></code>
- <code title="patch /devices/{device_id}">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">update</a>(device_id, \*\*<a href="src/miru_server_sdk/types/device_update_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/device.py">Device</a></code>
- <code title="get /devices">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">list</a>(\*\*<a href="src/miru_server_sdk/types/device_list_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/device_list_response.py">DeviceListResponse</a></code>
- <code title="delete /devices/{device_id}">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">delete</a>(device_id) -> <a href="./src/miru_server_sdk/types/device_delete_response.py">DeviceDeleteResponse</a></code>
- <code title="post /devices/{device_id}/activation_token">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">create_activation_token</a>(device_id, \*\*<a href="src/miru_server_sdk/types/device_create_activation_token_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/device_create_activation_token_response.py">DeviceCreateActivationTokenResponse</a></code>
- <code title="post /devices/{device_id}/stage">client.devices.<a href="./src/miru_server_sdk/resources/devices.py">stage</a>(device_id, \*\*<a href="src/miru_server_sdk/types/device_stage_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/device.py">Device</a></code>

# Webhooks

Types:

```python
from miru_server_sdk.types import (
    ConfigInstanceTargetStatusValidatedWebhookEvent,
    UnwrapWebhookEvent,
)
```
