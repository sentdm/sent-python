# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SentError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Sent",
    "AsyncSent",
    "Client",
    "AsyncClient",
]


class Sent(SyncAPIClient):
    contact: resources.ContactResource
    contacts: resources.ContactsResource
    messages: resources.MessagesResource
    sms: resources.SMSResource
    whatsapp: resources.WhatsappResource
    templates: resources.TemplatesResource
    customers: resources.CustomersResource
    with_raw_response: SentWithRawResponse
    with_streaming_response: SentWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new synchronous sent client instance.

        This automatically infers the `api_key` argument from the `X_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("X_API_KEY")
        if api_key is None:
            raise SentError(
                "The api_key client option must be set either by passing api_key to the client or by setting the X_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SENT_BASE_URL")
        if base_url is None:
            base_url = f"https://sent-dm-dev.azurewebsites.net"

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

        self.contact = resources.ContactResource(self)
        self.contacts = resources.ContactsResource(self)
        self.messages = resources.MessagesResource(self)
        self.sms = resources.SMSResource(self)
        self.whatsapp = resources.WhatsappResource(self)
        self.templates = resources.TemplatesResource(self)
        self.customers = resources.CustomersResource(self)
        self.with_raw_response = SentWithRawResponse(self)
        self.with_streaming_response = SentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

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
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            base_url=base_url or self.base_url,
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


class AsyncSent(AsyncAPIClient):
    contact: resources.AsyncContactResource
    contacts: resources.AsyncContactsResource
    messages: resources.AsyncMessagesResource
    sms: resources.AsyncSMSResource
    whatsapp: resources.AsyncWhatsappResource
    templates: resources.AsyncTemplatesResource
    customers: resources.AsyncCustomersResource
    with_raw_response: AsyncSentWithRawResponse
    with_streaming_response: AsyncSentWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new async sent client instance.

        This automatically infers the `api_key` argument from the `X_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("X_API_KEY")
        if api_key is None:
            raise SentError(
                "The api_key client option must be set either by passing api_key to the client or by setting the X_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SENT_BASE_URL")
        if base_url is None:
            base_url = f"https://sent-dm-dev.azurewebsites.net"

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

        self.contact = resources.AsyncContactResource(self)
        self.contacts = resources.AsyncContactsResource(self)
        self.messages = resources.AsyncMessagesResource(self)
        self.sms = resources.AsyncSMSResource(self)
        self.whatsapp = resources.AsyncWhatsappResource(self)
        self.templates = resources.AsyncTemplatesResource(self)
        self.customers = resources.AsyncCustomersResource(self)
        self.with_raw_response = AsyncSentWithRawResponse(self)
        self.with_streaming_response = AsyncSentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

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
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            base_url=base_url or self.base_url,
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


class SentWithRawResponse:
    def __init__(self, client: Sent) -> None:
        self.contact = resources.ContactResourceWithRawResponse(client.contact)
        self.contacts = resources.ContactsResourceWithRawResponse(client.contacts)
        self.messages = resources.MessagesResourceWithRawResponse(client.messages)
        self.sms = resources.SMSResourceWithRawResponse(client.sms)
        self.whatsapp = resources.WhatsappResourceWithRawResponse(client.whatsapp)
        self.templates = resources.TemplatesResourceWithRawResponse(client.templates)
        self.customers = resources.CustomersResourceWithRawResponse(client.customers)


class AsyncSentWithRawResponse:
    def __init__(self, client: AsyncSent) -> None:
        self.contact = resources.AsyncContactResourceWithRawResponse(client.contact)
        self.contacts = resources.AsyncContactsResourceWithRawResponse(client.contacts)
        self.messages = resources.AsyncMessagesResourceWithRawResponse(client.messages)
        self.sms = resources.AsyncSMSResourceWithRawResponse(client.sms)
        self.whatsapp = resources.AsyncWhatsappResourceWithRawResponse(client.whatsapp)
        self.templates = resources.AsyncTemplatesResourceWithRawResponse(client.templates)
        self.customers = resources.AsyncCustomersResourceWithRawResponse(client.customers)


class SentWithStreamedResponse:
    def __init__(self, client: Sent) -> None:
        self.contact = resources.ContactResourceWithStreamingResponse(client.contact)
        self.contacts = resources.ContactsResourceWithStreamingResponse(client.contacts)
        self.messages = resources.MessagesResourceWithStreamingResponse(client.messages)
        self.sms = resources.SMSResourceWithStreamingResponse(client.sms)
        self.whatsapp = resources.WhatsappResourceWithStreamingResponse(client.whatsapp)
        self.templates = resources.TemplatesResourceWithStreamingResponse(client.templates)
        self.customers = resources.CustomersResourceWithStreamingResponse(client.customers)


class AsyncSentWithStreamedResponse:
    def __init__(self, client: AsyncSent) -> None:
        self.contact = resources.AsyncContactResourceWithStreamingResponse(client.contact)
        self.contacts = resources.AsyncContactsResourceWithStreamingResponse(client.contacts)
        self.messages = resources.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.sms = resources.AsyncSMSResourceWithStreamingResponse(client.sms)
        self.whatsapp = resources.AsyncWhatsappResourceWithStreamingResponse(client.whatsapp)
        self.templates = resources.AsyncTemplatesResourceWithStreamingResponse(client.templates)
        self.customers = resources.AsyncCustomersResourceWithStreamingResponse(client.customers)


Client = Sent

AsyncClient = AsyncSent
