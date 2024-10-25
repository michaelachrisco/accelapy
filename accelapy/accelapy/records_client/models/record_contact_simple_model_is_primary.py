from enum import Enum


class RecordContactSimpleModelIsPrimary(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
