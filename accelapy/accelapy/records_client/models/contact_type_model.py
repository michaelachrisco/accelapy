from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactTypeModel")


@_attrs_define
class ContactTypeModel:
    """
    Attributes:
        max_occurance (Union[Unset, int]): The maximum number of times a contact type is used.
        min_occurance (Union[Unset, int]): The minimum number of times a contact type is used.
        value (Union[Unset, str]): The contact type value.
    """

    max_occurance: Union[Unset, int] = UNSET
    min_occurance: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_occurance = self.max_occurance
        min_occurance = self.min_occurance
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_occurance is not UNSET:
            field_dict["maxOccurance"] = max_occurance
        if min_occurance is not UNSET:
            field_dict["minOccurance"] = min_occurance
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_occurance = d.pop("maxOccurance", UNSET)

        min_occurance = d.pop("minOccurance", UNSET)

        value = d.pop("value", UNSET)

        contact_type_model = cls(
            max_occurance=max_occurance,
            min_occurance=min_occurance,
            value=value,
        )

        contact_type_model.additional_properties = d
        return contact_type_model

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
