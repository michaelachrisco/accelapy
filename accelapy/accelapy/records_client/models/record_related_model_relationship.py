from enum import Enum


class RecordRelatedModelRelationship(str, Enum):
    CHILD = "child"
    PARENT = "parent"
    RENEWAL = "renewal"

    def __str__(self) -> str:
        return str(self.value)
