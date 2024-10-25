from enum import Enum


class InspectionTypeModelAllowFailChecklistItems(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
