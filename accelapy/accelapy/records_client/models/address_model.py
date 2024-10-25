from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cap_id_model import CapIDModel
    from ..models.identifier_model import IdentifierModel


T = TypeVar("T", bound="AddressModel")


@_attrs_define
class AddressModel:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        address_type_flag (Union[Unset, IdentifierModel]):
        city (Union[Unset, str]):
        country (Union[Unset, IdentifierModel]):
        county (Union[Unset, str]):
        description (Union[Unset, str]):
        direction (Union[Unset, IdentifierModel]):
        distance (Union[Unset, float]):
        house_alpha_end (Union[Unset, str]):
        house_alpha_start (Union[Unset, str]):
        house_fraction_end (Union[Unset, IdentifierModel]):
        house_fraction_start (Union[Unset, IdentifierModel]):
        id (Union[Unset, int]):
        inspection_district (Union[Unset, str]):
        inspection_district_prefix (Union[Unset, str]):
        is_primary (Union[Unset, str]):
        level_end (Union[Unset, str]):
        level_prefix (Union[Unset, str]):
        level_start (Union[Unset, str]):
        neighborhood (Union[Unset, str]):
        neighborhood_prefix (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        record_id (Union[Unset, CapIDModel]):
        ref_address_id (Union[Unset, int]):
        secondary_street (Union[Unset, str]):
        secondary_street_number (Union[Unset, int]):
        service_provider_code (Union[Unset, str]):
        state (Union[Unset, IdentifierModel]):
        status (Union[Unset, IdentifierModel]):
        street_address (Union[Unset, str]):
        street_end (Union[Unset, int]):
        street_end_from (Union[Unset, int]):
        street_end_to (Union[Unset, int]):
        street_name (Union[Unset, str]):
        street_prefix (Union[Unset, str]):
        street_start (Union[Unset, int]):
        street_start_from (Union[Unset, int]):
        street_start_to (Union[Unset, int]):
        street_suffix (Union[Unset, IdentifierModel]):
        street_suffix_direction (Union[Unset, IdentifierModel]):
        type (Union[Unset, IdentifierModel]):
        unit_end (Union[Unset, str]):
        unit_start (Union[Unset, str]):
        unit_type (Union[Unset, IdentifierModel]):
        x_coordinate (Union[Unset, float]):
        y_coordinate (Union[Unset, float]):
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_type_flag: Union[Unset, "IdentifierModel"] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, "IdentifierModel"] = UNSET
    county: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    direction: Union[Unset, "IdentifierModel"] = UNSET
    distance: Union[Unset, float] = UNSET
    house_alpha_end: Union[Unset, str] = UNSET
    house_alpha_start: Union[Unset, str] = UNSET
    house_fraction_end: Union[Unset, "IdentifierModel"] = UNSET
    house_fraction_start: Union[Unset, "IdentifierModel"] = UNSET
    id: Union[Unset, int] = UNSET
    inspection_district: Union[Unset, str] = UNSET
    inspection_district_prefix: Union[Unset, str] = UNSET
    is_primary: Union[Unset, str] = UNSET
    level_end: Union[Unset, str] = UNSET
    level_prefix: Union[Unset, str] = UNSET
    level_start: Union[Unset, str] = UNSET
    neighborhood: Union[Unset, str] = UNSET
    neighborhood_prefix: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    record_id: Union[Unset, "CapIDModel"] = UNSET
    ref_address_id: Union[Unset, int] = UNSET
    secondary_street: Union[Unset, str] = UNSET
    secondary_street_number: Union[Unset, int] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    state: Union[Unset, "IdentifierModel"] = UNSET
    status: Union[Unset, "IdentifierModel"] = UNSET
    street_address: Union[Unset, str] = UNSET
    street_end: Union[Unset, int] = UNSET
    street_end_from: Union[Unset, int] = UNSET
    street_end_to: Union[Unset, int] = UNSET
    street_name: Union[Unset, str] = UNSET
    street_prefix: Union[Unset, str] = UNSET
    street_start: Union[Unset, int] = UNSET
    street_start_from: Union[Unset, int] = UNSET
    street_start_to: Union[Unset, int] = UNSET
    street_suffix: Union[Unset, "IdentifierModel"] = UNSET
    street_suffix_direction: Union[Unset, "IdentifierModel"] = UNSET
    type: Union[Unset, "IdentifierModel"] = UNSET
    unit_end: Union[Unset, str] = UNSET
    unit_start: Union[Unset, str] = UNSET
    unit_type: Union[Unset, "IdentifierModel"] = UNSET
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
        description = self.description
        direction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        distance = self.distance
        house_alpha_end = self.house_alpha_end
        house_alpha_start = self.house_alpha_start
        house_fraction_end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.house_fraction_end, Unset):
            house_fraction_end = self.house_fraction_end.to_dict()

        house_fraction_start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.house_fraction_start, Unset):
            house_fraction_start = self.house_fraction_start.to_dict()

        id = self.id
        inspection_district = self.inspection_district
        inspection_district_prefix = self.inspection_district_prefix
        is_primary = self.is_primary
        level_end = self.level_end
        level_prefix = self.level_prefix
        level_start = self.level_start
        neighborhood = self.neighborhood
        neighborhood_prefix = self.neighborhood_prefix
        postal_code = self.postal_code
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        ref_address_id = self.ref_address_id
        secondary_street = self.secondary_street
        secondary_street_number = self.secondary_street_number
        service_provider_code = self.service_provider_code
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        street_address = self.street_address
        street_end = self.street_end
        street_end_from = self.street_end_from
        street_end_to = self.street_end_to
        street_name = self.street_name
        street_prefix = self.street_prefix
        street_start = self.street_start
        street_start_from = self.street_start_from
        street_start_to = self.street_start_to
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
        if description is not UNSET:
            field_dict["description"] = description
        if direction is not UNSET:
            field_dict["direction"] = direction
        if distance is not UNSET:
            field_dict["distance"] = distance
        if house_alpha_end is not UNSET:
            field_dict["houseAlphaEnd"] = house_alpha_end
        if house_alpha_start is not UNSET:
            field_dict["houseAlphaStart"] = house_alpha_start
        if house_fraction_end is not UNSET:
            field_dict["houseFractionEnd"] = house_fraction_end
        if house_fraction_start is not UNSET:
            field_dict["houseFractionStart"] = house_fraction_start
        if id is not UNSET:
            field_dict["id"] = id
        if inspection_district is not UNSET:
            field_dict["inspectionDistrict"] = inspection_district
        if inspection_district_prefix is not UNSET:
            field_dict["inspectionDistrictPrefix"] = inspection_district_prefix
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if level_end is not UNSET:
            field_dict["levelEnd"] = level_end
        if level_prefix is not UNSET:
            field_dict["levelPrefix"] = level_prefix
        if level_start is not UNSET:
            field_dict["levelStart"] = level_start
        if neighborhood is not UNSET:
            field_dict["neighborhood"] = neighborhood
        if neighborhood_prefix is not UNSET:
            field_dict["neighborhoodPrefix"] = neighborhood_prefix
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if ref_address_id is not UNSET:
            field_dict["refAddressId"] = ref_address_id
        if secondary_street is not UNSET:
            field_dict["secondaryStreet"] = secondary_street
        if secondary_street_number is not UNSET:
            field_dict["secondaryStreetNumber"] = secondary_street_number
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address
        if street_end is not UNSET:
            field_dict["streetEnd"] = street_end
        if street_end_from is not UNSET:
            field_dict["streetEndFrom"] = street_end_from
        if street_end_to is not UNSET:
            field_dict["streetEndTo"] = street_end_to
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_prefix is not UNSET:
            field_dict["streetPrefix"] = street_prefix
        if street_start is not UNSET:
            field_dict["streetStart"] = street_start
        if street_start_from is not UNSET:
            field_dict["streetStartFrom"] = street_start_from
        if street_start_to is not UNSET:
            field_dict["streetStartTo"] = street_start_to
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
        if x_coordinate is not UNSET:
            field_dict["xCoordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["yCoordinate"] = y_coordinate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cap_id_model import CapIDModel
        from ..models.identifier_model import IdentifierModel

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        _address_type_flag = d.pop("addressTypeFlag", UNSET)
        address_type_flag: Union[Unset, IdentifierModel]
        if isinstance(_address_type_flag, Unset):
            address_type_flag = UNSET
        else:
            address_type_flag = IdentifierModel.from_dict(_address_type_flag)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, IdentifierModel]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = IdentifierModel.from_dict(_country)

        county = d.pop("county", UNSET)

        description = d.pop("description", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, IdentifierModel]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = IdentifierModel.from_dict(_direction)

        distance = d.pop("distance", UNSET)

        house_alpha_end = d.pop("houseAlphaEnd", UNSET)

        house_alpha_start = d.pop("houseAlphaStart", UNSET)

        _house_fraction_end = d.pop("houseFractionEnd", UNSET)
        house_fraction_end: Union[Unset, IdentifierModel]
        if isinstance(_house_fraction_end, Unset):
            house_fraction_end = UNSET
        else:
            house_fraction_end = IdentifierModel.from_dict(_house_fraction_end)

        _house_fraction_start = d.pop("houseFractionStart", UNSET)
        house_fraction_start: Union[Unset, IdentifierModel]
        if isinstance(_house_fraction_start, Unset):
            house_fraction_start = UNSET
        else:
            house_fraction_start = IdentifierModel.from_dict(_house_fraction_start)

        id = d.pop("id", UNSET)

        inspection_district = d.pop("inspectionDistrict", UNSET)

        inspection_district_prefix = d.pop("inspectionDistrictPrefix", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        level_end = d.pop("levelEnd", UNSET)

        level_prefix = d.pop("levelPrefix", UNSET)

        level_start = d.pop("levelStart", UNSET)

        neighborhood = d.pop("neighborhood", UNSET)

        neighborhood_prefix = d.pop("neighborhoodPrefix", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, CapIDModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = CapIDModel.from_dict(_record_id)

        ref_address_id = d.pop("refAddressId", UNSET)

        secondary_street = d.pop("secondaryStreet", UNSET)

        secondary_street_number = d.pop("secondaryStreetNumber", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

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

        street_end_from = d.pop("streetEndFrom", UNSET)

        street_end_to = d.pop("streetEndTo", UNSET)

        street_name = d.pop("streetName", UNSET)

        street_prefix = d.pop("streetPrefix", UNSET)

        street_start = d.pop("streetStart", UNSET)

        street_start_from = d.pop("streetStartFrom", UNSET)

        street_start_to = d.pop("streetStartTo", UNSET)

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

        x_coordinate = d.pop("xCoordinate", UNSET)

        y_coordinate = d.pop("yCoordinate", UNSET)

        address_model = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_type_flag=address_type_flag,
            city=city,
            country=country,
            county=county,
            description=description,
            direction=direction,
            distance=distance,
            house_alpha_end=house_alpha_end,
            house_alpha_start=house_alpha_start,
            house_fraction_end=house_fraction_end,
            house_fraction_start=house_fraction_start,
            id=id,
            inspection_district=inspection_district,
            inspection_district_prefix=inspection_district_prefix,
            is_primary=is_primary,
            level_end=level_end,
            level_prefix=level_prefix,
            level_start=level_start,
            neighborhood=neighborhood,
            neighborhood_prefix=neighborhood_prefix,
            postal_code=postal_code,
            record_id=record_id,
            ref_address_id=ref_address_id,
            secondary_street=secondary_street,
            secondary_street_number=secondary_street_number,
            service_provider_code=service_provider_code,
            state=state,
            status=status,
            street_address=street_address,
            street_end=street_end,
            street_end_from=street_end_from,
            street_end_to=street_end_to,
            street_name=street_name,
            street_prefix=street_prefix,
            street_start=street_start,
            street_start_from=street_start_from,
            street_start_to=street_start_to,
            street_suffix=street_suffix,
            street_suffix_direction=street_suffix_direction,
            type=type,
            unit_end=unit_end,
            unit_start=unit_start,
            unit_type=unit_type,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
        )

        address_model.additional_properties = d
        return address_model

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
