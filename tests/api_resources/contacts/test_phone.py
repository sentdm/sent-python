# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent.types.shared import Contact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        phone = client.contacts.phone.retrieve(
            phone_number="phoneNumber",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Contact, phone, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.contacts.phone.with_raw_response.retrieve(
            phone_number="phoneNumber",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = response.parse()
        assert_matches_type(Contact, phone, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.contacts.phone.with_streaming_response.retrieve(
            phone_number="phoneNumber",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = response.parse()
            assert_matches_type(Contact, phone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.contacts.phone.with_raw_response.retrieve(
                phone_number="phoneNumber",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.contacts.phone.with_raw_response.retrieve(
                phone_number="",
                customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncPhone:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        phone = await async_client.contacts.phone.retrieve(
            phone_number="phoneNumber",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Contact, phone, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.contacts.phone.with_raw_response.retrieve(
            phone_number="phoneNumber",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = await response.parse()
        assert_matches_type(Contact, phone, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.contacts.phone.with_streaming_response.retrieve(
            phone_number="phoneNumber",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = await response.parse()
            assert_matches_type(Contact, phone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.contacts.phone.with_raw_response.retrieve(
                phone_number="phoneNumber",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.contacts.phone.with_raw_response.retrieve(
                phone_number="",
                customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )