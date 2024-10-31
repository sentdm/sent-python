# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    contact_id: Annotated[str, PropertyInfo(alias="contactId")]

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]