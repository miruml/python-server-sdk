# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_server_sdk import Miru, AsyncMiru
from miru_server_sdk.types import (
    Device,
    DeviceListResponse,
    DeviceDeleteResponse,
    DeviceCreateActivationTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        device = client.devices.create(
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.devices.with_raw_response.create(
            name="Robot 1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.devices.with_streaming_response.create(
            name="Robot 1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        device = client.devices.retrieve(
            "dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.devices.with_raw_response.retrieve(
            "dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.devices.with_streaming_response.retrieve(
            "dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Miru) -> None:
        device = client.devices.update(
            device_id="dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Miru) -> None:
        device = client.devices.update(
            device_id="dvc_123",
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Miru) -> None:
        response = client.devices.with_raw_response.update(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Miru) -> None:
        with client.devices.with_streaming_response.update(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.update(
                device_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        device = client.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        device = client.devices.list(
            id="dev_123",
            expand=["total_count"],
            limit=1,
            name="My Device",
            offset=0,
            order_by="id:asc",
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Miru) -> None:
        device = client.devices.delete(
            "dvc_123",
        )
        assert_matches_type(DeviceDeleteResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Miru) -> None:
        response = client.devices.with_raw_response.delete(
            "dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceDeleteResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Miru) -> None:
        with client.devices.with_streaming_response.delete(
            "dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceDeleteResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_activation_token(self, client: Miru) -> None:
        device = client.devices.create_activation_token(
            device_id="dvc_123",
        )
        assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_activation_token_with_all_params(self, client: Miru) -> None:
        device = client.devices.create_activation_token(
            device_id="dvc_123",
            allow_reactivation=False,
        )
        assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_activation_token(self, client: Miru) -> None:
        response = client.devices.with_raw_response.create_activation_token(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_activation_token(self, client: Miru) -> None:
        with client.devices.with_streaming_response.create_activation_token(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_activation_token(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.create_activation_token(
                device_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stage(self, client: Miru) -> None:
        device = client.devices.stage(
            device_id="dvc_123",
            config_instances=[
                {
                    "config_schema_id": "cfg_sch_123",
                    "content": {
                        "direction": "forward",
                        "speed": 100,
                        "duration": 10,
                    },
                    "relative_filepath": "/v1/motion-control.json",
                }
            ],
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stage(self, client: Miru) -> None:
        response = client.devices.with_raw_response.stage(
            device_id="dvc_123",
            config_instances=[
                {
                    "config_schema_id": "cfg_sch_123",
                    "content": {
                        "direction": "forward",
                        "speed": 100,
                        "duration": 10,
                    },
                    "relative_filepath": "/v1/motion-control.json",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stage(self, client: Miru) -> None:
        with client.devices.with_streaming_response.stage(
            device_id="dvc_123",
            config_instances=[
                {
                    "config_schema_id": "cfg_sch_123",
                    "content": {
                        "direction": "forward",
                        "speed": 100,
                        "duration": 10,
                    },
                    "relative_filepath": "/v1/motion-control.json",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stage(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.stage(
                device_id="",
                config_instances=[
                    {
                        "config_schema_id": "cfg_sch_123",
                        "content": {
                            "direction": "forward",
                            "speed": 100,
                            "duration": 10,
                        },
                        "relative_filepath": "/v1/motion-control.json",
                    }
                ],
            )


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.create(
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.create(
            name="Robot 1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.create(
            name="Robot 1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.retrieve(
            "dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.retrieve(
            "dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.retrieve(
            "dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.update(
            device_id="dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.update(
            device_id="dvc_123",
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.update(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.update(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.update(
                device_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.list(
            id="dev_123",
            expand=["total_count"],
            limit=1,
            name="My Device",
            offset=0,
            order_by="id:asc",
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.delete(
            "dvc_123",
        )
        assert_matches_type(DeviceDeleteResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.delete(
            "dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceDeleteResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.delete(
            "dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceDeleteResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_activation_token(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.create_activation_token(
            device_id="dvc_123",
        )
        assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_activation_token_with_all_params(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.create_activation_token(
            device_id="dvc_123",
            allow_reactivation=False,
        )
        assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_activation_token(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.create_activation_token(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_activation_token(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.create_activation_token(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceCreateActivationTokenResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_activation_token(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.create_activation_token(
                device_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stage(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.stage(
            device_id="dvc_123",
            config_instances=[
                {
                    "config_schema_id": "cfg_sch_123",
                    "content": {
                        "direction": "forward",
                        "speed": 100,
                        "duration": 10,
                    },
                    "relative_filepath": "/v1/motion-control.json",
                }
            ],
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stage(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.stage(
            device_id="dvc_123",
            config_instances=[
                {
                    "config_schema_id": "cfg_sch_123",
                    "content": {
                        "direction": "forward",
                        "speed": 100,
                        "duration": 10,
                    },
                    "relative_filepath": "/v1/motion-control.json",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stage(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.stage(
            device_id="dvc_123",
            config_instances=[
                {
                    "config_schema_id": "cfg_sch_123",
                    "content": {
                        "direction": "forward",
                        "speed": 100,
                        "duration": 10,
                    },
                    "relative_filepath": "/v1/motion-control.json",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stage(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.stage(
                device_id="",
                config_instances=[
                    {
                        "config_schema_id": "cfg_sch_123",
                        "content": {
                            "direction": "forward",
                            "speed": 100,
                            "duration": 10,
                        },
                        "relative_filepath": "/v1/motion-control.json",
                    }
                ],
            )
