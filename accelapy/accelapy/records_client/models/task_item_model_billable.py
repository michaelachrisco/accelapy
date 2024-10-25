from enum import Enum


class TaskItemModelBillable(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
