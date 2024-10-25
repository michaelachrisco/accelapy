from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.apo_custom_forms_metadata_fields_data_type import ApoCustomFormsMetadataFieldsDataType
from ..models.apo_custom_forms_metadata_fields_is_public_visible import ApoCustomFormsMetadataFieldsIsPublicVisible
from ..models.apo_custom_forms_metadata_fields_is_record_searchable import (
    ApoCustomFormsMetadataFieldsIsRecordSearchable,
)
from ..models.apo_custom_forms_metadata_fields_is_required import ApoCustomFormsMetadataFieldsIsRequired
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apo_custom_forms_metadata_fields_label import ApoCustomFormsMetadataFieldsLabel
    from ..models.apo_custom_forms_metadata_fields_options_item import ApoCustomFormsMetadataFieldsOptionsItem


T = TypeVar("T", bound="ApoCustomFormsMetadataFields")


@_attrs_define
class ApoCustomFormsMetadataFields:
    """Describes the metadata of a custom field.

    Added in Civic Platform version: 9.2.0

        Attributes:
            id (Union[Unset, int]): The unique custom field id.
            name (Union[Unset, str]): The field name.
            description (Union[Unset, str]): Describes the usage or purpose of the custom field.
            label (Union[Unset, ApoCustomFormsMetadataFieldsLabel]): The field label.
            data_type (Union[Unset, ApoCustomFormsMetadataFieldsDataType]): The field data type. If the custom field is a
                DropdownList, the options[] array contains the list of possible values, or the sharedDropdownListName specifies
                the name of a shared dropdown list containing the possible values.
            default_value (Union[Unset, str]): Any default value for the custom field.
            display_order (Union[Unset, int]): The display order of the field on the custom form.
            unit (Union[Unset, str]): The unit of measure of a numeric custom field.
            is_required (Union[Unset, ApoCustomFormsMetadataFieldsIsRequired]): Indicates whether or not the field is
                required.
            is_public_visible (Union[Unset, ApoCustomFormsMetadataFieldsIsPublicVisible]): Indicates whether or not a
                citizen user can see this field.
            is_record_searchable (Union[Unset, ApoCustomFormsMetadataFieldsIsRecordSearchable]): Indicates whether or not
                the field is searchable.
            max_length (Union[Unset, int]): The field maximum length.
            options (Union[Unset, List['ApoCustomFormsMetadataFieldsOptionsItem']]): Contains possible field values, if the
                field is a dropdown field type.
            shared_dropdown_list_name (Union[Unset, str]): The name of the shared dropdown list, if the field is a dropdown
                field type.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    label: Union[Unset, "ApoCustomFormsMetadataFieldsLabel"] = UNSET
    data_type: Union[Unset, ApoCustomFormsMetadataFieldsDataType] = UNSET
    default_value: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    unit: Union[Unset, str] = UNSET
    is_required: Union[Unset, ApoCustomFormsMetadataFieldsIsRequired] = UNSET
    is_public_visible: Union[Unset, ApoCustomFormsMetadataFieldsIsPublicVisible] = UNSET
    is_record_searchable: Union[Unset, ApoCustomFormsMetadataFieldsIsRecordSearchable] = UNSET
    max_length: Union[Unset, int] = UNSET
    options: Union[Unset, List["ApoCustomFormsMetadataFieldsOptionsItem"]] = UNSET
    shared_dropdown_list_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        default_value = self.default_value
        display_order = self.display_order
        unit = self.unit
        is_required: Union[Unset, str] = UNSET
        if not isinstance(self.is_required, Unset):
            is_required = self.is_required.value

        is_public_visible: Union[Unset, str] = UNSET
        if not isinstance(self.is_public_visible, Unset):
            is_public_visible = self.is_public_visible.value

        is_record_searchable: Union[Unset, str] = UNSET
        if not isinstance(self.is_record_searchable, Unset):
            is_record_searchable = self.is_record_searchable.value

        max_length = self.max_length
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        shared_dropdown_list_name = self.shared_dropdown_list_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if unit is not UNSET:
            field_dict["unit"] = unit
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if is_public_visible is not UNSET:
            field_dict["isPublicVisible"] = is_public_visible
        if is_record_searchable is not UNSET:
            field_dict["isRecordSearchable"] = is_record_searchable
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if options is not UNSET:
            field_dict["options"] = options
        if shared_dropdown_list_name is not UNSET:
            field_dict["sharedDropdownListName"] = shared_dropdown_list_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.apo_custom_forms_metadata_fields_label import ApoCustomFormsMetadataFieldsLabel
        from ..models.apo_custom_forms_metadata_fields_options_item import ApoCustomFormsMetadataFieldsOptionsItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _label = d.pop("label", UNSET)
        label: Union[Unset, ApoCustomFormsMetadataFieldsLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = ApoCustomFormsMetadataFieldsLabel.from_dict(_label)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, ApoCustomFormsMetadataFieldsDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = ApoCustomFormsMetadataFieldsDataType(_data_type)

        default_value = d.pop("defaultValue", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        unit = d.pop("unit", UNSET)

        _is_required = d.pop("isRequired", UNSET)
        is_required: Union[Unset, ApoCustomFormsMetadataFieldsIsRequired]
        if isinstance(_is_required, Unset):
            is_required = UNSET
        else:
            is_required = ApoCustomFormsMetadataFieldsIsRequired(_is_required)

        _is_public_visible = d.pop("isPublicVisible", UNSET)
        is_public_visible: Union[Unset, ApoCustomFormsMetadataFieldsIsPublicVisible]
        if isinstance(_is_public_visible, Unset):
            is_public_visible = UNSET
        else:
            is_public_visible = ApoCustomFormsMetadataFieldsIsPublicVisible(_is_public_visible)

        _is_record_searchable = d.pop("isRecordSearchable", UNSET)
        is_record_searchable: Union[Unset, ApoCustomFormsMetadataFieldsIsRecordSearchable]
        if isinstance(_is_record_searchable, Unset):
            is_record_searchable = UNSET
        else:
            is_record_searchable = ApoCustomFormsMetadataFieldsIsRecordSearchable(_is_record_searchable)

        max_length = d.pop("maxLength", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = ApoCustomFormsMetadataFieldsOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        shared_dropdown_list_name = d.pop("sharedDropdownListName", UNSET)

        apo_custom_forms_metadata_fields = cls(
            id=id,
            name=name,
            description=description,
            label=label,
            data_type=data_type,
            default_value=default_value,
            display_order=display_order,
            unit=unit,
            is_required=is_required,
            is_public_visible=is_public_visible,
            is_record_searchable=is_record_searchable,
            max_length=max_length,
            options=options,
            shared_dropdown_list_name=shared_dropdown_list_name,
        )

        apo_custom_forms_metadata_fields.additional_properties = d
        return apo_custom_forms_metadata_fields

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
