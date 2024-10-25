from enum import Enum


class InspectionModelScheduleEndAMPM(str, Enum):
    AM = "AM"
    PM = "PM"

    def __str__(self) -> str:
        return str(self.value)
