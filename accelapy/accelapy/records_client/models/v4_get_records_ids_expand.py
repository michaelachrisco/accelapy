from enum import Enum


class V4GetRecordsIdsExpand(str, Enum):
    ADDRESSES = "addresses"
    ASSETS = "assets"
    CONTACTS = "contacts"
    CUSTOMFORMS = "customForms"
    CUSTOMTABLES = "customTables"
    OWNERS = "owners"
    PARCELS = "parcels"
    PROFESSIONALS = "professionals"

    def __str__(self) -> str:
        return str(self.value)
