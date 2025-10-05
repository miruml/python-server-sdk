# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_server_sdk import Miru, AsyncMiru
from miru_server_sdk.types import Release, ReleaseListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReleases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        release = client.releases.retrieve(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        release = client.releases.retrieve(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.releases.with_raw_response.retrieve(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.releases.with_streaming_response.retrieve(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            client.releases.with_raw_response.retrieve(
                release_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        release = client.releases.list()
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        release = client.releases.list(
            id="rls_123",
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by="id:asc",
            version="v1.0.0",
        )
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.releases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.releases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(ReleaseListResponse, release, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReleases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.retrieve(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.retrieve(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.retrieve(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.retrieve(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            await async_client.releases.with_raw_response.retrieve(
                release_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.list()
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.list(
            id="rls_123",
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by="id:asc",
            version="v1.0.0",
        )
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(ReleaseListResponse, release, path=["response"])

        assert cast(Any, response.is_closed) is True
