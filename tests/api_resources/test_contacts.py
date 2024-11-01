# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Sent) -> None:
        contact = client.contacts.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            page_size=0,
        )
        assert_matches_type(object, contact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.contacts.with_raw_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(object, contact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.contacts.with_streaming_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(object, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        contact = await async_client.contacts.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            page_size=0,
        )
        assert_matches_type(object, contact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.contacts.with_raw_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(object, contact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.contacts.with_streaming_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(object, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
