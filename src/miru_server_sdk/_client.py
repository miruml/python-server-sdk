# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import MiruError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import devices, releases, deployments, config_instances
    from .resources.devices import DevicesResource, AsyncDevicesResource
    from .resources.releases import ReleasesResource, AsyncReleasesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.deployments import DeploymentsResource, AsyncDeploymentsResource
    from .resources.config_instances import ConfigInstancesResource, AsyncConfigInstancesResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Miru",
    "AsyncMiru",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "prod": "https://api.mirurobotics.com/beta",
    "uat": "https://uat.api.mirurobotics.com/beta",
    "staging": "https://staging.api.mirurobotics.com/beta",
    "local": "http://localhost:8080/beta",
}


class Miru(SyncAPIClient):
    # client options
    api_key: str
    host: str
    version: str

    _environment: Literal["prod", "uat", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        version: str | None = None,
        environment: Literal["prod", "uat", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Miru client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MIRU_SERVER_API_KEY`
        - `host` from `MIRU_SERVER_HOST`
        - `version` from `MIRU_SERVER_VERSION`
        """
        if api_key is None:
            api_key = os.environ.get("MIRU_SERVER_API_KEY")
        if api_key is None:
            raise MiruError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MIRU_SERVER_API_KEY environment variable"
            )
        self.api_key = api_key

        if host is None:
            host = os.environ.get("MIRU_SERVER_HOST") or "api.mirurobotics.com"
        self.host = host

        if version is None:
            version = os.environ.get("MIRU_SERVER_VERSION") or "v1"
        self.version = version

        self._environment = environment

        base_url_env = os.environ.get("MIRU_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `MIRU_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "prod"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def config_instances(self) -> ConfigInstancesResource:
        from .resources.config_instances import ConfigInstancesResource

        return ConfigInstancesResource(self)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        from .resources.deployments import DeploymentsResource

        return DeploymentsResource(self)

    @cached_property
    def devices(self) -> DevicesResource:
        from .resources.devices import DevicesResource

        return DevicesResource(self)

    @cached_property
    def releases(self) -> ReleasesResource:
        from .resources.releases import ReleasesResource

        return ReleasesResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> MiruWithRawResponse:
        return MiruWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiruWithStreamedResponse:
        return MiruWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        version: str | None = None,
        environment: Literal["prod", "uat", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            host=host or self.host,
            version=version or self.version,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMiru(AsyncAPIClient):
    # client options
    api_key: str
    host: str
    version: str

    _environment: Literal["prod", "uat", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        version: str | None = None,
        environment: Literal["prod", "uat", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMiru client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MIRU_SERVER_API_KEY`
        - `host` from `MIRU_SERVER_HOST`
        - `version` from `MIRU_SERVER_VERSION`
        """
        if api_key is None:
            api_key = os.environ.get("MIRU_SERVER_API_KEY")
        if api_key is None:
            raise MiruError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MIRU_SERVER_API_KEY environment variable"
            )
        self.api_key = api_key

        if host is None:
            host = os.environ.get("MIRU_SERVER_HOST") or "api.mirurobotics.com"
        self.host = host

        if version is None:
            version = os.environ.get("MIRU_SERVER_VERSION") or "v1"
        self.version = version

        self._environment = environment

        base_url_env = os.environ.get("MIRU_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `MIRU_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "prod"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def config_instances(self) -> AsyncConfigInstancesResource:
        from .resources.config_instances import AsyncConfigInstancesResource

        return AsyncConfigInstancesResource(self)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        from .resources.deployments import AsyncDeploymentsResource

        return AsyncDeploymentsResource(self)

    @cached_property
    def devices(self) -> AsyncDevicesResource:
        from .resources.devices import AsyncDevicesResource

        return AsyncDevicesResource(self)

    @cached_property
    def releases(self) -> AsyncReleasesResource:
        from .resources.releases import AsyncReleasesResource

        return AsyncReleasesResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMiruWithRawResponse:
        return AsyncMiruWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiruWithStreamedResponse:
        return AsyncMiruWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        version: str | None = None,
        environment: Literal["prod", "uat", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            host=host or self.host,
            version=version or self.version,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MiruWithRawResponse:
    _client: Miru

    def __init__(self, client: Miru) -> None:
        self._client = client

    @cached_property
    def config_instances(self) -> config_instances.ConfigInstancesResourceWithRawResponse:
        from .resources.config_instances import ConfigInstancesResourceWithRawResponse

        return ConfigInstancesResourceWithRawResponse(self._client.config_instances)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithRawResponse:
        from .resources.deployments import DeploymentsResourceWithRawResponse

        return DeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def devices(self) -> devices.DevicesResourceWithRawResponse:
        from .resources.devices import DevicesResourceWithRawResponse

        return DevicesResourceWithRawResponse(self._client.devices)

    @cached_property
    def releases(self) -> releases.ReleasesResourceWithRawResponse:
        from .resources.releases import ReleasesResourceWithRawResponse

        return ReleasesResourceWithRawResponse(self._client.releases)


class AsyncMiruWithRawResponse:
    _client: AsyncMiru

    def __init__(self, client: AsyncMiru) -> None:
        self._client = client

    @cached_property
    def config_instances(self) -> config_instances.AsyncConfigInstancesResourceWithRawResponse:
        from .resources.config_instances import AsyncConfigInstancesResourceWithRawResponse

        return AsyncConfigInstancesResourceWithRawResponse(self._client.config_instances)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithRawResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithRawResponse

        return AsyncDeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def devices(self) -> devices.AsyncDevicesResourceWithRawResponse:
        from .resources.devices import AsyncDevicesResourceWithRawResponse

        return AsyncDevicesResourceWithRawResponse(self._client.devices)

    @cached_property
    def releases(self) -> releases.AsyncReleasesResourceWithRawResponse:
        from .resources.releases import AsyncReleasesResourceWithRawResponse

        return AsyncReleasesResourceWithRawResponse(self._client.releases)


class MiruWithStreamedResponse:
    _client: Miru

    def __init__(self, client: Miru) -> None:
        self._client = client

    @cached_property
    def config_instances(self) -> config_instances.ConfigInstancesResourceWithStreamingResponse:
        from .resources.config_instances import ConfigInstancesResourceWithStreamingResponse

        return ConfigInstancesResourceWithStreamingResponse(self._client.config_instances)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithStreamingResponse:
        from .resources.deployments import DeploymentsResourceWithStreamingResponse

        return DeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def devices(self) -> devices.DevicesResourceWithStreamingResponse:
        from .resources.devices import DevicesResourceWithStreamingResponse

        return DevicesResourceWithStreamingResponse(self._client.devices)

    @cached_property
    def releases(self) -> releases.ReleasesResourceWithStreamingResponse:
        from .resources.releases import ReleasesResourceWithStreamingResponse

        return ReleasesResourceWithStreamingResponse(self._client.releases)


class AsyncMiruWithStreamedResponse:
    _client: AsyncMiru

    def __init__(self, client: AsyncMiru) -> None:
        self._client = client

    @cached_property
    def config_instances(self) -> config_instances.AsyncConfigInstancesResourceWithStreamingResponse:
        from .resources.config_instances import AsyncConfigInstancesResourceWithStreamingResponse

        return AsyncConfigInstancesResourceWithStreamingResponse(self._client.config_instances)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithStreamingResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithStreamingResponse

        return AsyncDeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def devices(self) -> devices.AsyncDevicesResourceWithStreamingResponse:
        from .resources.devices import AsyncDevicesResourceWithStreamingResponse

        return AsyncDevicesResourceWithStreamingResponse(self._client.devices)

    @cached_property
    def releases(self) -> releases.AsyncReleasesResourceWithStreamingResponse:
        from .resources.releases import AsyncReleasesResourceWithStreamingResponse

        return AsyncReleasesResourceWithStreamingResponse(self._client.releases)


Client = Miru

AsyncClient = AsyncMiru
