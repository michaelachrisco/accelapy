import urllib.parse

class Payload:
    def __init__(self, grant_type=None, client_id=None, client_secret=None, username=None, password=None, scope=None, agency_name=None, environment=None, payload_str=None):
        if payload_str:
            # Parse the payload string and set attributes
            self._parse_payload_string(payload_str)
        else:
            # Set attributes directly from parameters
            self.grant_type = grant_type
            self.client_id = client_id
            self.client_secret = client_secret
            self.username = username
            self.password = password
            self.scope = scope
            self.agency_name = agency_name
            self.environment = environment

        # Validate all fields to ensure no None values
        self._validate_fields()

    def _parse_payload_string(self, payload_str):
        # Parse the URL-encoded string into a dictionary
        parsed_data = urllib.parse.parse_qs(payload_str)
        
        # Set each attribute, handling list values from parse_qs
        self.grant_type = parsed_data.get('grant_type', [None])[0]
        self.client_id = parsed_data.get('client_id', [None])[0]
        self.client_secret = parsed_data.get('client_secret', [None])[0]
        self.username = parsed_data.get('username', [None])[0]
        self.password = parsed_data.get('password', [None])[0]
        self.scope = parsed_data.get('scope', [None])[0]
        self.agency_name = parsed_data.get('agency_name', [None])[0]
        self.environment = parsed_data.get('environment', [None])[0]

    def _validate_fields(self):
        # Check if any attribute is None
        missing_fields = [field for field, value in self.__dict__.items() if value is None]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    def to_payload_str(self):
        # Convert the attributes back into a URL-encoded string
        payload_dict = {
            'grant_type': self.grant_type,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password,
            'scope': self.scope,
            'agency_name': self.agency_name,
            'environment': self.environment
        }
        # Return the URL-encoded string
        return urllib.parse.urlencode(payload_dict)

    def __repr__(self):
        # For easy inspection of object attributes
        return (f"Payload(grant_type='{self.grant_type}', client_id='{self.client_id}', "
                f"client_secret='{self.client_secret}', username='{self.username}', "
                f"password='{self.password}', scope='{self.scope}', "
                f"agency_name='{self.agency_name}', environment='{self.environment}')")
