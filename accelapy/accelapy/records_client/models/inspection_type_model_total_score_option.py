from enum import Enum


class InspectionTypeModelTotalScoreOption(str, Enum):
    AVG = "AVG"
    MAX = "MAX"
    MIN = "MIN"
    SUBTRACT = "SUBTRACT"
    TOTAL = "TOTAL"

    def __str__(self) -> str:
        return str(self.value)
