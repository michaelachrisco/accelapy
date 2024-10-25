from enum import Enum


class V4GetRecordsRecordIdRelatedRelationship(str, Enum):
    CHILD = "child"
    PARENT = "parent"
    RENEWAL = "renewal"

    def __str__(self) -> str:
        return str(self.value)
