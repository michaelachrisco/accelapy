import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_model import IdentifierModel


T = TypeVar("T", bound="ContactAddress")


@_attrs_define
class ContactAddress:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        address_line_3 (Union[Unset, str]):
        city (Union[Unset, str]):
        country (Union[Unset, IdentifierModel]):
        direction (Union[Unset, IdentifierModel]):
        effective_date (Union[Unset, datetime.datetime]):
        expiration_date (Union[Unset, datetime.datetime]):
        fax (Union[Unset, str]):
        fax_country_code (Union[Unset, str]):
        house_alpha_end (Union[Unset, str]):
        house_alpha_start (Union[Unset, str]):
        id (Union[Unset, int]):
        is_primary (Union[Unset, str]):
        level_end (Union[Unset, str]):
        level_prefix (Union[Unset, str]):
        level_start (Union[Unset, str]):
        phone (Union[Unset, str]):
        phone_country_code (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        recipient (Union[Unset, str]):
        state (Union[Unset, IdentifierModel]):
        status (Union[Unset, IdentifierModel]):
        street_address (Union[Unset, str]):
        street_end (Union[Unset, int]):
        street_name (Union[Unset, str]):
        street_prefix (Union[Unset, str]):
        street_start (Union[Unset, int]):
        street_suffix (Union[Unset, IdentifierModel]):
        street_suffix_direction (Union[Unset, IdentifierModel]):
        type (Union[Unset, IdentifierModel]):
        unit_end (Union[Unset, str]):
        unit_start (Union[Unset, str]):
        unit_type (Union[Unset, IdentifierModel]):
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, "IdentifierModel"] = UNSET
    direction: Union[Unset, "IdentifierModel"] = UNSET
    effective_date: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    fax: Union[Unset, str] = UNSET
    fax_country_code: Union[Unset, str] = UNSET
    house_alpha_end: Union[Unset, str] = UNSET
    house_alpha_start: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_primary: Union[Unset, str] = UNSET
    level_end: Union[Unset, str] = UNSET
    level_prefix: Union[Unset, str] = UNSET
    level_start: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_country_code: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    recipient: Union[Unset, str] = UNSET
    state: Union[Unset, "IdentifierModel"] = UNSET
    status: Union[Unset, "IdentifierModel"] = UNSET
    street_address: Union[Unset, str] = UNSET
    street_end: Union[Unset, int] = UNSET
    street_name: Union[Unset, str] = UNSET
    street_prefix: Union[Unset, str] = UNSET
    street_start: Union[Unset, int] = UNSET
    street_suffix: Union[Unset, "IdentifierModel"] = UNSET
    street_suffix_direction: Union[Unset, "IdentifierModel"] = UNSET
    type: Union[Unset, "IdentifierModel"] = UNSET
    unit_end: Union[Unset, str] = UNSET
    unit_start: Union[Unset, str] = UNSET
    unit_type: Union[Unset, "IdentifierModel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line_1 = self.address_line_1
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        city = self.city
        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        direction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        fax = self.fax
        fax_country_code = self.fax_country_code
        house_alpha_end = self.house_alpha_end
        house_alpha_start = self.house_alpha_start
        id = self.id
        is_primary = self.is_primary
        level_end = self.level_end
        level_prefix = self.level_prefix
        level_start = self.level_start
        phone = self.phone
        phone_country_code = self.phone_country_code
        postal_code = self.postal_code
        recipient = self.recipient
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        street_address = self.street_address
        street_end = self.street_end
        street_name = self.street_name
        street_prefix = self.street_prefix
        street_start = self.street_start
        street_suffix: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.street_suffix, Unset):
            street_suffix = self.street_suffix.to_dict()

        street_suffix_direction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.street_suffix_direction, Unset):
            street_suffix_direction = self.street_suffix_direction.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        unit_end = self.unit_end
        unit_start = self.unit_start
        unit_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if direction is not UNSET:
            field_dict["direction"] = direction
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if fax is not UNSET:
            field_dict["fax"] = fax
        if fax_country_code is not UNSET:
            field_dict["faxCountryCode"] = fax_country_code
        if house_alpha_end is not UNSET:
            field_dict["houseAlphaEnd"] = house_alpha_end
        if house_alpha_start is not UNSET:
            field_dict["houseAlphaStart"] = house_alpha_start
        if id is not UNSET:
            field_dict["id"] = id
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if level_end is not UNSET:
            field_dict["levelEnd"] = level_end
        if level_prefix is not UNSET:
            field_dict["levelPrefix"] = level_prefix
        if level_start is not UNSET:
            field_dict["levelStart"] = level_start
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_country_code is not UNSET:
            field_dict["phoneCountryCode"] = phone_country_code
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address
        if street_end is not UNSET:
            field_dict["streetEnd"] = street_end
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_prefix is not UNSET:
            field_dict["streetPrefix"] = street_prefix
        if street_start is not UNSET:
            field_dict["streetStart"] = street_start
        if street_suffix is not UNSET:
            field_dict["streetSuffix"] = street_suffix
        if street_suffix_direction is not UNSET:
            field_dict["streetSuffixDirection"] = street_suffix_direction
        if type is not UNSET:
            field_dict["type"] = type
        if unit_end is not UNSET:
            field_dict["unitEnd"] = unit_end
        if unit_start is not UNSET:
            field_dict["unitStart"] = unit_start
        if unit_type is not UNSET:
            field_dict["unitType"] = unit_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_model import IdentifierModel

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, IdentifierModel]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = IdentifierModel.from_dict(_country)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, IdentifierModel]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = IdentifierModel.from_dict(_direction)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.datetime]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        fax = d.pop("fax", UNSET)

        fax_country_code = d.pop("faxCountryCode", UNSET)

        house_alpha_end = d.pop("houseAlphaEnd", UNSET)

        house_alpha_start = d.pop("houseAlphaStart", UNSET)

        id = d.pop("id", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        level_end = d.pop("levelEnd", UNSET)

        level_prefix = d.pop("levelPrefix", UNSET)

        level_start = d.pop("levelStart", UNSET)

        phone = d.pop("phone", UNSET)

        phone_country_code = d.pop("phoneCountryCode", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        recipient = d.pop("recipient", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, IdentifierModel]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = IdentifierModel.from_dict(_state)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IdentifierModel]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IdentifierModel.from_dict(_status)

        street_address = d.pop("streetAddress", UNSET)

        street_end = d.pop("streetEnd", UNSET)

        street_name = d.pop("streetName", UNSET)

        street_prefix = d.pop("streetPrefix", UNSET)

        street_start = d.pop("streetStart", UNSET)

        _street_suffix = d.pop("streetSuffix", UNSET)
        street_suffix: Union[Unset, IdentifierModel]
        if isinstance(_street_suffix, Unset):
            street_suffix = UNSET
        else:
            street_suffix = IdentifierModel.from_dict(_street_suffix)

        _street_suffix_direction = d.pop("streetSuffixDirection", UNSET)
        street_suffix_direction: Union[Unset, IdentifierModel]
        if isinstance(_street_suffix_direction, Unset):
            street_suffix_direction = UNSET
        else:
            street_suffix_direction = IdentifierModel.from_dict(_street_suffix_direction)

        _type = d.pop("type", UNSET)
        type: Union[Unset, IdentifierModel]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = IdentifierModel.from_dict(_type)

        unit_end = d.pop("unitEnd", UNSET)

        unit_start = d.pop("unitStart", UNSET)

        _unit_type = d.pop("unitType", UNSET)
        unit_type: Union[Unset, IdentifierModel]
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = IdentifierModel.from_dict(_unit_type)

        contact_address = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            city=city,
            country=country,
            direction=direction,
            effective_date=effective_date,
            expiration_date=expiration_date,
            fax=fax,
            fax_country_code=fax_country_code,
            house_alpha_end=house_alpha_end,
            house_alpha_start=house_alpha_start,
            id=id,
            is_primary=is_primary,
            level_end=level_end,
            level_prefix=level_prefix,
            level_start=level_start,
            phone=phone,
            phone_country_code=phone_country_code,
            postal_code=postal_code,
            recipient=recipient,
            state=state,
            status=status,
            street_address=street_address,
            street_end=street_end,
            street_name=street_name,
            street_prefix=street_prefix,
            street_start=street_start,
            street_suffix=street_suffix,
            street_suffix_direction=street_suffix_direction,
            type=type,
            unit_end=unit_end,
            unit_start=unit_start,
            unit_type=unit_type,
        )

        contact_address.additional_properties = d
        return contact_address

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
