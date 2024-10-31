# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .sent_dm_services_contracts_data_customer_dto_param import SentDmServicesContractsDataCustomerDtoParam

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    customer: SentDmServicesContractsDataCustomerDtoParam
