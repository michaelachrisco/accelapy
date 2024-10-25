from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_form_field import CustomFormField


T = TypeVar("T", bound="CustomFormSubgroupModel")


@_attrs_define
class CustomFormSubgroupModel:
    """
    Attributes:
        display_order (Union[Unset, int]): The custom form subgroup display order.
        fields (Union[Unset, List['CustomFormField']]):
        id (Union[Unset, str]): The custom form subgroup system id assigned by the Civic Platform server.
        text (Union[Unset, str]): The custom form subgroup name.
    """

    display_order: Union[Unset, int] = UNSET
    fields: Union[Unset, List["CustomFormField"]] = UNSET
    id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_order = self.display_order
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        id = self.id
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_form_field import CustomFormField

        d = src_dict.copy()
        display_order = d.pop("displayOrder", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = CustomFormField.from_dict(fields_item_data)

            fields.append(fields_item)

        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        custom_form_subgroup_model = cls(
            display_order=display_order,
            fields=fields,
            id=id,
            text=text,
        )

        custom_form_subgroup_model.additional_properties = d
        return custom_form_subgroup_model

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
