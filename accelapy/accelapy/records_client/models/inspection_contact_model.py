import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_contact_model_birth_city import InspectionContactModelBirthCity
    from ..models.inspection_contact_model_birth_region import InspectionContactModelBirthRegion
    from ..models.inspection_contact_model_birth_state import InspectionContactModelBirthState
    from ..models.inspection_contact_model_driver_license_state import InspectionContactModelDriverLicenseState
    from ..models.inspection_contact_model_gender import InspectionContactModelGender
    from ..models.inspection_contact_model_preferred_channel import InspectionContactModelPreferredChannel
    from ..models.inspection_contact_model_race import InspectionContactModelRace
    from ..models.inspection_contact_model_relation import InspectionContactModelRelation
    from ..models.inspection_contact_model_salutation import InspectionContactModelSalutation
    from ..models.inspection_contact_model_status import InspectionContactModelStatus
    from ..models.inspection_contact_model_type import InspectionContactModelType
    from ..models.owner_address_model import OwnerAddressModel


T = TypeVar("T", bound="InspectionContactModel")


@_attrs_define
class InspectionContactModel:
    """
    Attributes:
        address (Union[Unset, OwnerAddressModel]):
        birth_city (Union[Unset, InspectionContactModelBirthCity]): The city of birth for an individual.
        birth_date (Union[Unset, datetime.datetime]): The birth date.
        birth_region (Union[Unset, InspectionContactModelBirthRegion]): The country of birth or region of birth for an
            individual.
        birth_state (Union[Unset, InspectionContactModelBirthState]): The state of birth for an individual.
        business_name (Union[Unset, str]): A secondary business name for the applicable individual.
        comment (Union[Unset, str]): A comment about the inspection contact.
        deceased_date (Union[Unset, datetime.datetime]): The deceased date.
        driver_license_number (Union[Unset, str]): The driver's license number of the contact. This field is active only
            when the Contact Type selected is Individual.
        driver_license_state (Union[Unset, InspectionContactModelDriverLicenseState]): The state that issued the
            driver's license.
        email (Union[Unset, str]): The contact's email address.
        fax (Union[Unset, str]): The fax number for the contact.
        fax_country_code (Union[Unset, str]): Fax Number Country Code
        federal_employer_id (Union[Unset, str]): The Federal Employer Identification Number. It is used to identify a
            business for tax purposes.
        first_name (Union[Unset, str]): The contact's first name.
        full_name (Union[Unset, str]): The contact's full name.
        gender (Union[Unset, InspectionContactModelGender]): The gender (male or female) of the individual.
        id (Union[Unset, str]): The contact system id assigned by the Civic Platform server.
        individual_or_organization (Union[Unset, str]): The organization to which the contact belongs. This field is
            only active when the Contact Type selected is Organization.
        last_name (Union[Unset, str]): The last name (surname).
        middle_name (Union[Unset, str]): The middle name.
        organization_name (Union[Unset, str]): The organization to which the contact belongs. This field is only active
            when the Contact Type selected is Organization.
        passport_number (Union[Unset, str]): The contact's passport number. This field is only active when the Contact
            Type selected is Individual.
        phone1 (Union[Unset, str]): The primary telephone number of the contact.
        phone_1_country_code (Union[Unset, str]): Phone Number 1 Country Code
        phone2 (Union[Unset, str]): The secondary telephone number of the contact.
        phone_2_country_code (Union[Unset, str]): Phone Number 2 Country Code
        phone3 (Union[Unset, str]): The tertiary telephone number for the contact.
        phone_3_country_code (Union[Unset, str]): Phone Number 3 Country Code
        post_office_box (Union[Unset, str]): The post office box number.
        preferred_channel (Union[Unset, InspectionContactModelPreferredChannel]): The method by which the contact
            prefers to be notified, by phone for example. See [Get All Contact Preferred Channels](./api-
            settings.html#operation/v4.get.settings.contacts.preferredChannels).
        race (Union[Unset, InspectionContactModelRace]): The contact's race or ethnicity. See [Get All Contact
            Races](./api-settings.html#operation/v4.get.settings.contacts.races).
        relation (Union[Unset, InspectionContactModelRelation]): The contact's relationship to the application or
            service request.
        salutation (Union[Unset, InspectionContactModelSalutation]): The salutation to be used when addressing the
            contact; for example Mr. oar Ms. This field is active only when Contact Type = Individual. See [Get All Contact
            Salutations](./api-settings.html#operation/v4.get.settings.contacts.salutations).
        service_provider_code (Union[Unset, str]): The unique agency identifier
        social_security_number (Union[Unset, str]): The individual's social security number. This field is only active
            when the Contact Type selected is Individual.
        state_id_number (Union[Unset, str]): The contact's state ID number. This field is only active when the Contact
            Type selected is Individual.
        status (Union[Unset, InspectionContactModelStatus]): The contact status.
        suffix (Union[Unset, str]): The contact name suffix.
        title (Union[Unset, str]): The individual's business title.
        trade_name (Union[Unset, str]): The contact's preferred business or trade name. This field is active only when
            the Contact Type selected is Organization.
        type (Union[Unset, InspectionContactModelType]): The contact type. See [Get All Contact Types](./api-
            settings.html#operation/v4.get.settings.contacts.types).
    """

    address: Union[Unset, "OwnerAddressModel"] = UNSET
    birth_city: Union[Unset, "InspectionContactModelBirthCity"] = UNSET
    birth_date: Union[Unset, datetime.datetime] = UNSET
    birth_region: Union[Unset, "InspectionContactModelBirthRegion"] = UNSET
    birth_state: Union[Unset, "InspectionContactModelBirthState"] = UNSET
    business_name: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    deceased_date: Union[Unset, datetime.datetime] = UNSET
    driver_license_number: Union[Unset, str] = UNSET
    driver_license_state: Union[Unset, "InspectionContactModelDriverLicenseState"] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    fax_country_code: Union[Unset, str] = UNSET
    federal_employer_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    gender: Union[Unset, "InspectionContactModelGender"] = UNSET
    id: Union[Unset, str] = UNSET
    individual_or_organization: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    organization_name: Union[Unset, str] = UNSET
    passport_number: Union[Unset, str] = UNSET
    phone1: Union[Unset, str] = UNSET
    phone_1_country_code: Union[Unset, str] = UNSET
    phone2: Union[Unset, str] = UNSET
    phone_2_country_code: Union[Unset, str] = UNSET
    phone3: Union[Unset, str] = UNSET
    phone_3_country_code: Union[Unset, str] = UNSET
    post_office_box: Union[Unset, str] = UNSET
    preferred_channel: Union[Unset, "InspectionContactModelPreferredChannel"] = UNSET
    race: Union[Unset, "InspectionContactModelRace"] = UNSET
    relation: Union[Unset, "InspectionContactModelRelation"] = UNSET
    salutation: Union[Unset, "InspectionContactModelSalutation"] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    social_security_number: Union[Unset, str] = UNSET
    state_id_number: Union[Unset, str] = UNSET
    status: Union[Unset, "InspectionContactModelStatus"] = UNSET
    suffix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    trade_name: Union[Unset, str] = UNSET
    type: Union[Unset, "InspectionContactModelType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        birth_city: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_city, Unset):
            birth_city = self.birth_city.to_dict()

        birth_date: Union[Unset, str] = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        birth_region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_region, Unset):
            birth_region = self.birth_region.to_dict()

        birth_state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_state, Unset):
            birth_state = self.birth_state.to_dict()

        business_name = self.business_name
        comment = self.comment
        deceased_date: Union[Unset, str] = UNSET
        if not isinstance(self.deceased_date, Unset):
            deceased_date = self.deceased_date.isoformat()

        driver_license_number = self.driver_license_number
        driver_license_state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.driver_license_state, Unset):
            driver_license_state = self.driver_license_state.to_dict()

        email = self.email
        fax = self.fax
        fax_country_code = self.fax_country_code
        federal_employer_id = self.federal_employer_id
        first_name = self.first_name
        full_name = self.full_name
        gender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        id = self.id
        individual_or_organization = self.individual_or_organization
        last_name = self.last_name
        middle_name = self.middle_name
        organization_name = self.organization_name
        passport_number = self.passport_number
        phone1 = self.phone1
        phone_1_country_code = self.phone_1_country_code
        phone2 = self.phone2
        phone_2_country_code = self.phone_2_country_code
        phone3 = self.phone3
        phone_3_country_code = self.phone_3_country_code
        post_office_box = self.post_office_box
        preferred_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preferred_channel, Unset):
            preferred_channel = self.preferred_channel.to_dict()

        race: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.race, Unset):
            race = self.race.to_dict()

        relation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation.to_dict()

        salutation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.to_dict()

        service_provider_code = self.service_provider_code
        social_security_number = self.social_security_number
        state_id_number = self.state_id_number
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        suffix = self.suffix
        title = self.title
        trade_name = self.trade_name
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if birth_city is not UNSET:
            field_dict["birthCity"] = birth_city
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if birth_region is not UNSET:
            field_dict["birthRegion"] = birth_region
        if birth_state is not UNSET:
            field_dict["birthState"] = birth_state
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if comment is not UNSET:
            field_dict["comment"] = comment
        if deceased_date is not UNSET:
            field_dict["deceasedDate"] = deceased_date
        if driver_license_number is not UNSET:
            field_dict["driverLicenseNumber"] = driver_license_number
        if driver_license_state is not UNSET:
            field_dict["driverLicenseState"] = driver_license_state
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if fax_country_code is not UNSET:
            field_dict["faxCountryCode"] = fax_country_code
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
        if individual_or_organization is not UNSET:
            field_dict["individualOrOrganization"] = individual_or_organization
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if passport_number is not UNSET:
            field_dict["passportNumber"] = passport_number
        if phone1 is not UNSET:
            field_dict["phone1"] = phone1
        if phone_1_country_code is not UNSET:
            field_dict["phone1CountryCode"] = phone_1_country_code
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone_2_country_code is not UNSET:
            field_dict["phone2CountryCode"] = phone_2_country_code
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if phone_3_country_code is not UNSET:
            field_dict["phone3CountryCode"] = phone_3_country_code
        if post_office_box is not UNSET:
            field_dict["postOfficeBox"] = post_office_box
        if preferred_channel is not UNSET:
            field_dict["preferredChannel"] = preferred_channel
        if race is not UNSET:
            field_dict["race"] = race
        if relation is not UNSET:
            field_dict["relation"] = relation
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if social_security_number is not UNSET:
            field_dict["socialSecurityNumber"] = social_security_number
        if state_id_number is not UNSET:
            field_dict["stateIdNumber"] = state_id_number
        if status is not UNSET:
            field_dict["status"] = status
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if title is not UNSET:
            field_dict["title"] = title
        if trade_name is not UNSET:
            field_dict["tradeName"] = trade_name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inspection_contact_model_birth_city import InspectionContactModelBirthCity
        from ..models.inspection_contact_model_birth_region import InspectionContactModelBirthRegion
        from ..models.inspection_contact_model_birth_state import InspectionContactModelBirthState
        from ..models.inspection_contact_model_driver_license_state import InspectionContactModelDriverLicenseState
        from ..models.inspection_contact_model_gender import InspectionContactModelGender
        from ..models.inspection_contact_model_preferred_channel import InspectionContactModelPreferredChannel
        from ..models.inspection_contact_model_race import InspectionContactModelRace
        from ..models.inspection_contact_model_relation import InspectionContactModelRelation
        from ..models.inspection_contact_model_salutation import InspectionContactModelSalutation
        from ..models.inspection_contact_model_status import InspectionContactModelStatus
        from ..models.inspection_contact_model_type import InspectionContactModelType
        from ..models.owner_address_model import OwnerAddressModel

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, OwnerAddressModel]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = OwnerAddressModel.from_dict(_address)

        _birth_city = d.pop("birthCity", UNSET)
        birth_city: Union[Unset, InspectionContactModelBirthCity]
        if isinstance(_birth_city, Unset):
            birth_city = UNSET
        else:
            birth_city = InspectionContactModelBirthCity.from_dict(_birth_city)

        _birth_date = d.pop("birthDate", UNSET)
        birth_date: Union[Unset, datetime.datetime]
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date)

        _birth_region = d.pop("birthRegion", UNSET)
        birth_region: Union[Unset, InspectionContactModelBirthRegion]
        if isinstance(_birth_region, Unset):
            birth_region = UNSET
        else:
            birth_region = InspectionContactModelBirthRegion.from_dict(_birth_region)

        _birth_state = d.pop("birthState", UNSET)
        birth_state: Union[Unset, InspectionContactModelBirthState]
        if isinstance(_birth_state, Unset):
            birth_state = UNSET
        else:
            birth_state = InspectionContactModelBirthState.from_dict(_birth_state)

        business_name = d.pop("businessName", UNSET)

        comment = d.pop("comment", UNSET)

        _deceased_date = d.pop("deceasedDate", UNSET)
        deceased_date: Union[Unset, datetime.datetime]
        if isinstance(_deceased_date, Unset):
            deceased_date = UNSET
        else:
            deceased_date = isoparse(_deceased_date)

        driver_license_number = d.pop("driverLicenseNumber", UNSET)

        _driver_license_state = d.pop("driverLicenseState", UNSET)
        driver_license_state: Union[Unset, InspectionContactModelDriverLicenseState]
        if isinstance(_driver_license_state, Unset):
            driver_license_state = UNSET
        else:
            driver_license_state = InspectionContactModelDriverLicenseState.from_dict(_driver_license_state)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        fax_country_code = d.pop("faxCountryCode", UNSET)

        federal_employer_id = d.pop("federalEmployerId", UNSET)

        first_name = d.pop("firstName", UNSET)

        full_name = d.pop("fullName", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, InspectionContactModelGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = InspectionContactModelGender.from_dict(_gender)

        id = d.pop("id", UNSET)

        individual_or_organization = d.pop("individualOrOrganization", UNSET)

        last_name = d.pop("lastName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        organization_name = d.pop("organizationName", UNSET)

        passport_number = d.pop("passportNumber", UNSET)

        phone1 = d.pop("phone1", UNSET)

        phone_1_country_code = d.pop("phone1CountryCode", UNSET)

        phone2 = d.pop("phone2", UNSET)

        phone_2_country_code = d.pop("phone2CountryCode", UNSET)

        phone3 = d.pop("phone3", UNSET)

        phone_3_country_code = d.pop("phone3CountryCode", UNSET)

        post_office_box = d.pop("postOfficeBox", UNSET)

        _preferred_channel = d.pop("preferredChannel", UNSET)
        preferred_channel: Union[Unset, InspectionContactModelPreferredChannel]
        if isinstance(_preferred_channel, Unset):
            preferred_channel = UNSET
        else:
            preferred_channel = InspectionContactModelPreferredChannel.from_dict(_preferred_channel)

        _race = d.pop("race", UNSET)
        race: Union[Unset, InspectionContactModelRace]
        if isinstance(_race, Unset):
            race = UNSET
        else:
            race = InspectionContactModelRace.from_dict(_race)

        _relation = d.pop("relation", UNSET)
        relation: Union[Unset, InspectionContactModelRelation]
        if isinstance(_relation, Unset):
            relation = UNSET
        else:
            relation = InspectionContactModelRelation.from_dict(_relation)

        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, InspectionContactModelSalutation]
        if isinstance(_salutation, Unset):
            salutation = UNSET
        else:
            salutation = InspectionContactModelSalutation.from_dict(_salutation)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        social_security_number = d.pop("socialSecurityNumber", UNSET)

        state_id_number = d.pop("stateIdNumber", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InspectionContactModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InspectionContactModelStatus.from_dict(_status)

        suffix = d.pop("suffix", UNSET)

        title = d.pop("title", UNSET)

        trade_name = d.pop("tradeName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InspectionContactModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InspectionContactModelType.from_dict(_type)

        inspection_contact_model = cls(
            address=address,
            birth_city=birth_city,
            birth_date=birth_date,
            birth_region=birth_region,
            birth_state=birth_state,
            business_name=business_name,
            comment=comment,
            deceased_date=deceased_date,
            driver_license_number=driver_license_number,
            driver_license_state=driver_license_state,
            email=email,
            fax=fax,
            fax_country_code=fax_country_code,
            federal_employer_id=federal_employer_id,
            first_name=first_name,
            full_name=full_name,
            gender=gender,
            id=id,
            individual_or_organization=individual_or_organization,
            last_name=last_name,
            middle_name=middle_name,
            organization_name=organization_name,
            passport_number=passport_number,
            phone1=phone1,
            phone_1_country_code=phone_1_country_code,
            phone2=phone2,
            phone_2_country_code=phone_2_country_code,
            phone3=phone3,
            phone_3_country_code=phone_3_country_code,
            post_office_box=post_office_box,
            preferred_channel=preferred_channel,
            race=race,
            relation=relation,
            salutation=salutation,
            service_provider_code=service_provider_code,
            social_security_number=social_security_number,
            state_id_number=state_id_number,
            status=status,
            suffix=suffix,
            title=title,
            trade_name=trade_name,
            type=type,
        )

        inspection_contact_model.additional_properties = d
        return inspection_contact_model

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
