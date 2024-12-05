# accelapy
An Accela specific API for https://developer.accela.com/docs/api_reference/api-index.html

## How to use:
`pip install accelapy`

You may need to get your payload from Accela for your environment.

```python
from accelapy.client import AccelaClient
from accelapy.records_client.types import Response
from accelapy.records_client.models import RecordModel, TableModel
import json
from typing import List
from accelapy.payload import Payload

payload = Payload(payload_str='totally-real-payload')
api_client = AccelaClient(payload=payload)

# Get an Accela record, then get its associated custom tables
record_response: Response = api_client.v4_get_records.sync_detailed(client=api_client.authentication_client,
                                                                    custom_id='TM-6308')
json_load = json.loads(record_response.content)
record_models: List[RecordModel] = [RecordModel.from_dict(x) for x in json_load['result']]
print(record_models)

real_record_id = record_models[0].id
record_custom_tables_response: Response = api_client.v_4_get_records_record_id_custom_tables.sync_detailed(
    client=api_client.authentication_client, record_id=real_record_id)
json_load = json.loads(record_custom_tables_response.content)

custom_tables: List[TableModel] = [TableModel.from_dict(x) for x in json_load['result']]
print(custom_tables)
```
