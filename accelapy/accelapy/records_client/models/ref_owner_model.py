from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.owner_address_model import OwnerAddressModel
    from ..models.record_id_model import RecordIdModel
    from ..models.ref_owner_model_status import RefOwnerModelStatus


T = TypeVar("T", bound="RefOwnerModel")


@_attrs_define
class RefOwnerModel:
    """
    Attributes:
        email (Union[Unset, str]): The contact's email address.
        fax (Union[Unset, str]): The fax number for the contact.
        first_name (Union[Unset, str]): The contact's first name. This field is only active when the Contact Type
            selected is Individual.
        full_name (Union[Unset, str]): The contact's full name. This field is only active when the Contact Type selected
            is Individual.
        id (Union[Unset, int]): The owner system id assigned by the Civic Platform server.
        is_primary (Union[Unset, str]): Indicates whether or not to designate the owner as the primary owner.
        last_name (Union[Unset, str]): The last name (surname).
        mail_address (Union[Unset, OwnerAddressModel]):
        middle_name (Union[Unset, str]): The contact's middle name.
        parcel_id (Union[Unset, str]): The unique Id generated for a parcel.
        phone (Union[Unset, str]): The telephone number of the owner.
        phone_country_code (Union[Unset, str]): The country code for the assoicated phone number.
        record_id (Union[Unset, RecordIdModel]):
        ref_owner_id (Union[Unset, float]): The reference owner id.
        status (Union[Unset, RefOwnerModelStatus]): The owner status.
        tax_id (Union[Unset, str]): The owner's tax ID number.
        title (Union[Unset, str]): The individual's business title.
        type (Union[Unset, str]): The owner type.
    """

    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_primary: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    mail_address: Union[Unset, "OwnerAddressModel"] = UNSET
    middle_name: Union[Unset, str] = UNSET
    parcel_id: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_country_code: Union[Unset, str] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    ref_owner_id: Union[Unset, float] = UNSET
    status: Union[Unset, "RefOwnerModelStatus"] = UNSET
    tax_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        fax = self.fax
        first_name = self.first_name
        full_name = self.full_name
        id = self.id
        is_primary = self.is_primary
        last_name = self.last_name
        mail_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mail_address, Unset):
            mail_address = self.mail_address.to_dict()

        middle_name = self.middle_name
        parcel_id = self.parcel_id
        phone = self.phone
        phone_country_code = self.phone_country_code
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        ref_owner_id = self.ref_owner_id
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        tax_id = self.tax_id
        title = self.title
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if mail_address is not UNSET:
            field_dict["mailAddress"] = mail_address
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if parcel_id is not UNSET:
            field_dict["parcelId"] = parcel_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_country_code is not UNSET:
            field_dict["phoneCountryCode"] = phone_country_code
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if ref_owner_id is not UNSET:
            field_dict["refOwnerId"] = ref_owner_id
        if status is not UNSET:
            field_dict["status"] = status
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.owner_address_model import OwnerAddressModel
        from ..models.record_id_model import RecordIdModel
        from ..models.ref_owner_model_status import RefOwnerModelStatus

        d = src_dict.copy()
        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        first_name = d.pop("firstName", UNSET)

        full_name = d.pop("fullName", UNSET)

        id = d.pop("id", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        last_name = d.pop("lastName", UNSET)

        _mail_address = d.pop("mailAddress", UNSET)
        mail_address: Union[Unset, OwnerAddressModel]
        if isinstance(_mail_address, Unset):
            mail_address = UNSET
        else:
            mail_address = OwnerAddressModel.from_dict(_mail_address)

        middle_name = d.pop("middleName", UNSET)

        parcel_id = d.pop("parcelId", UNSET)

        phone = d.pop("phone", UNSET)

        phone_country_code = d.pop("phoneCountryCode", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        ref_owner_id = d.pop("refOwnerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RefOwnerModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RefOwnerModelStatus.from_dict(_status)

        tax_id = d.pop("taxId", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        ref_owner_model = cls(
            email=email,
            fax=fax,
            first_name=first_name,
            full_name=full_name,
            id=id,
            is_primary=is_primary,
            last_name=last_name,
            mail_address=mail_address,
            middle_name=middle_name,
            parcel_id=parcel_id,
            phone=phone,
            phone_country_code=phone_country_code,
            record_id=record_id,
            ref_owner_id=ref_owner_id,
            status=status,
            tax_id=tax_id,
            title=title,
            type=type,
        )

        ref_owner_model.additional_properties = d
        return ref_owner_model

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
