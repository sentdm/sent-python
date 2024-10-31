# Shared Types

```python
from sent.types import SentDmServicesContractsDataContactDto
```

# Contact

## ID

Methods:

- <code title="get /contact/{customerId}/id/{id}">client.contact.id.<a href="./src/sent/resources/contact/id.py">retrieve</a>(id, \*, customer_id) -> <a href="./src/sent/types/shared/sent_dm_services_contracts_data_contact_dto.py">SentDmServicesContractsDataContactDto</a></code>

## Phone

Methods:

- <code title="get /contact/{customerId}/phone/{phoneNumber}">client.contact.phone.<a href="./src/sent/resources/contact/phone.py">retrieve</a>(phone_number, \*, customer_id) -> <a href="./src/sent/types/shared/sent_dm_services_contracts_data_contact_dto.py">SentDmServicesContractsDataContactDto</a></code>

# Contacts

Types:

```python
from sent.types import ContactListResponse
```

Methods:

- <code title="get /contacts">client.contacts.<a href="./src/sent/resources/contacts.py">list</a>(\*\*<a href="src/sent/types/contact_list_params.py">params</a>) -> <a href="./src/sent/types/contact_list_response.py">object</a></code>

# Messages

Types:

```python
from sent.types import MessageCreateResponse, MessagePhoneNumberResponse
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/sent/resources/messages.py">create</a>(\*\*<a href="src/sent/types/message_create_params.py">params</a>) -> <a href="./src/sent/types/message_create_response.py">object</a></code>
- <code title="post /messages/phone-number">client.messages.<a href="./src/sent/resources/messages.py">phone_number</a>(\*\*<a href="src/sent/types/message_phone_number_params.py">params</a>) -> <a href="./src/sent/types/message_phone_number_response.py">object</a></code>

# SMS

Types:

```python
from sent.types import SentDmServicesContractsDataSMSPayloadDto
```

Methods:

- <code title="get /sms">client.sms.<a href="./src/sent/resources/sms.py">list</a>(\*\*<a href="src/sent/types/sms_list_params.py">params</a>) -> <a href="./src/sent/types/sent_dm_services_contracts_data_sms_payload_dto.py">SentDmServicesContractsDataSMSPayloadDto</a></code>

# Whatsapp

Types:

```python
from sent.types import SentDmServicesContractsDataWhatsappPayloadDto
```

Methods:

- <code title="get /whatsapp">client.whatsapp.<a href="./src/sent/resources/whatsapp.py">list</a>(\*\*<a href="src/sent/types/whatsapp_list_params.py">params</a>) -> <a href="./src/sent/types/sent_dm_services_contracts_data_whatsapp_payload_dto.py">SentDmServicesContractsDataWhatsappPayloadDto</a></code>

# Templates

Types:

```python
from sent.types import (
    SentDmServicesContractsResponsesTemplateResponse,
    TemplateCreateResponse,
    TemplateUpdateResponse,
    TemplateListResponse,
    TemplateDeleteResponse,
)
```

Methods:

- <code title="post /templates">client.templates.<a href="./src/sent/resources/templates.py">create</a>(\*\*<a href="src/sent/types/template_create_params.py">params</a>) -> <a href="./src/sent/types/template_create_response.py">object</a></code>
- <code title="get /templates/{customerId}/{id}">client.templates.<a href="./src/sent/resources/templates.py">retrieve</a>(id, \*, customer_id) -> <a href="./src/sent/types/sent_dm_services_contracts_responses_template_response.py">SentDmServicesContractsResponsesTemplateResponse</a></code>
- <code title="put /templates/{id}">client.templates.<a href="./src/sent/resources/templates.py">update</a>(id, \*\*<a href="src/sent/types/template_update_params.py">params</a>) -> <a href="./src/sent/types/template_update_response.py">object</a></code>
- <code title="get /templates">client.templates.<a href="./src/sent/resources/templates.py">list</a>(\*\*<a href="src/sent/types/template_list_params.py">params</a>) -> <a href="./src/sent/types/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /templates/{customerId}/{id}">client.templates.<a href="./src/sent/resources/templates.py">delete</a>(id, \*, customer_id) -> <a href="./src/sent/types/template_delete_response.py">object</a></code>

# Customers

Types:

```python
from sent.types import SentDmServicesContractsDataCustomerDto, CustomerDeleteResponse
```

Methods:

- <code title="get /customers/{id}">client.customers.<a href="./src/sent/resources/customers.py">retrieve</a>(id) -> <a href="./src/sent/types/sent_dm_services_contracts_data_customer_dto.py">SentDmServicesContractsDataCustomerDto</a></code>
- <code title="put /customers/{id}">client.customers.<a href="./src/sent/resources/customers.py">update</a>(id, \*\*<a href="src/sent/types/customer_update_params.py">params</a>) -> <a href="./src/sent/types/sent_dm_services_contracts_data_customer_dto.py">SentDmServicesContractsDataCustomerDto</a></code>
- <code title="delete /customers/{id}">client.customers.<a href="./src/sent/resources/customers.py">delete</a>(id) -> <a href="./src/sent/types/customer_delete_response.py">object</a></code>
