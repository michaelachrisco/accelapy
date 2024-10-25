from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordTypeNoAliasModel")


@_attrs_define
class RecordTypeNoAliasModel:
    """
    Attributes:
        category (Union[Unset, str]): The 4th level in a 4-level record type structure (Group-Type-Subtype-Category).
        filter_name (Union[Unset, str]): The name of the record type filter which defines the record types to be
            displayed for the citizen user.
        group (Union[Unset, str]): The 1st level in a 4-level record type structure (Group-Type-Subtype-Category).
        id (Union[Unset, str]): The record type system id assigned by the Civic Platform server.
        module (Union[Unset, str]): Use to filter by the module. See [Get All Modules](./api-
            settings.html#operation/v4.get.settings.modules).
        sub_type (Union[Unset, str]): The 3rd level in a 4-level record type structure (Group-Type-Subtype-Category).
        text (Union[Unset, str]): The record type display text
        type (Union[Unset, str]): The 2nd level in a 4-level record type structure (Group-Type-Subtype-Category).
        value (Union[Unset, str]): The record type value.
    """

    category: Union[Unset, str] = UNSET
    filter_name: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    module: Union[Unset, str] = UNSET
    sub_type: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        filter_name = self.filter_name
        group = self.group
        id = self.id
        module = self.module
        sub_type = self.sub_type
        text = self.text
        type = self.type
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if filter_name is not UNSET:
            field_dict["filterName"] = filter_name
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if module is not UNSET:
            field_dict["module"] = module
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if text is not UNSET:
            field_dict["text"] = text
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        filter_name = d.pop("filterName", UNSET)

        group = d.pop("group", UNSET)

        id = d.pop("id", UNSET)

        module = d.pop("module", UNSET)

        sub_type = d.pop("subType", UNSET)

        text = d.pop("text", UNSET)

        type = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        record_type_no_alias_model = cls(
            category=category,
            filter_name=filter_name,
            group=group,
            id=id,
            module=module,
            sub_type=sub_type,
            text=text,
            type=type,
            value=value,
        )

        record_type_no_alias_model.additional_properties = d
        return record_type_no_alias_model

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
