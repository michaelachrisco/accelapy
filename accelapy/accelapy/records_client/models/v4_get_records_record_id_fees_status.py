from enum import Enum


class V4GetRecordsRecordIdFeesStatus(str, Enum):
    PAID = "paid"
    UNPAID = "unpaid"

    def __str__(self) -> str:
        return str(self.value)
