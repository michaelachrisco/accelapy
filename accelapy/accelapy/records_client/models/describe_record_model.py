from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.element_model import ElementModel
    from ..models.field_model import FieldModel


T = TypeVar("T", bound="DescribeRecordModel")


@_attrs_define
class DescribeRecordModel:
    """
    Attributes:
        elements (Union[Unset, List['ElementModel']]):
        fields (Union[Unset, List['FieldModel']]):
    """

    elements: Union[Unset, List["ElementModel"]] = UNSET
    fields: Union[Unset, List["FieldModel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()

                elements.append(elements_item)

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elements is not UNSET:
            field_dict["elements"] = elements
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.element_model import ElementModel
        from ..models.field_model import FieldModel

        d = src_dict.copy()
        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in _elements or []:
            elements_item = ElementModel.from_dict(elements_item_data)

            elements.append(elements_item)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = FieldModel.from_dict(fields_item_data)

            fields.append(fields_item)

        describe_record_model = cls(
            elements=elements,
            fields=fields,
        )

        describe_record_model.additional_properties = d
        return describe_record_model

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
