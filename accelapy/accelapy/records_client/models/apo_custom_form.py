from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApoCustomForm")


@_attrs_define
class ApoCustomForm:
    """A set of custom field name-value pairs on a custom form.

    Added in Civic Platform version: 9.2.0

        Attributes:
            id (Union[Unset, str]): The unique string id of the custom form template for the custom data.
            a_custom_field_name (Union[Unset, str]): A custom field name. Note that this is the custom attribute name (not
                the attribute label). To get the attribute display label, use [Get Record Address Custom Forms
                Metadata](#operation/v4.get.records.recordId.addresses.addressId.customForms.meta).
            a_custom_field_value (Union[Unset, str]): A custom field value
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
            field_dict["aCustomFieldName"] = a_custom_field_name
        if a_custom_field_value is not UNSET:
            field_dict["aCustomFieldValue"] = a_custom_field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        a_custom_field_name = d.pop("aCustomFieldName", UNSET)

        a_custom_field_value = d.pop("aCustomFieldValue", UNSET)

        apo_custom_form = cls(
            id=id,
            a_custom_field_name=a_custom_field_name,
            a_custom_field_value=a_custom_field_value,
        )

        apo_custom_form.additional_properties = d
        return apo_custom_form

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
