from enum import Enum


class V4GetRecordsIdsExpandCustomForms(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
