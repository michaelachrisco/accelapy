from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRolePrivilegeModel")


@_attrs_define
class UserRolePrivilegeModel:
    """
    Attributes:
        contact_allowed (Union[Unset, bool]): Indicates whether or not the permission is given to a contact.
        delete_allowed (Union[Unset, bool]): Indicates whether or not the permission to delete a document is allowed.
        download_allowed (Union[Unset, bool]): Indicates whether or not the permission to download a document is
            allowed.
        license_type_rules (Union[Unset, List[str]]):
        licensend_professional_allowed (Union[Unset, bool]): Indicates whether or not the permission is given to a
            licensed professional.
        owner_allowed (Union[Unset, bool]): Indicates whether or not the permission is given to an owner.
        record_creator_allowed (Union[Unset, bool]): Indicates whether or not the permission is given to a record
            creator.
        registered_user_allowed (Union[Unset, bool]): Indicates whether or not the permission is given to a registered
            public user.
        title_view_allowed (Union[Unset, bool]): Indicates whether or not the permission to view a document name is
            allowed.
        upload_allowed (Union[Unset, bool]): Indicates whether or not the permission to upload a document is allowed.
    """

    contact_allowed: Union[Unset, bool] = UNSET
    delete_allowed: Union[Unset, bool] = UNSET
    download_allowed: Union[Unset, bool] = UNSET
    license_type_rules: Union[Unset, List[str]] = UNSET
    licensend_professional_allowed: Union[Unset, bool] = UNSET
    owner_allowed: Union[Unset, bool] = UNSET
    record_creator_allowed: Union[Unset, bool] = UNSET
    registered_user_allowed: Union[Unset, bool] = UNSET
    title_view_allowed: Union[Unset, bool] = UNSET
    upload_allowed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_allowed = self.contact_allowed
        delete_allowed = self.delete_allowed
        download_allowed = self.download_allowed
        license_type_rules: Union[Unset, List[str]] = UNSET
        if not isinstance(self.license_type_rules, Unset):
            license_type_rules = self.license_type_rules

        licensend_professional_allowed = self.licensend_professional_allowed
        owner_allowed = self.owner_allowed
        record_creator_allowed = self.record_creator_allowed
        registered_user_allowed = self.registered_user_allowed
        title_view_allowed = self.title_view_allowed
        upload_allowed = self.upload_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_allowed is not UNSET:
            field_dict["contactAllowed"] = contact_allowed
        if delete_allowed is not UNSET:
            field_dict["deleteAllowed"] = delete_allowed
        if download_allowed is not UNSET:
            field_dict["downloadAllowed"] = download_allowed
        if license_type_rules is not UNSET:
            field_dict["licenseTypeRules"] = license_type_rules
        if licensend_professional_allowed is not UNSET:
            field_dict["licensendProfessionalAllowed"] = licensend_professional_allowed
        if owner_allowed is not UNSET:
            field_dict["ownerAllowed"] = owner_allowed
        if record_creator_allowed is not UNSET:
            field_dict["recordCreatorAllowed"] = record_creator_allowed
        if registered_user_allowed is not UNSET:
            field_dict["registeredUserAllowed"] = registered_user_allowed
        if title_view_allowed is not UNSET:
            field_dict["titleViewAllowed"] = title_view_allowed
        if upload_allowed is not UNSET:
            field_dict["uploadAllowed"] = upload_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact_allowed = d.pop("contactAllowed", UNSET)

        delete_allowed = d.pop("deleteAllowed", UNSET)

        download_allowed = d.pop("downloadAllowed", UNSET)

        license_type_rules = cast(List[str], d.pop("licenseTypeRules", UNSET))

        licensend_professional_allowed = d.pop("licensendProfessionalAllowed", UNSET)

        owner_allowed = d.pop("ownerAllowed", UNSET)

        record_creator_allowed = d.pop("recordCreatorAllowed", UNSET)

        registered_user_allowed = d.pop("registeredUserAllowed", UNSET)

        title_view_allowed = d.pop("titleViewAllowed", UNSET)

        upload_allowed = d.pop("uploadAllowed", UNSET)

        user_role_privilege_model = cls(
            contact_allowed=contact_allowed,
            delete_allowed=delete_allowed,
            download_allowed=download_allowed,
            license_type_rules=license_type_rules,
            licensend_professional_allowed=licensend_professional_allowed,
            owner_allowed=owner_allowed,
            record_creator_allowed=record_creator_allowed,
            registered_user_allowed=registered_user_allowed,
            title_view_allowed=title_view_allowed,
            upload_allowed=upload_allowed,
        )

        user_role_privilege_model.additional_properties = d
        return user_role_privilege_model

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
