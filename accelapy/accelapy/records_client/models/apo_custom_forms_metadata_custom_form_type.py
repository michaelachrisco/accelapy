from enum import Enum


class ApoCustomFormsMetadataCustomFormType(str, Enum):
    ADDRESS = "address"
    OWNER = "owner"
    PARCEL = "parcel"

    def __str__(self) -> str:
        return str(self.value)
