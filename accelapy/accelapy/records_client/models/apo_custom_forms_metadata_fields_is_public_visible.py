from enum import Enum


class ApoCustomFormsMetadataFieldsIsPublicVisible(str, Enum):
    N = "N"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)
