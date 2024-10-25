from enum import Enum


class ApoCustomFormsMetadataFieldsDataType(str, Enum):
    DATE = "Date"
    DROPDOWNLIST = "DropdownList"
    NUMBER = "Number"
    RADIO = "Radio"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)
