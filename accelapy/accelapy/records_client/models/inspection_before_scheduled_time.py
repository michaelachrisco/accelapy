from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InspectionBeforeScheduledTime")


@_attrs_define
class InspectionBeforeScheduledTime:
    """Specifies the number of days or hours before the scheduled time on the inspection date.

    Attributes:
        days (Union[Unset, int]): Inspections can only be cancelled within this number of days before the scheduled time
            on the inspection date.
        hours (Union[Unset, int]): Inspections can only be cancelled within this number of hours before the scheduled
            time on the inspection date.
        time (Union[Unset, str]): Inspections can only be cancelled within the number of specified days or hours before
            this time ("hh:mm AM|PM") on the inspection date.
    """

    days: Union[Unset, int] = UNSET
    hours: Union[Unset, int] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days = self.days
        hours = self.hours
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if hours is not UNSET:
            field_dict["hours"] = hours
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days = d.pop("days", UNSET)

        hours = d.pop("hours", UNSET)

        time = d.pop("time", UNSET)

        inspection_before_scheduled_time = cls(
            days=days,
            hours=hours,
            time=time,
        )

        inspection_before_scheduled_time.additional_properties = d
        return inspection_before_scheduled_time

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
