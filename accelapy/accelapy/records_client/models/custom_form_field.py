from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_form_field_is_readonly import CustomFormFieldIsReadonly
from ..models.custom_form_field_is_required import CustomFormFieldIsRequired
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asi_table_drill import ASITableDrill
    from ..models.custom_form_field_options_item import CustomFormFieldOptionsItem


T = TypeVar("T", bound="CustomFormField")


@_attrs_define
class CustomFormField:
    """
    Attributes:
        display_order (Union[Unset, int]):
        drill_down (Union[Unset, ASITableDrill]):
        field_type (Union[Unset, str]): The custom field data type.
        id (Union[Unset, str]): The custom field system id assigned by the Civic Platform server.
        is_readonly (Union[Unset, CustomFormFieldIsReadonly]): Indicates whether or not the custom field is read-only.
        is_required (Union[Unset, CustomFormFieldIsRequired]): Indicates whether or not the custom field is required.
        max_length (Union[Unset, int]): The custom field length
        options (Union[Unset, List['CustomFormFieldOptionsItem']]):
        text (Union[Unset, str]): The custom field localized text.
        value (Union[Unset, str]): The custom field stored value.
    """

    display_order: Union[Unset, int] = UNSET
    drill_down: Union[Unset, "ASITableDrill"] = UNSET
    field_type: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_readonly: Union[Unset, CustomFormFieldIsReadonly] = UNSET
    is_required: Union[Unset, CustomFormFieldIsRequired] = UNSET
    max_length: Union[Unset, int] = UNSET
    options: Union[Unset, List["CustomFormFieldOptionsItem"]] = UNSET
    text: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_order = self.display_order
        drill_down: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.drill_down, Unset):
            drill_down = self.drill_down.to_dict()

        field_type = self.field_type
        id = self.id
        is_readonly: Union[Unset, str] = UNSET
        if not isinstance(self.is_readonly, Unset):
            is_readonly = self.is_readonly.value

        is_required: Union[Unset, str] = UNSET
        if not isinstance(self.is_required, Unset):
            is_required = self.is_required.value

        max_length = self.max_length
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        text = self.text
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if drill_down is not UNSET:
            field_dict["drillDown"] = drill_down
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if id is not UNSET:
            field_dict["id"] = id
        if is_readonly is not UNSET:
            field_dict["isReadonly"] = is_readonly
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if options is not UNSET:
            field_dict["options"] = options
        if text is not UNSET:
            field_dict["text"] = text
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asi_table_drill import ASITableDrill
        from ..models.custom_form_field_options_item import CustomFormFieldOptionsItem

        d = src_dict.copy()
        display_order = d.pop("displayOrder", UNSET)

        _drill_down = d.pop("drillDown", UNSET)
        drill_down: Union[Unset, ASITableDrill]
        if isinstance(_drill_down, Unset):
            drill_down = UNSET
        else:
            drill_down = ASITableDrill.from_dict(_drill_down)

        field_type = d.pop("fieldType", UNSET)

        id = d.pop("id", UNSET)

        _is_readonly = d.pop("isReadonly", UNSET)
        is_readonly: Union[Unset, CustomFormFieldIsReadonly]
        if isinstance(_is_readonly, Unset):
            is_readonly = UNSET
        else:
            is_readonly = CustomFormFieldIsReadonly(_is_readonly)

        _is_required = d.pop("isRequired", UNSET)
        is_required: Union[Unset, CustomFormFieldIsRequired]
        if isinstance(_is_required, Unset):
            is_required = UNSET
        else:
            is_required = CustomFormFieldIsRequired(_is_required)

        max_length = d.pop("maxLength", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = CustomFormFieldOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        text = d.pop("text", UNSET)

        value = d.pop("value", UNSET)

        custom_form_field = cls(
            display_order=display_order,
            drill_down=drill_down,
            field_type=field_type,
            id=id,
            is_readonly=is_readonly,
            is_required=is_required,
            max_length=max_length,
            options=options,
            text=text,
            value=value,
        )

        custom_form_field.additional_properties = d
        return custom_form_field

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
