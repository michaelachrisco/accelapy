from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_record_address_model_address_type_flag import RequestRecordAddressModelAddressTypeFlag
    from ..models.request_record_address_model_country import RequestRecordAddressModelCountry
    from ..models.request_record_address_model_direction import RequestRecordAddressModelDirection
    from ..models.request_record_address_model_house_fraction_end import RequestRecordAddressModelHouseFractionEnd
    from ..models.request_record_address_model_house_fraction_start import RequestRecordAddressModelHouseFractionStart
    from ..models.request_record_address_model_state import RequestRecordAddressModelState
    from ..models.request_record_address_model_status import RequestRecordAddressModelStatus
    from ..models.request_record_address_model_street_suffix import RequestRecordAddressModelStreetSuffix
    from ..models.request_record_address_model_street_suffix_direction import (
        RequestRecordAddressModelStreetSuffixDirection,
    )
    from ..models.request_record_address_model_type import RequestRecordAddressModelType
    from ..models.request_record_address_model_unit_type import RequestRecordAddressModelUnitType


T = TypeVar("T", bound="RequestRecordAddressModel")


@_attrs_define
class RequestRecordAddressModel:
    """
    Attributes:
        address_line_1 (Union[Unset, str]): The first line of the address.
        address_line_2 (Union[Unset, str]): The first line of the address.
        address_type_flag (Union[Unset, RequestRecordAddressModelAddressTypeFlag]): A code name or an abbreviation of
            the address type.
        city (Union[Unset, str]): The name of the city.
        country (Union[Unset, RequestRecordAddressModelCountry]): The name of the country. See [Get All Address
            Countries](./api-settings.html#operation/v4.get.settings.addresses.countries).
        county (Union[Unset, str]): The name of the county.
        cross_street_name_start (Union[Unset, str]): The beginning intersecting street name for searching.

            Added in Civic Platform version: 9.2.0
        cross_street_name_end (Union[Unset, str]): The ending intersecting street name for searching.

            Added in Civic Platform version: 9.2.0
        description (Union[Unset, str]): A description of the address.
        direction (Union[Unset, RequestRecordAddressModelDirection]): The street direction of the primary address
            associated with the application.
        distance (Union[Unset, float]): The distance from another landmark used to locate the address.
        house_alpha_start (Union[Unset, str]): The beginning alphabetic unit in street address.
        house_alpha_end (Union[Unset, str]): The ending alphabetic unit in street address.
        house_fraction_start (Union[Unset, RequestRecordAddressModelHouseFractionStart]): Beginning fraction value used
            in combination with the Street number fields.
        house_fraction_end (Union[Unset, RequestRecordAddressModelHouseFractionEnd]): Ending franction value used in
            combination with the Street number fields.
        inspection_district (Union[Unset, str]): The inspection district where the address is located.
        inspection_district_prefix (Union[Unset, str]): The prefix for the inspection district where the address is
            located.
        is_primary (Union[Unset, str]): Indicates whether or not to designate the address as the primary address. Only
            one address can be primary at any given time.
        level_start (Union[Unset, str]): The starting level number (floor number) that makes up the address within a
            complex.
        level_end (Union[Unset, str]): The ending level number (floor number) that makes up the address within a
            complex.
        level_prefix (Union[Unset, str]): The prefix for the level numbers (floor numbers) that make up the address.
        location_type (Union[Unset, str]): The type of location used for Right of Way Management. The valid values are
            configured with the LOCATION_TYPE standard choice in Civic Platform Administration.

            Added in Civic Platform version: 9.2.0
        neighborhood (Union[Unset, str]): The neighborhood where the address is located.
        neighborhood_prefix (Union[Unset, str]): The prefix for neighborhood where the address is located.
        postal_code (Union[Unset, str]): The postal ZIP code for the address.
        secondary_street (Union[Unset, str]): This field (along with the Secondary Road Number field) displays an extra
            description for the location when two roads that cross or a street with two names makes up the address of the
            location.
        secondary_street_number (Union[Unset, float]): This field (along with the Secondary Road field) displays an
            extra description for the location when two roads that cross or a street with two names makes up the address of
            the location.
        state (Union[Unset, RequestRecordAddressModelState]): The name of the state.
        status (Union[Unset, RequestRecordAddressModelStatus]): The address status indicating whether the address is
            active or inactive.
        street_address (Union[Unset, str]): The street address.
        street_end (Union[Unset, float]): The ending number of a street address range.
        street_name (Union[Unset, str]): The name of the street.
        street_name_start (Union[Unset, str]): The beginning street name for searching.

            Added in Civic Platform version: 9.2.0
        street_name_end (Union[Unset, str]): The ending street name for searching.

            Added in Civic Platform version: 9.2.0
        street_prefix (Union[Unset, str]): Any part of an address that appears before a street name or number. For
            example, if the address is 123 West Main, "West" is the street prefix.
        street_start (Union[Unset, float]): The starting number of a street address range.
        street_suffix (Union[Unset, RequestRecordAddressModelStreetSuffix]): The type of street such as "Lane" or
            "Boulevard".
        street_suffix_direction (Union[Unset, RequestRecordAddressModelStreetSuffixDirection]): The direction appended
            to the street suffix. For example, if the address is 500 56th Avenue NW, "NW" is the street suffix direction.
        type (Union[Unset, RequestRecordAddressModelType]): The address type.
        unit_start (Union[Unset, str]): The starting value of a range of unit numbers.
        unit_end (Union[Unset, str]): The ending value of a range of unit numbers.
        unit_type (Union[Unset, RequestRecordAddressModelUnitType]): The unit type designation of the address.
        x_coordinate (Union[Unset, float]): The longitudinal coordinate for this address.
        y_coordinate (Union[Unset, float]): The latitudinal coordinate for this address.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_type_flag: Union[Unset, "RequestRecordAddressModelAddressTypeFlag"] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, "RequestRecordAddressModelCountry"] = UNSET
    county: Union[Unset, str] = UNSET
    cross_street_name_start: Union[Unset, str] = UNSET
    cross_street_name_end: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    direction: Union[Unset, "RequestRecordAddressModelDirection"] = UNSET
    distance: Union[Unset, float] = UNSET
    house_alpha_start: Union[Unset, str] = UNSET
    house_alpha_end: Union[Unset, str] = UNSET
    house_fraction_start: Union[Unset, "RequestRecordAddressModelHouseFractionStart"] = UNSET
    house_fraction_end: Union[Unset, "RequestRecordAddressModelHouseFractionEnd"] = UNSET
    inspection_district: Union[Unset, str] = UNSET
    inspection_district_prefix: Union[Unset, str] = UNSET
    is_primary: Union[Unset, str] = UNSET
    level_start: Union[Unset, str] = UNSET
    level_end: Union[Unset, str] = UNSET
    level_prefix: Union[Unset, str] = UNSET
    location_type: Union[Unset, str] = UNSET
    neighborhood: Union[Unset, str] = UNSET
    neighborhood_prefix: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    secondary_street: Union[Unset, str] = UNSET
    secondary_street_number: Union[Unset, float] = UNSET
    state: Union[Unset, "RequestRecordAddressModelState"] = UNSET
    status: Union[Unset, "RequestRecordAddressModelStatus"] = UNSET
    street_address: Union[Unset, str] = UNSET
    street_end: Union[Unset, float] = UNSET
    street_name: Union[Unset, str] = UNSET
    street_name_start: Union[Unset, str] = UNSET
    street_name_end: Union[Unset, str] = UNSET
    street_prefix: Union[Unset, str] = UNSET
    street_start: Union[Unset, float] = UNSET
    street_suffix: Union[Unset, "RequestRecordAddressModelStreetSuffix"] = UNSET
    street_suffix_direction: Union[Unset, "RequestRecordAddressModelStreetSuffixDirection"] = UNSET
    type: Union[Unset, "RequestRecordAddressModelType"] = UNSET
    unit_start: Union[Unset, str] = UNSET
    unit_end: Union[Unset, str] = UNSET
    unit_type: Union[Unset, "RequestRecordAddressModelUnitType"] = UNSET
    x_coordinate: Union[Unset, float] = UNSET
    y_coordinate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line_1 = self.address_line_1
        address_line_2 = self.address_line_2
        address_type_flag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_type_flag, Unset):
            address_type_flag = self.address_type_flag.to_dict()

        city = self.city
        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        county = self.county
        cross_street_name_start = self.cross_street_name_start
        cross_street_name_end = self.cross_street_name_end
        description = self.description
        direction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        distance = self.distance
        house_alpha_start = self.house_alpha_start
        house_alpha_end = self.house_alpha_end
        house_fraction_start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.house_fraction_start, Unset):
            house_fraction_start = self.house_fraction_start.to_dict()

        house_fraction_end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.house_fraction_end, Unset):
            house_fraction_end = self.house_fraction_end.to_dict()

        inspection_district = self.inspection_district
        inspection_district_prefix = self.inspection_district_prefix
        is_primary = self.is_primary
        level_start = self.level_start
        level_end = self.level_end
        level_prefix = self.level_prefix
        location_type = self.location_type
        neighborhood = self.neighborhood
        neighborhood_prefix = self.neighborhood_prefix
        postal_code = self.postal_code
        secondary_street = self.secondary_street
        secondary_street_number = self.secondary_street_number
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        street_address = self.street_address
        street_end = self.street_end
        street_name = self.street_name
        street_name_start = self.street_name_start
        street_name_end = self.street_name_end
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

        unit_start = self.unit_start
        unit_end = self.unit_end
        unit_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.to_dict()

        x_coordinate = self.x_coordinate
        y_coordinate = self.y_coordinate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_type_flag is not UNSET:
            field_dict["addressTypeFlag"] = address_type_flag
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if county is not UNSET:
            field_dict["county"] = county
        if cross_street_name_start is not UNSET:
            field_dict["crossStreetNameStart"] = cross_street_name_start
        if cross_street_name_end is not UNSET:
            field_dict["crossStreetNameEnd"] = cross_street_name_end
        if description is not UNSET:
            field_dict["description"] = description
        if direction is not UNSET:
            field_dict["direction"] = direction
        if distance is not UNSET:
            field_dict["distance"] = distance
        if house_alpha_start is not UNSET:
            field_dict["houseAlphaStart"] = house_alpha_start
        if house_alpha_end is not UNSET:
            field_dict["houseAlphaEnd"] = house_alpha_end
        if house_fraction_start is not UNSET:
            field_dict["houseFractionStart"] = house_fraction_start
        if house_fraction_end is not UNSET:
            field_dict["houseFractionEnd"] = house_fraction_end
        if inspection_district is not UNSET:
            field_dict["inspectionDistrict"] = inspection_district
        if inspection_district_prefix is not UNSET:
            field_dict["inspectionDistrictPrefix"] = inspection_district_prefix
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if level_start is not UNSET:
            field_dict["levelStart"] = level_start
        if level_end is not UNSET:
            field_dict["levelEnd"] = level_end
        if level_prefix is not UNSET:
            field_dict["levelPrefix"] = level_prefix
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if neighborhood is not UNSET:
            field_dict["neighborhood"] = neighborhood
        if neighborhood_prefix is not UNSET:
            field_dict["neighborhoodPrefix"] = neighborhood_prefix
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if secondary_street is not UNSET:
            field_dict["secondaryStreet"] = secondary_street
        if secondary_street_number is not UNSET:
            field_dict["secondaryStreetNumber"] = secondary_street_number
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
        if street_name_start is not UNSET:
            field_dict["streetNameStart"] = street_name_start
        if street_name_end is not UNSET:
            field_dict["streetNameEnd"] = street_name_end
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
        if unit_start is not UNSET:
            field_dict["unitStart"] = unit_start
        if unit_end is not UNSET:
            field_dict["unitEnd"] = unit_end
        if unit_type is not UNSET:
            field_dict["unitType"] = unit_type
        if x_coordinate is not UNSET:
            field_dict["xCoordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["yCoordinate"] = y_coordinate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.request_record_address_model_address_type_flag import RequestRecordAddressModelAddressTypeFlag
        from ..models.request_record_address_model_country import RequestRecordAddressModelCountry
        from ..models.request_record_address_model_direction import RequestRecordAddressModelDirection
        from ..models.request_record_address_model_house_fraction_end import RequestRecordAddressModelHouseFractionEnd
        from ..models.request_record_address_model_house_fraction_start import (
            RequestRecordAddressModelHouseFractionStart,
        )
        from ..models.request_record_address_model_state import RequestRecordAddressModelState
        from ..models.request_record_address_model_status import RequestRecordAddressModelStatus
        from ..models.request_record_address_model_street_suffix import RequestRecordAddressModelStreetSuffix
        from ..models.request_record_address_model_street_suffix_direction import (
            RequestRecordAddressModelStreetSuffixDirection,
        )
        from ..models.request_record_address_model_type import RequestRecordAddressModelType
        from ..models.request_record_address_model_unit_type import RequestRecordAddressModelUnitType

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        _address_type_flag = d.pop("addressTypeFlag", UNSET)
        address_type_flag: Union[Unset, RequestRecordAddressModelAddressTypeFlag]
        if isinstance(_address_type_flag, Unset):
            address_type_flag = UNSET
        else:
            address_type_flag = RequestRecordAddressModelAddressTypeFlag.from_dict(_address_type_flag)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, RequestRecordAddressModelCountry]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = RequestRecordAddressModelCountry.from_dict(_country)

        county = d.pop("county", UNSET)

        cross_street_name_start = d.pop("crossStreetNameStart", UNSET)

        cross_street_name_end = d.pop("crossStreetNameEnd", UNSET)

        description = d.pop("description", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, RequestRecordAddressModelDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = RequestRecordAddressModelDirection.from_dict(_direction)

        distance = d.pop("distance", UNSET)

        house_alpha_start = d.pop("houseAlphaStart", UNSET)

        house_alpha_end = d.pop("houseAlphaEnd", UNSET)

        _house_fraction_start = d.pop("houseFractionStart", UNSET)
        house_fraction_start: Union[Unset, RequestRecordAddressModelHouseFractionStart]
        if isinstance(_house_fraction_start, Unset):
            house_fraction_start = UNSET
        else:
            house_fraction_start = RequestRecordAddressModelHouseFractionStart.from_dict(_house_fraction_start)

        _house_fraction_end = d.pop("houseFractionEnd", UNSET)
        house_fraction_end: Union[Unset, RequestRecordAddressModelHouseFractionEnd]
        if isinstance(_house_fraction_end, Unset):
            house_fraction_end = UNSET
        else:
            house_fraction_end = RequestRecordAddressModelHouseFractionEnd.from_dict(_house_fraction_end)

        inspection_district = d.pop("inspectionDistrict", UNSET)

        inspection_district_prefix = d.pop("inspectionDistrictPrefix", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        level_start = d.pop("levelStart", UNSET)

        level_end = d.pop("levelEnd", UNSET)

        level_prefix = d.pop("levelPrefix", UNSET)

        location_type = d.pop("locationType", UNSET)

        neighborhood = d.pop("neighborhood", UNSET)

        neighborhood_prefix = d.pop("neighborhoodPrefix", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        secondary_street = d.pop("secondaryStreet", UNSET)

        secondary_street_number = d.pop("secondaryStreetNumber", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, RequestRecordAddressModelState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RequestRecordAddressModelState.from_dict(_state)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RequestRecordAddressModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestRecordAddressModelStatus.from_dict(_status)

        street_address = d.pop("streetAddress", UNSET)

        street_end = d.pop("streetEnd", UNSET)

        street_name = d.pop("streetName", UNSET)

        street_name_start = d.pop("streetNameStart", UNSET)

        street_name_end = d.pop("streetNameEnd", UNSET)

        street_prefix = d.pop("streetPrefix", UNSET)

        street_start = d.pop("streetStart", UNSET)

        _street_suffix = d.pop("streetSuffix", UNSET)
        street_suffix: Union[Unset, RequestRecordAddressModelStreetSuffix]
        if isinstance(_street_suffix, Unset):
            street_suffix = UNSET
        else:
            street_suffix = RequestRecordAddressModelStreetSuffix.from_dict(_street_suffix)

        _street_suffix_direction = d.pop("streetSuffixDirection", UNSET)
        street_suffix_direction: Union[Unset, RequestRecordAddressModelStreetSuffixDirection]
        if isinstance(_street_suffix_direction, Unset):
            street_suffix_direction = UNSET
        else:
            street_suffix_direction = RequestRecordAddressModelStreetSuffixDirection.from_dict(_street_suffix_direction)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RequestRecordAddressModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RequestRecordAddressModelType.from_dict(_type)

        unit_start = d.pop("unitStart", UNSET)

        unit_end = d.pop("unitEnd", UNSET)

        _unit_type = d.pop("unitType", UNSET)
        unit_type: Union[Unset, RequestRecordAddressModelUnitType]
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = RequestRecordAddressModelUnitType.from_dict(_unit_type)

        x_coordinate = d.pop("xCoordinate", UNSET)

        y_coordinate = d.pop("yCoordinate", UNSET)

        request_record_address_model = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_type_flag=address_type_flag,
            city=city,
            country=country,
            county=county,
            cross_street_name_start=cross_street_name_start,
            cross_street_name_end=cross_street_name_end,
            description=description,
            direction=direction,
            distance=distance,
            house_alpha_start=house_alpha_start,
            house_alpha_end=house_alpha_end,
            house_fraction_start=house_fraction_start,
            house_fraction_end=house_fraction_end,
            inspection_district=inspection_district,
            inspection_district_prefix=inspection_district_prefix,
            is_primary=is_primary,
            level_start=level_start,
            level_end=level_end,
            level_prefix=level_prefix,
            location_type=location_type,
            neighborhood=neighborhood,
            neighborhood_prefix=neighborhood_prefix,
            postal_code=postal_code,
            secondary_street=secondary_street,
            secondary_street_number=secondary_street_number,
            state=state,
            status=status,
            street_address=street_address,
            street_end=street_end,
            street_name=street_name,
            street_name_start=street_name_start,
            street_name_end=street_name_end,
            street_prefix=street_prefix,
            street_start=street_start,
            street_suffix=street_suffix,
            street_suffix_direction=street_suffix_direction,
            type=type,
            unit_start=unit_start,
            unit_end=unit_end,
            unit_type=unit_type,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
        )

        request_record_address_model.additional_properties = d
        return request_record_address_model

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
