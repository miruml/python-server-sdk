# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_server_sdk import Miru, AsyncMiru
from miru_server_sdk.types import (
    ConfigInstance,
    ConfigInstanceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        config_instance = client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        config_instance = client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
            expand=["content"],
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.config_instances.with_raw_response.retrieve(
            config_instance_id="cfg_inst_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = response.parse()
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.config_instances.with_streaming_response.retrieve(
            config_instance_id="cfg_inst_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = response.parse()
            assert_matches_type(ConfigInstance, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_instance_id` but received ''"):
            client.config_instances.with_raw_response.retrieve(
                config_instance_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        config_instance = client.config_instances.list()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        config_instance = client.config_instances.list(
            id="cfg_inst_123",
            activity_status="created",
            config_schema_id="cfg_sch_123",
            config_type_id="cfg_typ_123",
            device_id="dvc_123",
            error_status="none",
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by="id:asc",
            target_status="created",
        )
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.config_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = response.parse()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.config_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = response.parse()
            assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
            expand=["content"],
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_instances.with_raw_response.retrieve(
            config_instance_id="cfg_inst_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = await response.parse()
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.config_instances.with_streaming_response.retrieve(
            config_instance_id="cfg_inst_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = await response.parse()
            assert_matches_type(ConfigInstance, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_instance_id` but received ''"):
            await async_client.config_instances.with_raw_response.retrieve(
                config_instance_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.list()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.list(
            id="cfg_inst_123",
            activity_status="created",
            config_schema_id="cfg_sch_123",
            config_type_id="cfg_typ_123",
            device_id="dvc_123",
            error_status="none",
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by="id:asc",
            target_status="created",
        )
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = await response.parse()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.config_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = await response.parse()
            assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True
