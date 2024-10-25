from enum import Enum


class RequestRecordModelCreatedByCloning(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
