from enum import Enum


class InspectionTypeModelIsRequired(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
