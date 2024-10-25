from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentModel")


@_attrs_define
class DepartmentModel:
    """
    Attributes:
        agency (Union[Unset, str]): The department agency
        bureau (Union[Unset, str]): The name of the bureau, which is an organization level within an agency.
        division (Union[Unset, str]): The name of the division, which is an organization level within a bureau.
        group (Union[Unset, str]): The department group.
        id (Union[Unset, str]): The department system id assigned by the Civic Platform server.
        office (Union[Unset, str]): An organization level within a group. An office is the final level within an
            organization structure. Agency->Bureau->Division->Section->Group->Office.
        section (Union[Unset, str]): A piece of a township measuring 640 acres, one square mile, numbered with reference
            to the base line and meridian line.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        text (Union[Unset, str]): The localized display text.
        value (Union[Unset, str]): The value for the specified parameter.
    """

    agency: Union[Unset, str] = UNSET
    bureau: Union[Unset, str] = UNSET
    division: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    office: Union[Unset, str] = UNSET
    section: Union[Unset, str] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agency = self.agency
        bureau = self.bureau
        division = self.division
        group = self.group
        id = self.id
        office = self.office
        section = self.section
        service_provider_code = self.service_provider_code
        text = self.text
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agency is not UNSET:
            field_dict["agency"] = agency
        if bureau is not UNSET:
            field_dict["bureau"] = bureau
        if division is not UNSET:
            field_dict["division"] = division
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if office is not UNSET:
            field_dict["office"] = office
        if section is not UNSET:
            field_dict["section"] = section
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if text is not UNSET:
            field_dict["text"] = text
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agency = d.pop("agency", UNSET)

        bureau = d.pop("bureau", UNSET)

        division = d.pop("division", UNSET)

        group = d.pop("group", UNSET)

        id = d.pop("id", UNSET)

        office = d.pop("office", UNSET)

        section = d.pop("section", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        text = d.pop("text", UNSET)

        value = d.pop("value", UNSET)

        department_model = cls(
            agency=agency,
            bureau=bureau,
            division=division,
            group=group,
            id=id,
            office=office,
            section=section,
            service_provider_code=service_provider_code,
            text=text,
            value=value,
        )

        department_model.additional_properties = d
        return department_model

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
