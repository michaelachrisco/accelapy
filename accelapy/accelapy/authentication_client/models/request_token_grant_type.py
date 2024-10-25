from enum import Enum


class RequestTokenGrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    PASSWORD = "password"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
