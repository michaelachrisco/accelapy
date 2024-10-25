from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.row_model_action import RowModelAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_attribute_model import CustomAttributeModel


T = TypeVar("T", bound="RowModel")


@_attrs_define
class RowModel:
    """
    Attributes:
        action (Union[Unset, RowModelAction]): The requested operation on the row.
        fields (Union[Unset, CustomAttributeModel]): Contains a custom form consisting of the custom form id and custom
            field name and value pairs. For example in JSON, "My Custom Field": "My Custom Value". The custom field name and
            its data type are defined in Civic Platform custom forms or custom tables: <br/>**For a Text field**, the
            maximum length is 256.  <br/>**For a Number field**, any numeric form is allowed, including negative numbers.
            <br/>**For a Date field**, the format is MM/dd/yyyy.  <br/>**For a Time field**, the format is hh:mm.
            <br/>**For a TextArea field**, the maximum length is 4000 characters, and allows line return characters.
            <br/>**For a DropdownList field**, the dropdown list values are in the options[] array.  <br/>**For a CheckBox
            field**, the (case-sensitive) valid values are "UNCHECKED" and "CHECKED".  <br/>**For a Radio(Y/N) field**, the
            (case-sensitive) valid values are "Yes" and "No".
        id (Union[Unset, str]): The row id.
    """

    action: Union[Unset, RowModelAction] = UNSET
    fields: Union[Unset, "CustomAttributeModel"] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_attribute_model import CustomAttributeModel

        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, RowModelAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = RowModelAction(_action)

        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, CustomAttributeModel]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = CustomAttributeModel.from_dict(_fields)

        id = d.pop("id", UNSET)

        row_model = cls(
            action=action,
            fields=fields,
            id=id,
        )

        row_model.additional_properties = d
        return row_model

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
