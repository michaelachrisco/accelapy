import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_professional_model_country import LicenseProfessionalModelCountry
    from ..models.license_professional_model_gender import LicenseProfessionalModelGender
    from ..models.license_professional_model_license_type import LicenseProfessionalModelLicenseType
    from ..models.license_professional_model_licensing_board import LicenseProfessionalModelLicensingBoard
    from ..models.license_professional_model_salutation import LicenseProfessionalModelSalutation
    from ..models.license_professional_model_state import LicenseProfessionalModelState
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="LicenseProfessionalModel")


@_attrs_define
class LicenseProfessionalModel:
    """
    Attributes:
        address_line_1 (Union[Unset, str]): The first line of the address.
        address_line_2 (Union[Unset, str]): The second line of the address.
        address_line_3 (Union[Unset, str]): The third line of the address.
        birth_date (Union[Unset, datetime.datetime]): The birth date of an individual.
        business_license (Union[Unset, str]): The official business license number issued by an agency. A licensed
            professional can have the same license number assigned to multiple license types.
        business_name (Union[Unset, str]): A business name for the applicable individual.
        business_name_2 (Union[Unset, str]): A secondary business name for the applicable individual.
        city (Union[Unset, str]): The name of the city.
        comment (Union[Unset, str]): Comments or notes about the current context.
        country (Union[Unset, LicenseProfessionalModelCountry]): The name of the country.
        email (Union[Unset, str]): The contact's email address.
        expiration_date (Union[Unset, datetime.datetime]): The license expiration date.
        fax (Union[Unset, str]): The fax number for the contact.
        federal_employer_id (Union[Unset, str]): The Federal Employer Identification Number. It is used to identify a
            business for tax purposes.
        first_name (Union[Unset, str]): The licensed professional's first name.
        full_name (Union[Unset, str]): The licensed professional's full name.
        gender (Union[Unset, LicenseProfessionalModelGender]): The gender (male or female) of the individual.
        id (Union[Unset, str]): The licensed professional system id assigned by the Civic Platform server.
        is_primary (Union[Unset, str]): Indicates whether or not to designate the professional as the primary
            professional.
        last_name (Union[Unset, str]): The licensed professional's last name.
        last_renewal_date (Union[Unset, datetime.datetime]): The last date for a professionals renewal license.
        license_number (Union[Unset, str]): The licensed professional's license number.
        license_type (Union[Unset, LicenseProfessionalModelLicenseType]): The type of license held by the professional.
        licensing_board (Union[Unset, LicenseProfessionalModelLicensingBoard]): The name of the licensing board that
            issued the license.
        middle_name (Union[Unset, str]): The licensed professional's middle name.
        original_issue_date (Union[Unset, datetime.datetime]): The original issuance date of license.
        phone1 (Union[Unset, str]): The primary phone number of the contact.
        phone2 (Union[Unset, str]): The secondary phone number of the contact.
        phone3 (Union[Unset, str]): The tertiary phone number for the contact.
        post_office_box (Union[Unset, str]): The post office box number.
        postal_code (Union[Unset, str]): The postal ZIP code for the address.
        record_id (Union[Unset, RecordIdModel]):
        reference_license_id (Union[Unset, str]): The unique Id generated for a professional stored in the system.
        salutation (Union[Unset, LicenseProfessionalModelSalutation]): The salutation to be used when addressing the
            contact; for example Mr. or Ms. This field is active only when Contact Type = Individual.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        state (Union[Unset, LicenseProfessionalModelState]): The state corresponding to the address on record.
        suffix (Union[Unset, str]): The licensed professional's name suffix.
        title (Union[Unset, str]): The individual's professional title.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    birth_date: Union[Unset, datetime.datetime] = UNSET
    business_license: Union[Unset, str] = UNSET
    business_name: Union[Unset, str] = UNSET
    business_name_2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    country: Union[Unset, "LicenseProfessionalModelCountry"] = UNSET
    email: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    fax: Union[Unset, str] = UNSET
    federal_employer_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    gender: Union[Unset, "LicenseProfessionalModelGender"] = UNSET
    id: Union[Unset, str] = UNSET
    is_primary: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    last_renewal_date: Union[Unset, datetime.datetime] = UNSET
    license_number: Union[Unset, str] = UNSET
    license_type: Union[Unset, "LicenseProfessionalModelLicenseType"] = UNSET
    licensing_board: Union[Unset, "LicenseProfessionalModelLicensingBoard"] = UNSET
    middle_name: Union[Unset, str] = UNSET
    original_issue_date: Union[Unset, datetime.datetime] = UNSET
    phone1: Union[Unset, str] = UNSET
    phone2: Union[Unset, str] = UNSET
    phone3: Union[Unset, str] = UNSET
    post_office_box: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    reference_license_id: Union[Unset, str] = UNSET
    salutation: Union[Unset, "LicenseProfessionalModelSalutation"] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    state: Union[Unset, "LicenseProfessionalModelState"] = UNSET
    suffix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line_1 = self.address_line_1
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        birth_date: Union[Unset, str] = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        business_license = self.business_license
        business_name = self.business_name
        business_name_2 = self.business_name_2
        city = self.city
        comment = self.comment
        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        email = self.email
        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        fax = self.fax
        federal_employer_id = self.federal_employer_id
        first_name = self.first_name
        full_name = self.full_name
        gender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        id = self.id
        is_primary = self.is_primary
        last_name = self.last_name
        last_renewal_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_renewal_date, Unset):
            last_renewal_date = self.last_renewal_date.isoformat()

        license_number = self.license_number
        license_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_type, Unset):
            license_type = self.license_type.to_dict()

        licensing_board: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.licensing_board, Unset):
            licensing_board = self.licensing_board.to_dict()

        middle_name = self.middle_name
        original_issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.original_issue_date, Unset):
            original_issue_date = self.original_issue_date.isoformat()

        phone1 = self.phone1
        phone2 = self.phone2
        phone3 = self.phone3
        post_office_box = self.post_office_box
        postal_code = self.postal_code
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        reference_license_id = self.reference_license_id
        salutation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.to_dict()

        service_provider_code = self.service_provider_code
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        suffix = self.suffix
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if business_license is not UNSET:
            field_dict["businessLicense"] = business_license
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if business_name_2 is not UNSET:
            field_dict["businessName2"] = business_name_2
        if city is not UNSET:
            field_dict["city"] = city
        if comment is not UNSET:
            field_dict["comment"] = comment
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if fax is not UNSET:
            field_dict["fax"] = fax
        if federal_employer_id is not UNSET:
            field_dict["federalEmployerId"] = federal_employer_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if id is not UNSET:
            field_dict["id"] = id
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if last_renewal_date is not UNSET:
            field_dict["lastRenewalDate"] = last_renewal_date
        if license_number is not UNSET:
            field_dict["licenseNumber"] = license_number
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if licensing_board is not UNSET:
            field_dict["licensingBoard"] = licensing_board
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if original_issue_date is not UNSET:
            field_dict["originalIssueDate"] = original_issue_date
        if phone1 is not UNSET:
            field_dict["phone1"] = phone1
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if post_office_box is not UNSET:
            field_dict["postOfficeBox"] = post_office_box
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if reference_license_id is not UNSET:
            field_dict["referenceLicenseId"] = reference_license_id
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if state is not UNSET:
            field_dict["state"] = state
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.license_professional_model_country import LicenseProfessionalModelCountry
        from ..models.license_professional_model_gender import LicenseProfessionalModelGender
        from ..models.license_professional_model_license_type import LicenseProfessionalModelLicenseType
        from ..models.license_professional_model_licensing_board import LicenseProfessionalModelLicensingBoard
        from ..models.license_professional_model_salutation import LicenseProfessionalModelSalutation
        from ..models.license_professional_model_state import LicenseProfessionalModelState
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        _birth_date = d.pop("birthDate", UNSET)
        birth_date: Union[Unset, datetime.datetime]
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date)

        business_license = d.pop("businessLicense", UNSET)

        business_name = d.pop("businessName", UNSET)

        business_name_2 = d.pop("businessName2", UNSET)

        city = d.pop("city", UNSET)

        comment = d.pop("comment", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, LicenseProfessionalModelCountry]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = LicenseProfessionalModelCountry.from_dict(_country)

        email = d.pop("email", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        fax = d.pop("fax", UNSET)

        federal_employer_id = d.pop("federalEmployerId", UNSET)

        first_name = d.pop("firstName", UNSET)

        full_name = d.pop("fullName", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, LicenseProfessionalModelGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = LicenseProfessionalModelGender.from_dict(_gender)

        id = d.pop("id", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        last_name = d.pop("lastName", UNSET)

        _last_renewal_date = d.pop("lastRenewalDate", UNSET)
        last_renewal_date: Union[Unset, datetime.datetime]
        if isinstance(_last_renewal_date, Unset):
            last_renewal_date = UNSET
        else:
            last_renewal_date = isoparse(_last_renewal_date)

        license_number = d.pop("licenseNumber", UNSET)

        _license_type = d.pop("licenseType", UNSET)
        license_type: Union[Unset, LicenseProfessionalModelLicenseType]
        if isinstance(_license_type, Unset):
            license_type = UNSET
        else:
            license_type = LicenseProfessionalModelLicenseType.from_dict(_license_type)

        _licensing_board = d.pop("licensingBoard", UNSET)
        licensing_board: Union[Unset, LicenseProfessionalModelLicensingBoard]
        if isinstance(_licensing_board, Unset):
            licensing_board = UNSET
        else:
            licensing_board = LicenseProfessionalModelLicensingBoard.from_dict(_licensing_board)

        middle_name = d.pop("middleName", UNSET)

        _original_issue_date = d.pop("originalIssueDate", UNSET)
        original_issue_date: Union[Unset, datetime.datetime]
        if isinstance(_original_issue_date, Unset):
            original_issue_date = UNSET
        else:
            original_issue_date = isoparse(_original_issue_date)

        phone1 = d.pop("phone1", UNSET)

        phone2 = d.pop("phone2", UNSET)

        phone3 = d.pop("phone3", UNSET)

        post_office_box = d.pop("postOfficeBox", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        reference_license_id = d.pop("referenceLicenseId", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, LicenseProfessionalModelSalutation]
        if isinstance(_salutation, Unset):
            salutation = UNSET
        else:
            salutation = LicenseProfessionalModelSalutation.from_dict(_salutation)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, LicenseProfessionalModelState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LicenseProfessionalModelState.from_dict(_state)

        suffix = d.pop("suffix", UNSET)

        title = d.pop("title", UNSET)

        license_professional_model = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            birth_date=birth_date,
            business_license=business_license,
            business_name=business_name,
            business_name_2=business_name_2,
            city=city,
            comment=comment,
            country=country,
            email=email,
            expiration_date=expiration_date,
            fax=fax,
            federal_employer_id=federal_employer_id,
            first_name=first_name,
            full_name=full_name,
            gender=gender,
            id=id,
            is_primary=is_primary,
            last_name=last_name,
            last_renewal_date=last_renewal_date,
            license_number=license_number,
            license_type=license_type,
            licensing_board=licensing_board,
            middle_name=middle_name,
            original_issue_date=original_issue_date,
            phone1=phone1,
            phone2=phone2,
            phone3=phone3,
            post_office_box=post_office_box,
            postal_code=postal_code,
            record_id=record_id,
            reference_license_id=reference_license_id,
            salutation=salutation,
            service_provider_code=service_provider_code,
            state=state,
            suffix=suffix,
            title=title,
        )

        license_professional_model.additional_properties = d
        return license_professional_model

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
