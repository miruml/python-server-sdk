# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    device_list_params,
    device_stage_params,
    device_create_params,
    device_update_params,
    device_create_activation_token_params,
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
from ..types.device import Device
from ..types.device_list_response import DeviceListResponse
from ..types.device_delete_response import DeviceDeleteResponse
from ..types.device_create_activation_token_response import DeviceCreateActivationTokenResponse

__all__ = ["DevicesResource", "AsyncDevicesResource"]


class DevicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return DevicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """
        Create a new device

        Args:
          name: The name of the device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/devices",
            body=maybe_transform({"name": name}, device_create_params.DeviceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    def retrieve(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """
        Get a device by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            f"/devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    def update(
        self,
        device_id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """Update a device by ID

        Args:
          name: The new name of the device.

        If null or excluded from the request, the device
              name is not updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._patch(
            f"/devices/{device_id}",
            body=maybe_transform({"name": name}, device_update_params.DeviceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["total_count"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceListResponse:
        """
        List devices

        Args:
          id: The device ID to filter by

          expand: The fields to expand in the device list

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The device name to filter by

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            cast_to=DeviceListResponse,
        )

    def delete(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceDeleteResponse:
        """
        Delete a device by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._delete(
            f"/devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceDeleteResponse,
        )

    def create_activation_token(
        self,
        device_id: str,
        *,
        allow_reactivation: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCreateActivationTokenResponse:
        """
        Create a new device activation token

        Args:
          allow_reactivation: Whether this token can reactivate already activated devices. If false, the token
              is unable to activate devices which are already activated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._post(
            f"/devices/{device_id}/activation_token",
            body=maybe_transform(
                {"allow_reactivation": allow_reactivation},
                device_create_activation_token_params.DeviceCreateActivationTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCreateActivationTokenResponse,
        )

    def stage(
        self,
        device_id: str,
        *,
        config_instances: Iterable[device_stage_params.ConfigInstance],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """
        Stage a device

        Args:
          config_instances: The config instances to stage on the device. These config instances will be
              deployed to the device as soon as it is activated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._post(
            f"/devices/{device_id}/stage",
            body=maybe_transform({"config_instances": config_instances}, device_stage_params.DeviceStageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )


class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return AsyncDevicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """
        Create a new device

        Args:
          name: The name of the device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/devices",
            body=await async_maybe_transform({"name": name}, device_create_params.DeviceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    async def retrieve(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """
        Get a device by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            f"/devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    async def update(
        self,
        device_id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """Update a device by ID

        Args:
          name: The new name of the device.

        If null or excluded from the request, the device
              name is not updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._patch(
            f"/devices/{device_id}",
            body=await async_maybe_transform({"name": name}, device_update_params.DeviceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    async def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["total_count"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceListResponse:
        """
        List devices

        Args:
          id: The device ID to filter by

          expand: The fields to expand in the device list

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The device name to filter by

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            cast_to=DeviceListResponse,
        )

    async def delete(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceDeleteResponse:
        """
        Delete a device by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._delete(
            f"/devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceDeleteResponse,
        )

    async def create_activation_token(
        self,
        device_id: str,
        *,
        allow_reactivation: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceCreateActivationTokenResponse:
        """
        Create a new device activation token

        Args:
          allow_reactivation: Whether this token can reactivate already activated devices. If false, the token
              is unable to activate devices which are already activated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._post(
            f"/devices/{device_id}/activation_token",
            body=await async_maybe_transform(
                {"allow_reactivation": allow_reactivation},
                device_create_activation_token_params.DeviceCreateActivationTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCreateActivationTokenResponse,
        )

    async def stage(
        self,
        device_id: str,
        *,
        config_instances: Iterable[device_stage_params.ConfigInstance],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Device:
        """
        Stage a device

        Args:
          config_instances: The config instances to stage on the device. These config instances will be
              deployed to the device as soon as it is activated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._post(
            f"/devices/{device_id}/stage",
            body=await async_maybe_transform(
                {"config_instances": config_instances}, device_stage_params.DeviceStageParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.create = to_raw_response_wrapper(
            devices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            devices.retrieve,
        )
        self.update = to_raw_response_wrapper(
            devices.update,
        )
        self.list = to_raw_response_wrapper(
            devices.list,
        )
        self.delete = to_raw_response_wrapper(
            devices.delete,
        )
        self.create_activation_token = to_raw_response_wrapper(
            devices.create_activation_token,
        )
        self.stage = to_raw_response_wrapper(
            devices.stage,
        )


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.create = async_to_raw_response_wrapper(
            devices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            devices.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            devices.update,
        )
        self.list = async_to_raw_response_wrapper(
            devices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            devices.delete,
        )
        self.create_activation_token = async_to_raw_response_wrapper(
            devices.create_activation_token,
        )
        self.stage = async_to_raw_response_wrapper(
            devices.stage,
        )


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.create = to_streamed_response_wrapper(
            devices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            devices.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            devices.update,
        )
        self.list = to_streamed_response_wrapper(
            devices.list,
        )
        self.delete = to_streamed_response_wrapper(
            devices.delete,
        )
        self.create_activation_token = to_streamed_response_wrapper(
            devices.create_activation_token,
        )
        self.stage = to_streamed_response_wrapper(
            devices.stage,
        )


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.create = async_to_streamed_response_wrapper(
            devices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            devices.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            devices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            devices.delete,
        )
        self.create_activation_token = async_to_streamed_response_wrapper(
            devices.create_activation_token,
        )
        self.stage = async_to_streamed_response_wrapper(
            devices.stage,
        )
