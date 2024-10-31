# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from sent.types import SentDmServicesContractsDataCustomerDto
from sent._utils import parse_datetime
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        customer = client.customers.retrieve(
            "id",
        )
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.customers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.customers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Sent) -> None:
        customer = client.customers.update(
            id="id",
        )
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        customer = client.customers.update(
            id="id",
            customer={
                "id": "id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "name": "name",
                "sending_phone_number": "sendingPhoneNumber",
                "sms_bearer_token": "smsBearerToken",
                "sms_default_webhook_url": "smsDefaultWebhookUrl",
                "sms_messaging_profile_id": "smsMessagingProfileId",
                "sms_webhook_failover_url": "smsWebhookFailoverUrl",
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "whatsapp_business_associate_id": "whatsappBusinessAssociateId",
                "whatsapp_phone_number_id": "whatsappPhoneNumberId",
                "whatsapp_system_user_access_token": "whatsappSystemUserAccessToken",
            },
        )
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.customers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.customers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        customer = client.customers.delete(
            "id",
        )
        assert_matches_type(object, customer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.customers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(object, customer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.customers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(object, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.with_raw_response.delete(
                "",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        customer = await async_client.customers.retrieve(
            "id",
        )
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.customers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.customers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        customer = await async_client.customers.update(
            id="id",
        )
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        customer = await async_client.customers.update(
            id="id",
            customer={
                "id": "id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "name": "name",
                "sending_phone_number": "sendingPhoneNumber",
                "sms_bearer_token": "smsBearerToken",
                "sms_default_webhook_url": "smsDefaultWebhookUrl",
                "sms_messaging_profile_id": "smsMessagingProfileId",
                "sms_webhook_failover_url": "smsWebhookFailoverUrl",
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "whatsapp_business_associate_id": "whatsappBusinessAssociateId",
                "whatsapp_phone_number_id": "whatsappPhoneNumberId",
                "whatsapp_system_user_access_token": "whatsappSystemUserAccessToken",
            },
        )
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.customers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.customers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(SentDmServicesContractsDataCustomerDto, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        customer = await async_client.customers.delete(
            "id",
        )
        assert_matches_type(object, customer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.customers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(object, customer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.customers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(object, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.with_raw_response.delete(
                "",
            )
