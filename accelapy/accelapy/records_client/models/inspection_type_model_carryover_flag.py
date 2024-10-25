from enum import Enum


class InspectionTypeModelCarryoverFlag(str, Enum):
    A = "A"

    def __str__(self) -> str:
        return str(self.value)
