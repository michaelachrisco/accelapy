from enum import Enum


class RowModelAction(str, Enum):
    ADD = "add"
    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
