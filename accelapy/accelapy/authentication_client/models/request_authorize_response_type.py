from enum import Enum


class RequestAuthorizeResponseType(str, Enum):
    CODE = "code"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)
