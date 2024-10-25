from .authentication_client import Client as AuthenticationClient
from .records_client import Client as RecordsClient
from .records_client.api.records import v4_get_records
from .create_get_headers import CreateGetHeaders
from .payload import Payload

class AccelaClient:
    def __init__(self,
                 payload: Payload,
                 url='https://apis.accela.com/'):
        self.url = url
        self.payload = payload
        self.create_get_headers = CreateGetHeaders(payload.to_payload_str())
        self._authentication_client = AuthenticationClient(base_url = url)
        self._records_client = RecordsClient(base_url=url)
        self.v4_get_records = v4_get_records

    @property
    def authentication_client(self):
        return self._authentication_client.with_headers(self.create_get_headers.get_header())
    
    @property
    def records_client(self):
        return self._records_client.with_headers(self.create_get_headers.get_header())