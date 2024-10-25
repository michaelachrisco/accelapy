import json
from datetime import timedelta, datetime

import requests


class Token(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

class CreateGetHeadersToken(Exception):
    pass



class CreateGetHeaders:
    def __init__(self, payload):
        self.payload = payload
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.expires = 0
        self.session_datetime_now = datetime.now()

    def is_time_expired(self):
        # Get the current time
        now = datetime.now()

        # Create a timedelta object representing the given time duration
        time_difference = timedelta(seconds=self.expires)

        # Calculate the future time by adding the time difference to the current time
        future_time = self.session_datetime_now + time_difference
        return now > future_time

    def get_header(self):
        if 'Authorization' not in self.header:
            self.header['Authorization'] = self.create_token_by_scope()

        if self.is_time_expired():
            self.header['Authorization'] = self.create_token_by_scope()

        return self.header

    def create_token_by_scope(self):
        reqUrl = "https://apis.accela.com/oauth2/token"
        # TODO: Break this down into parts instead of throwing all this into one string.
        response = requests.request("POST", reqUrl, data=self.payload, headers=self.header)
        if response.status_code == 200:
            result_dict = response.json()
            self.expires = int(result_dict['expires_in'])
            token = Token(response.text.encode('utf8'))

            self.session_datetime_now = datetime.now()
            return str(token.access_token)
        else:
            raise CreateGetHeadersToken('Cannot find access token, check your payload.')
