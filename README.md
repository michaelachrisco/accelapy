# accelapy
An Accela specific API client for Accela V4 API https://developer.accela.com/docs/api_reference/api-index.html

# Install
`pip install accelapy`

## How to use:

You may need to get your payload from Accela for your environment. See: [Password Credential Login](https://developer.accela.com/docs/construct-passwordCredentialLogin.html) for more information.
This library is used for syncing to and from Accela. It contains validation, better error statements, and pythonic models for the API in Accela.


### Authentication
```python
from accelapy.client import AccelaClient
from accelapy.records_client.types import Response
from accelapy.records_client.models import RecordModel, TableModel
import json
from typing import List
from accelapy.payload import Payload

payload = Payload(payload_str='totally-real-payload')

# OR optionally generate payload from arguments
# You will likely need to talk to Accela. Please give accela support an email/call to get this. 
payload = Payload(payload = Payload(scope='records', grant_type='password', client_id='totallyrealclientid', client_secret='totallyrealsecret', username='USER', password='pass', agency_name='AGENCYNAME', environment='NONPROD1')

api_client = AccelaClient(payload=payload)

```
### Get a record:
```python

# Get an Accela record, then get its associated custom tables
record_response: Response[RecordModel] = api_client.v4_get_records.sync_detailed(client=api_client.authentication_client,
                                                                    custom_id='TM-6308')

json_load = json.loads(record_response.content)
record_models: List[RecordModel] = [RecordModel.from_dict(x) for x in json_load['result']]
print(record_models)
```

### Get a records custom table:
``` python
real_record_id = record_models[0].id
record_custom_tables_response: Response = api_client.v_4_get_records_record_id_custom_tables.sync_detailed(
    client=api_client.authentication_client, record_id=real_record_id)
json_load = json.loads(record_custom_tables_response.content)

custom_tables: List[TableModel] = [TableModel.from_dict(x) for x in json_load['result']]
print(custom_tables)
```

## Documentation
* Accela API Auth docs: https://developer.accela.com/docs/api_reference/api-auth.html
* Accela API Records docs: https://developer.accela.com/docs/api_reference/api-records.html
* TODO: Many more from [this list](https://developer.accela.com/docs/api_reference/api-index.html)
