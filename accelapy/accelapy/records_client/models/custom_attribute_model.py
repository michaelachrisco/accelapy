from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomAttributeModel")


@_attrs_define
class CustomAttributeModel:
    """Contains a custom form consisting of the custom form id and custom field name and value pairs. For example in JSON,
    "My Custom Field": "My Custom Value". The custom field name and its data type are defined in Civic Platform custom
    forms or custom tables: <br/>**For a Text field**, the maximum length is 256.  <br/>**For a Number field**, any
    numeric form is allowed, including negative numbers.  <br/>**For a Date field**, the format is MM/dd/yyyy.
    <br/>**For a Time field**, the format is hh:mm.  <br/>**For a TextArea field**, the maximum length is 4000
    characters, and allows line return characters.  <br/>**For a DropdownList field**, the dropdown list values are in
    the options[] array.  <br/>**For a CheckBox field**, the (case-sensitive) valid values are "UNCHECKED" and
    "CHECKED".  <br/>**For a Radio(Y/N) field**, the (case-sensitive) valid values are "Yes" and "No".

        Attributes:
            id (Union[Unset, str]): The custom form id.
            a_custom_field_name (Union[Unset, str]): The name of a custom field.
            a_custom_field_value (Union[Unset, str]): The value of a custom field.
    """

    id: Union[Unset, str] = UNSET
    a_custom_field_name: Union[Unset, str] = UNSET
    a_custom_field_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        a_custom_field_name = self.a_custom_field_name
        a_custom_field_value = self.a_custom_field_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if a_custom_field_name is not UNSET:
            field_dict["<aCustomFieldName>"] = a_custom_field_name
        if a_custom_field_value is not UNSET:
            field_dict["<aCustomFieldValue>"] = a_custom_field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        a_custom_field_name = d.pop("<aCustomFieldName>", UNSET)

        a_custom_field_value = d.pop("<aCustomFieldValue>", UNSET)

        custom_attribute_model = cls(
            id=id,
            a_custom_field_name=a_custom_field_name,
            a_custom_field_value=a_custom_field_value,
        )

        custom_attribute_model.additional_properties = d
        return custom_attribute_model

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
