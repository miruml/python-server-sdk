# ConfigInstances

Types:

```python
from miru_server_sdk.types import (
    ConfigInstance,
    ConfigSchema,
    ConfigType,
    PaginatedList,
    ConfigInstanceListResponse,
)
```

Methods:

- <code title="get /config_instances/{config_instance_id}">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">retrieve</a>(config_instance_id, \*\*<a href="src/miru_server_sdk/types/config_instance_retrieve_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance.py">ConfigInstance</a></code>
- <code title="get /config_instances">client.config_instances.<a href="./src/miru_server_sdk/resources/config_instances.py">list</a>(\*\*<a href="src/miru_server_sdk/types/config_instance_list_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/config_instance_list_response.py">ConfigInstanceListResponse</a></code>

# Deployments

Types:

```python
from miru_server_sdk.types import Deployment, DeploymentListResponse, DeploymentValidateResponse
```

Methods:

- <code title="post /deployments">client.deployments.<a href="./src/miru_server_sdk/resources/deployments.py">create</a>(\*\*<a href="src/miru_server_sdk/types/deployment_create_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/deployment.py">Deployment</a></code>
- <code title="get /deployments/{deployment_id}">client.deployments.<a href="./src/miru_server_sdk/resources/deployments.py">retrieve</a>(deployment_id, \*\*<a href="src/miru_server_sdk/types/deployment_retrieve_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/deployment.py">Deployment</a></code>
- <code title="get /deployments">client.deployments.<a href="./src/miru_server_sdk/resources/deployments.py">list</a>(\*\*<a href="src/miru_server_sdk/types/deployment_list_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="post /deployments/{deployment_id}/validate">client.deployments.<a href="./src/miru_server_sdk/resources/deployments.py">validate</a>(deployment_id, \*\*<a href="src/miru_server_sdk/types/deployment_validate_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/deployment_validate_response.py">DeploymentValidateResponse</a></code>

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

# Releases

Types:

```python
from miru_server_sdk.types import Release, ReleaseListResponse
```

Methods:

- <code title="get /releases/{release_id}">client.releases.<a href="./src/miru_server_sdk/resources/releases.py">retrieve</a>(release_id, \*\*<a href="src/miru_server_sdk/types/release_retrieve_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/release.py">Release</a></code>
- <code title="get /releases">client.releases.<a href="./src/miru_server_sdk/resources/releases.py">list</a>(\*\*<a href="src/miru_server_sdk/types/release_list_params.py">params</a>) -> <a href="./src/miru_server_sdk/types/release_list_response.py">ReleaseListResponse</a></code>

# Webhooks

Types:

```python
from miru_server_sdk.types import DeploymentValidateWebhookEvent, UnwrapWebhookEvent
```
