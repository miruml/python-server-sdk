# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    deployment_list_params,
    deployment_create_params,
    deployment_retrieve_params,
    deployment_validate_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.deployment import Deployment
from ..types.deployment_list_response import DeploymentListResponse
from ..types.deployment_validate_response import DeploymentValidateResponse

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        device_id: str,
        new_config_instances: Iterable[deployment_create_params.NewConfigInstance],
        release_id: str,
        target_status: Literal["staged", "deployed"],
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        patch_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Stage or deploy a new deployment.

        Args:
          description: The description of the deployment.

          device_id: The ID of the device that the deployment is being created for.

          new_config_instances: The _new_ config instances to create for this deployment. A deployment must have
              exactly one config instance for each config schema in the deployment's release.
              If less config instances are provided than the number of schemas, the deployment
              will 'transfer' config instances from the deployment it is patched from.
              Archived config instances cannot be transferred.

          release_id: The release ID which this deployment adheres to.

          target_status: Desired state of the deployment.

              - Staged: ready for deployment. Deployments can only be staged if their release
                is not the current release for the device.
              - Deployed: deployed to the device. Deployments can only be deployed if their
                release is the device's current release.

              If custom validation is enabled for the release, the deployment must pass
              validation before fulfilling the target status.

          expand: The fields to expand in the deployment.

          patch_source_id: The ID of the deployment that this deployment was patched from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/deployments",
            body=maybe_transform(
                {
                    "description": description,
                    "device_id": device_id,
                    "new_config_instances": new_config_instances,
                    "release_id": release_id,
                    "target_status": target_status,
                    "patch_source_id": patch_source_id,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_create_params.DeploymentCreateParams),
            ),
            cast_to=Deployment,
        )

    def retrieve(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Get

        Args:
          expand: The fields to expand in the deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            f"/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_retrieve_params.DeploymentRetrieveParams),
            ),
            cast_to=Deployment,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        activity_status: Literal["validating", "needs_review", "staged", "queued", "deployed", "removing", "archived"]
        | Omit = omit,
        device_id: str | Omit = omit,
        error_status: Literal["none", "failed", "retrying"] | Omit = omit,
        expand: List[Literal["total_count", "device", "release", "config_instances"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | Omit = omit,
        release_id: str | Omit = omit,
        target_status: Literal["staged", "deployed", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentListResponse:
        """
        List

        Args:
          id: The deployment ID to filter by.

          activity_status: The deployment activity status to filter by.

          device_id: The deployment device ID to filter by.

          error_status: The deployment error status to filter by.

          expand: The fields to expand in the deployments list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          release_id: The deployment release ID to filter by.

          target_status: The deployment target status to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "activity_status": activity_status,
                        "device_id": device_id,
                        "error_status": error_status,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "release_id": release_id,
                        "target_status": target_status,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            cast_to=DeploymentListResponse,
        )

    def validate(
        self,
        deployment_id: str,
        *,
        config_instances: Iterable[deployment_validate_params.ConfigInstance],
        is_valid: bool,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentValidateResponse:
        """
        Validate a deployment with your custom validation.

        Args:
          config_instances: The config instance errors for this deployment.

          is_valid: Whether the deployment is valid. If invalid, the deployment is immediately
              archived and marked as 'failed'.

          message: A message displayed on the deployment level in the UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            f"/deployments/{deployment_id}/validate",
            body=maybe_transform(
                {
                    "config_instances": config_instances,
                    "is_valid": is_valid,
                    "message": message,
                },
                deployment_validate_params.DeploymentValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentValidateResponse,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        device_id: str,
        new_config_instances: Iterable[deployment_create_params.NewConfigInstance],
        release_id: str,
        target_status: Literal["staged", "deployed"],
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        patch_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Stage or deploy a new deployment.

        Args:
          description: The description of the deployment.

          device_id: The ID of the device that the deployment is being created for.

          new_config_instances: The _new_ config instances to create for this deployment. A deployment must have
              exactly one config instance for each config schema in the deployment's release.
              If less config instances are provided than the number of schemas, the deployment
              will 'transfer' config instances from the deployment it is patched from.
              Archived config instances cannot be transferred.

          release_id: The release ID which this deployment adheres to.

          target_status: Desired state of the deployment.

              - Staged: ready for deployment. Deployments can only be staged if their release
                is not the current release for the device.
              - Deployed: deployed to the device. Deployments can only be deployed if their
                release is the device's current release.

              If custom validation is enabled for the release, the deployment must pass
              validation before fulfilling the target status.

          expand: The fields to expand in the deployment.

          patch_source_id: The ID of the deployment that this deployment was patched from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/deployments",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "device_id": device_id,
                    "new_config_instances": new_config_instances,
                    "release_id": release_id,
                    "target_status": target_status,
                    "patch_source_id": patch_source_id,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, deployment_create_params.DeploymentCreateParams),
            ),
            cast_to=Deployment,
        )

    async def retrieve(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Get

        Args:
          expand: The fields to expand in the deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            f"/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, deployment_retrieve_params.DeploymentRetrieveParams
                ),
            ),
            cast_to=Deployment,
        )

    async def list(
        self,
        *,
        id: str | Omit = omit,
        activity_status: Literal["validating", "needs_review", "staged", "queued", "deployed", "removing", "archived"]
        | Omit = omit,
        device_id: str | Omit = omit,
        error_status: Literal["none", "failed", "retrying"] | Omit = omit,
        expand: List[Literal["total_count", "device", "release", "config_instances"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | Omit = omit,
        release_id: str | Omit = omit,
        target_status: Literal["staged", "deployed", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentListResponse:
        """
        List

        Args:
          id: The deployment ID to filter by.

          activity_status: The deployment activity status to filter by.

          device_id: The deployment device ID to filter by.

          error_status: The deployment error status to filter by.

          expand: The fields to expand in the deployments list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          release_id: The deployment release ID to filter by.

          target_status: The deployment target status to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "activity_status": activity_status,
                        "device_id": device_id,
                        "error_status": error_status,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "release_id": release_id,
                        "target_status": target_status,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            cast_to=DeploymentListResponse,
        )

    async def validate(
        self,
        deployment_id: str,
        *,
        config_instances: Iterable[deployment_validate_params.ConfigInstance],
        is_valid: bool,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentValidateResponse:
        """
        Validate a deployment with your custom validation.

        Args:
          config_instances: The config instance errors for this deployment.

          is_valid: Whether the deployment is valid. If invalid, the deployment is immediately
              archived and marked as 'failed'.

          message: A message displayed on the deployment level in the UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            f"/deployments/{deployment_id}/validate",
            body=await async_maybe_transform(
                {
                    "config_instances": config_instances,
                    "is_valid": is_valid,
                    "message": message,
                },
                deployment_validate_params.DeploymentValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentValidateResponse,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deployments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deployments.list,
        )
        self.validate = to_raw_response_wrapper(
            deployments.validate,
        )


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deployments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deployments.list,
        )
        self.validate = async_to_raw_response_wrapper(
            deployments.validate,
        )


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deployments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deployments.list,
        )
        self.validate = to_streamed_response_wrapper(
            deployments.validate,
        )


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deployments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deployments.list,
        )
        self.validate = async_to_streamed_response_wrapper(
            deployments.validate,
        )
