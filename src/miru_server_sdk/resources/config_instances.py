# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    config_instance_list_params,
    config_instance_deploy_params,
    config_instance_reject_params,
    config_instance_approve_params,
    config_instance_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.config_instance import ConfigInstance
from ..types.config_instance_list_response import ConfigInstanceListResponse
from ..types.config_instance_deploy_response import ConfigInstanceDeployResponse

__all__ = ["ConfigInstancesResource", "AsyncConfigInstancesResource"]


class ConfigInstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return ConfigInstancesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        config_instance_id: str,
        *,
        expand: List[Literal["content", "config_schema", "device", "config_type"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstance:
        """
        Get a config instance by ID

        Args:
          expand: The fields to expand in the config instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return self._get(
            f"/config_instances/{config_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_instance_retrieve_params.ConfigInstanceRetrieveParams),
            ),
            cast_to=ConfigInstance,
        )

    def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        activity_status: Literal["created", "validating", "validated", "queued", "deployed", "removed"]
        | NotGiven = NOT_GIVEN,
        config_schema_id: str | NotGiven = NOT_GIVEN,
        config_type_id: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        error_status: Literal["none", "failed", "retrying"] | NotGiven = NOT_GIVEN,
        expand: List[Literal["total_count", "content", "config_schema", "device", "config_type"]]
        | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | NotGiven = NOT_GIVEN,
        target_status: Literal["created", "validated", "deployed", "removed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstanceListResponse:
        """
        List config instances

        Args:
          id: The config instance ID to filter by

          activity_status: The config instance activity status to filter by

          config_schema_id: The config schema ID to filter by

          config_type_id: The config type ID to filter by

          device_id: The device ID to filter by

          error_status: The config instance error status to filter by

          expand: The fields to expand in the config instance list

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          target_status: The config instance target status to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config_instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "activity_status": activity_status,
                        "config_schema_id": config_schema_id,
                        "config_type_id": config_type_id,
                        "device_id": device_id,
                        "error_status": error_status,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "target_status": target_status,
                    },
                    config_instance_list_params.ConfigInstanceListParams,
                ),
            ),
            cast_to=ConfigInstanceListResponse,
        )

    def approve(
        self,
        config_instance_id: str,
        *,
        message: str,
        expand: List[Literal["content", "config_schema", "device", "config_type"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstance:
        """
        Approve a config instance for deployment

        Args:
          message: A high level success message displayed to the user

          expand: The fields to expand in the config instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return self._post(
            f"/config_instances/{config_instance_id}/approve",
            body=maybe_transform({"message": message}, config_instance_approve_params.ConfigInstanceApproveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_instance_approve_params.ConfigInstanceApproveParams),
            ),
            cast_to=ConfigInstance,
        )

    def deploy(
        self,
        config_instance_id: str,
        *,
        dry_run: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstanceDeployResponse:
        """
        Deploy a config instance to a device

        Args:
          dry_run: Perform a dry run that simulates the operation without making actual changes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return self._post(
            f"/config_instances/{config_instance_id}/deploy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, config_instance_deploy_params.ConfigInstanceDeployParams),
            ),
            cast_to=ConfigInstanceDeployResponse,
        )

    def reject(
        self,
        config_instance_id: str,
        *,
        errors: Iterable[config_instance_reject_params.Error],
        message: str,
        expand: List[Literal["content", "config_schema", "device", "config_type"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstance:
        """
        Reject a config instance for deployment

        Args:
          message: A high level error message displayed to the user

          expand: The fields to expand in the config instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return self._post(
            f"/config_instances/{config_instance_id}/reject",
            body=maybe_transform(
                {
                    "errors": errors,
                    "message": message,
                },
                config_instance_reject_params.ConfigInstanceRejectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_instance_reject_params.ConfigInstanceRejectParams),
            ),
            cast_to=ConfigInstance,
        )


class AsyncConfigInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return AsyncConfigInstancesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        config_instance_id: str,
        *,
        expand: List[Literal["content", "config_schema", "device", "config_type"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstance:
        """
        Get a config instance by ID

        Args:
          expand: The fields to expand in the config instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return await self._get(
            f"/config_instances/{config_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_instance_retrieve_params.ConfigInstanceRetrieveParams
                ),
            ),
            cast_to=ConfigInstance,
        )

    async def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        activity_status: Literal["created", "validating", "validated", "queued", "deployed", "removed"]
        | NotGiven = NOT_GIVEN,
        config_schema_id: str | NotGiven = NOT_GIVEN,
        config_type_id: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        error_status: Literal["none", "failed", "retrying"] | NotGiven = NOT_GIVEN,
        expand: List[Literal["total_count", "content", "config_schema", "device", "config_type"]]
        | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | NotGiven = NOT_GIVEN,
        target_status: Literal["created", "validated", "deployed", "removed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstanceListResponse:
        """
        List config instances

        Args:
          id: The config instance ID to filter by

          activity_status: The config instance activity status to filter by

          config_schema_id: The config schema ID to filter by

          config_type_id: The config type ID to filter by

          device_id: The device ID to filter by

          error_status: The config instance error status to filter by

          expand: The fields to expand in the config instance list

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          target_status: The config instance target status to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config_instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "activity_status": activity_status,
                        "config_schema_id": config_schema_id,
                        "config_type_id": config_type_id,
                        "device_id": device_id,
                        "error_status": error_status,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "target_status": target_status,
                    },
                    config_instance_list_params.ConfigInstanceListParams,
                ),
            ),
            cast_to=ConfigInstanceListResponse,
        )

    async def approve(
        self,
        config_instance_id: str,
        *,
        message: str,
        expand: List[Literal["content", "config_schema", "device", "config_type"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstance:
        """
        Approve a config instance for deployment

        Args:
          message: A high level success message displayed to the user

          expand: The fields to expand in the config instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return await self._post(
            f"/config_instances/{config_instance_id}/approve",
            body=await async_maybe_transform(
                {"message": message}, config_instance_approve_params.ConfigInstanceApproveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_instance_approve_params.ConfigInstanceApproveParams
                ),
            ),
            cast_to=ConfigInstance,
        )

    async def deploy(
        self,
        config_instance_id: str,
        *,
        dry_run: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstanceDeployResponse:
        """
        Deploy a config instance to a device

        Args:
          dry_run: Perform a dry run that simulates the operation without making actual changes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return await self._post(
            f"/config_instances/{config_instance_id}/deploy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dry_run": dry_run}, config_instance_deploy_params.ConfigInstanceDeployParams
                ),
            ),
            cast_to=ConfigInstanceDeployResponse,
        )

    async def reject(
        self,
        config_instance_id: str,
        *,
        errors: Iterable[config_instance_reject_params.Error],
        message: str,
        expand: List[Literal["content", "config_schema", "device", "config_type"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstance:
        """
        Reject a config instance for deployment

        Args:
          message: A high level error message displayed to the user

          expand: The fields to expand in the config instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return await self._post(
            f"/config_instances/{config_instance_id}/reject",
            body=await async_maybe_transform(
                {
                    "errors": errors,
                    "message": message,
                },
                config_instance_reject_params.ConfigInstanceRejectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_instance_reject_params.ConfigInstanceRejectParams
                ),
            ),
            cast_to=ConfigInstance,
        )


class ConfigInstancesResourceWithRawResponse:
    def __init__(self, config_instances: ConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve = to_raw_response_wrapper(
            config_instances.retrieve,
        )
        self.list = to_raw_response_wrapper(
            config_instances.list,
        )
        self.approve = to_raw_response_wrapper(
            config_instances.approve,
        )
        self.deploy = to_raw_response_wrapper(
            config_instances.deploy,
        )
        self.reject = to_raw_response_wrapper(
            config_instances.reject,
        )


class AsyncConfigInstancesResourceWithRawResponse:
    def __init__(self, config_instances: AsyncConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve = async_to_raw_response_wrapper(
            config_instances.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            config_instances.list,
        )
        self.approve = async_to_raw_response_wrapper(
            config_instances.approve,
        )
        self.deploy = async_to_raw_response_wrapper(
            config_instances.deploy,
        )
        self.reject = async_to_raw_response_wrapper(
            config_instances.reject,
        )


class ConfigInstancesResourceWithStreamingResponse:
    def __init__(self, config_instances: ConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve = to_streamed_response_wrapper(
            config_instances.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            config_instances.list,
        )
        self.approve = to_streamed_response_wrapper(
            config_instances.approve,
        )
        self.deploy = to_streamed_response_wrapper(
            config_instances.deploy,
        )
        self.reject = to_streamed_response_wrapper(
            config_instances.reject,
        )


class AsyncConfigInstancesResourceWithStreamingResponse:
    def __init__(self, config_instances: AsyncConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve = async_to_streamed_response_wrapper(
            config_instances.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            config_instances.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            config_instances.approve,
        )
        self.deploy = async_to_streamed_response_wrapper(
            config_instances.deploy,
        )
        self.reject = async_to_streamed_response_wrapper(
            config_instances.reject,
        )
