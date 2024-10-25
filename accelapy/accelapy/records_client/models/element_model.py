from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_type_model import ContactTypeModel


T = TypeVar("T", bound="ElementModel")


@_attrs_define
class ElementModel:
    """
    Attributes:
        is_reference (Union[Unset, bool]): Indicates whether or not the entity is a reference.
        is_required (Union[Unset, bool]): Indicates whether or not the entity is required.
        name (Union[Unset, str]): The entity name.
        types (Union[Unset, List['ContactTypeModel']]):
    """

    is_reference: Union[Unset, bool] = UNSET
    is_required: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    types: Union[Unset, List["ContactTypeModel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_reference = self.is_reference
        is_required = self.is_required
        name = self.name
        types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.to_dict()

                types.append(types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_reference is not UNSET:
            field_dict["isReference"] = is_reference
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if name is not UNSET:
            field_dict["name"] = name
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_type_model import ContactTypeModel

        d = src_dict.copy()
        is_reference = d.pop("isReference", UNSET)

        is_required = d.pop("isRequired", UNSET)

        name = d.pop("name", UNSET)

        types = []
        _types = d.pop("types", UNSET)
        for types_item_data in _types or []:
            types_item = ContactTypeModel.from_dict(types_item_data)

            types.append(types_item)

        element_model = cls(
            is_reference=is_reference,
            is_required=is_required,
            name=name,
            types=types,
        )

        element_model.additional_properties = d
        return element_model

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
