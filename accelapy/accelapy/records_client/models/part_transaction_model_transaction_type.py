from enum import Enum


class PartTransactionModelTransactionType(str, Enum):
    ADJUST = "Adjust"
    ISSUE = "Issue"
    RECEIVE = "Receive"
    RESERVE = "Reserve"
    TRANSFER = "Transfer"

    def __str__(self) -> str:
        return str(self.value)
