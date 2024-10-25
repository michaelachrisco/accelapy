from enum import Enum


class CommentModelDisplayOnInspection(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
