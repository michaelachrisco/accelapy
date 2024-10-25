from enum import Enum


class CustomFormFieldIsReadonly(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
