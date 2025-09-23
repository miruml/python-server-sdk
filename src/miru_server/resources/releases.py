# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import release_list_params, release_retrieve_params
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
from ..types.release import Release
from ..types.release_list_response import ReleaseListResponse

__all__ = ["ReleasesResource", "AsyncReleasesResource"]


class ReleasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return ReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return ReleasesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        release_id: str,
        *,
        expand: List[Literal["config_schemas"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Release:
        """
        Retrieve a release by ID.

        Args:
          expand: The fields to expand in the releases.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not release_id:
            raise ValueError(f"Expected a non-empty value for `release_id` but received {release_id!r}")
        return self._get(
            f"/releases/{release_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, release_retrieve_params.ReleaseRetrieveParams),
            ),
            cast_to=Release,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        expand: List[Literal["total_count", "config_schemas"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseListResponse:
        """
        List releases.

        Args:
          id: The release ID to filter by.

          expand: The fields to expand in the releases list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          version: The release version to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/releases",
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
                        "offset": offset,
                        "order_by": order_by,
                        "version": version,
                    },
                    release_list_params.ReleaseListParams,
                ),
            ),
            cast_to=ReleaseListResponse,
        )


class AsyncReleasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-server-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-server-sdk#with_streaming_response
        """
        return AsyncReleasesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        release_id: str,
        *,
        expand: List[Literal["config_schemas"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Release:
        """
        Retrieve a release by ID.

        Args:
          expand: The fields to expand in the releases.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not release_id:
            raise ValueError(f"Expected a non-empty value for `release_id` but received {release_id!r}")
        return await self._get(
            f"/releases/{release_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, release_retrieve_params.ReleaseRetrieveParams),
            ),
            cast_to=Release,
        )

    async def list(
        self,
        *,
        id: str | Omit = omit,
        expand: List[Literal["total_count", "config_schemas"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"] | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseListResponse:
        """
        List releases.

        Args:
          id: The release ID to filter by.

          expand: The fields to expand in the releases list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          version: The release version to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/releases",
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
                        "offset": offset,
                        "order_by": order_by,
                        "version": version,
                    },
                    release_list_params.ReleaseListParams,
                ),
            ),
            cast_to=ReleaseListResponse,
        )


class ReleasesResourceWithRawResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.retrieve = to_raw_response_wrapper(
            releases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            releases.list,
        )


class AsyncReleasesResourceWithRawResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.retrieve = async_to_raw_response_wrapper(
            releases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            releases.list,
        )


class ReleasesResourceWithStreamingResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.retrieve = to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            releases.list,
        )


class AsyncReleasesResourceWithStreamingResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.retrieve = async_to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            releases.list,
        )
