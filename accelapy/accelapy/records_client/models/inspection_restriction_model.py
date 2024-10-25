from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_before_scheduled_time import InspectionBeforeScheduledTime


T = TypeVar("T", bound="InspectionRestrictionModel")


@_attrs_define
class InspectionRestrictionModel:
    """
    Attributes:
        before_scheduled_time (Union[Unset, InspectionBeforeScheduledTime]): Specifies the number of days or hours
            before the scheduled time on the inspection date.
    """

    before_scheduled_time: Union[Unset, "InspectionBeforeScheduledTime"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        before_scheduled_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.before_scheduled_time, Unset):
            before_scheduled_time = self.before_scheduled_time.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if before_scheduled_time is not UNSET:
            field_dict["beforeScheduledTime"] = before_scheduled_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inspection_before_scheduled_time import InspectionBeforeScheduledTime

        d = src_dict.copy()
        _before_scheduled_time = d.pop("beforeScheduledTime", UNSET)
        before_scheduled_time: Union[Unset, InspectionBeforeScheduledTime]
        if isinstance(_before_scheduled_time, Unset):
            before_scheduled_time = UNSET
        else:
            before_scheduled_time = InspectionBeforeScheduledTime.from_dict(_before_scheduled_time)

        inspection_restriction_model = cls(
            before_scheduled_time=before_scheduled_time,
        )

        inspection_restriction_model.additional_properties = d
        return inspection_restriction_model

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
