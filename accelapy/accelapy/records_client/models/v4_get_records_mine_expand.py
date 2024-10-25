from enum import Enum


class V4GetRecordsMineExpand(str, Enum):
    ADDRESSES = "addresses"
    CONTACTS = "contacts"
    CUSTOMFORMS = "customForms"
    CUSTOMTABLES = "customTables"
    OWNERS = "owners"
    PARCELS = "parcels"
    PROFESSIONALS = "professionals"

    def __str__(self) -> str:
        return str(self.value)
