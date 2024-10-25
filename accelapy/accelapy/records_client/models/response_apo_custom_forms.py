from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apo_custom_form import ApoCustomForm


T = TypeVar("T", bound="ResponseApoCustomForms")


@_attrs_define
class ResponseApoCustomForms:
    """APO custom forms response.

    Added in Civic Platform version: 9.2.0

        Attributes:
            apo_custom_forms (Union[Unset, List['ApoCustomForm']]):
            status (Union[Unset, int]): The return status code.
    """

    apo_custom_forms: Union[Unset, List["ApoCustomForm"]] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        apo_custom_forms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.apo_custom_forms, Unset):
            apo_custom_forms = []
            for apo_custom_forms_item_data in self.apo_custom_forms:
                apo_custom_forms_item = apo_custom_forms_item_data.to_dict()

                apo_custom_forms.append(apo_custom_forms_item)

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apo_custom_forms is not UNSET:
            field_dict["apo_customForms"] = apo_custom_forms
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.apo_custom_form import ApoCustomForm

        d = src_dict.copy()
        apo_custom_forms = []
        _apo_custom_forms = d.pop("apo_customForms", UNSET)
        for apo_custom_forms_item_data in _apo_custom_forms or []:
            apo_custom_forms_item = ApoCustomForm.from_dict(apo_custom_forms_item_data)

            apo_custom_forms.append(apo_custom_forms_item)

        status = d.pop("status", UNSET)

        response_apo_custom_forms = cls(
            apo_custom_forms=apo_custom_forms,
            status=status,
        )

        response_apo_custom_forms.additional_properties = d
        return response_apo_custom_forms

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
