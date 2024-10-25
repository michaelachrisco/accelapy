from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.apo_custom_forms_metadata_custom_form_type import ApoCustomFormsMetadataCustomFormType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apo_custom_forms_metadata_fields import ApoCustomFormsMetadataFields


T = TypeVar("T", bound="ApoCustomFormsMetadata")


@_attrs_define
class ApoCustomFormsMetadata:
    """Contains metadata description of a custom form, including the custom fields metadata.

    Added in Civic Platform version: 9.2.0

        Attributes:
            name (Union[Unset, str]): The name of the custom form
            description (Union[Unset, str]): Describes the usage or puporse of the custom form.
            fields (Union[Unset, List['ApoCustomFormsMetadataFields']]): Contains the field metadata.
            id (Union[Unset, str]): The unique string identifier of the custom form.
            custom_form_type (Union[Unset, ApoCustomFormsMetadataCustomFormType]): Indicates whether the custom form is for
                an address, parcel, or owner.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, List["ApoCustomFormsMetadataFields"]] = UNSET
    id: Union[Unset, str] = UNSET
    custom_form_type: Union[Unset, ApoCustomFormsMetadataCustomFormType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        id = self.id
        custom_form_type: Union[Unset, str] = UNSET
        if not isinstance(self.custom_form_type, Unset):
            custom_form_type = self.custom_form_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if custom_form_type is not UNSET:
            field_dict["customFormType"] = custom_form_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.apo_custom_forms_metadata_fields import ApoCustomFormsMetadataFields

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApoCustomFormsMetadataFields.from_dict(fields_item_data)

            fields.append(fields_item)

        id = d.pop("id", UNSET)

        _custom_form_type = d.pop("customFormType", UNSET)
        custom_form_type: Union[Unset, ApoCustomFormsMetadataCustomFormType]
        if isinstance(_custom_form_type, Unset):
            custom_form_type = UNSET
        else:
            custom_form_type = ApoCustomFormsMetadataCustomFormType(_custom_form_type)

        apo_custom_forms_metadata = cls(
            name=name,
            description=description,
            fields=fields,
            id=id,
            custom_form_type=custom_form_type,
        )

        apo_custom_forms_metadata.additional_properties = d
        return apo_custom_forms_metadata

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
