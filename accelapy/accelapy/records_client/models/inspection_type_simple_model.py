from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InspectionTypeSimpleModel")


@_attrs_define
class InspectionTypeSimpleModel:
    """
    Attributes:
        group (Union[Unset, str]):
        id (Union[Unset, int]):
        ivr_number (Union[Unset, int]): The IVR (Interactive Voice Response) number assigned to the inspection type.

            Added in Civic Platform 9.3.0
        text (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    group: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    ivr_number: Union[Unset, int] = UNSET
    text: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group = self.group
        id = self.id
        ivr_number = self.ivr_number
        text = self.text
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if ivr_number is not UNSET:
            field_dict["ivrNumber"] = ivr_number
        if text is not UNSET:
            field_dict["text"] = text
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group = d.pop("group", UNSET)

        id = d.pop("id", UNSET)

        ivr_number = d.pop("ivrNumber", UNSET)

        text = d.pop("text", UNSET)

        value = d.pop("value", UNSET)

        inspection_type_simple_model = cls(
            group=group,
            id=id,
            ivr_number=ivr_number,
            text=text,
            value=value,
        )

        inspection_type_simple_model.additional_properties = d
        return inspection_type_simple_model

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
