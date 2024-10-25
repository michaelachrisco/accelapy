from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_model import IdentifierModel


T = TypeVar("T", bound="ParcelModel1")


@_attrs_define
class ParcelModel1:
    """
    Attributes:
        block (Union[Unset, str]):
        book (Union[Unset, str]):
        census_tract (Union[Unset, str]):
        council_district (Union[Unset, str]):
        exemption_value (Union[Unset, float]):
        gis_sequence_number (Union[Unset, int]):
        id (Union[Unset, str]):
        improved_value (Union[Unset, float]):
        is_primary (Union[Unset, str]):
        land_value (Union[Unset, float]):
        legal_description (Union[Unset, str]):
        lot (Union[Unset, str]):
        map_number (Union[Unset, str]):
        map_reference_info (Union[Unset, str]):
        page (Union[Unset, str]):
        parcel (Union[Unset, str]):
        parcel_area (Union[Unset, float]):
        parcel_number (Union[Unset, str]):
        plan_area (Union[Unset, str]):
        range_ (Union[Unset, str]):
        section (Union[Unset, int]):
        status (Union[Unset, IdentifierModel]):
        subdivision (Union[Unset, IdentifierModel]):
        supervisor_district (Union[Unset, str]):
        township (Union[Unset, str]):
        tract (Union[Unset, str]):
    """

    block: Union[Unset, str] = UNSET
    book: Union[Unset, str] = UNSET
    census_tract: Union[Unset, str] = UNSET
    council_district: Union[Unset, str] = UNSET
    exemption_value: Union[Unset, float] = UNSET
    gis_sequence_number: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    improved_value: Union[Unset, float] = UNSET
    is_primary: Union[Unset, str] = UNSET
    land_value: Union[Unset, float] = UNSET
    legal_description: Union[Unset, str] = UNSET
    lot: Union[Unset, str] = UNSET
    map_number: Union[Unset, str] = UNSET
    map_reference_info: Union[Unset, str] = UNSET
    page: Union[Unset, str] = UNSET
    parcel: Union[Unset, str] = UNSET
    parcel_area: Union[Unset, float] = UNSET
    parcel_number: Union[Unset, str] = UNSET
    plan_area: Union[Unset, str] = UNSET
    range_: Union[Unset, str] = UNSET
    section: Union[Unset, int] = UNSET
    status: Union[Unset, "IdentifierModel"] = UNSET
    subdivision: Union[Unset, "IdentifierModel"] = UNSET
    supervisor_district: Union[Unset, str] = UNSET
    township: Union[Unset, str] = UNSET
    tract: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block = self.block
        book = self.book
        census_tract = self.census_tract
        council_district = self.council_district
        exemption_value = self.exemption_value
        gis_sequence_number = self.gis_sequence_number
        id = self.id
        improved_value = self.improved_value
        is_primary = self.is_primary
        land_value = self.land_value
        legal_description = self.legal_description
        lot = self.lot
        map_number = self.map_number
        map_reference_info = self.map_reference_info
        page = self.page
        parcel = self.parcel
        parcel_area = self.parcel_area
        parcel_number = self.parcel_number
        plan_area = self.plan_area
        range_ = self.range_
        section = self.section
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        subdivision: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subdivision, Unset):
            subdivision = self.subdivision.to_dict()

        supervisor_district = self.supervisor_district
        township = self.township
        tract = self.tract

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block is not UNSET:
            field_dict["block"] = block
        if book is not UNSET:
            field_dict["book"] = book
        if census_tract is not UNSET:
            field_dict["censusTract"] = census_tract
        if council_district is not UNSET:
            field_dict["councilDistrict"] = council_district
        if exemption_value is not UNSET:
            field_dict["exemptionValue"] = exemption_value
        if gis_sequence_number is not UNSET:
            field_dict["gisSequenceNumber"] = gis_sequence_number
        if id is not UNSET:
            field_dict["id"] = id
        if improved_value is not UNSET:
            field_dict["improvedValue"] = improved_value
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if land_value is not UNSET:
            field_dict["landValue"] = land_value
        if legal_description is not UNSET:
            field_dict["legalDescription"] = legal_description
        if lot is not UNSET:
            field_dict["lot"] = lot
        if map_number is not UNSET:
            field_dict["mapNumber"] = map_number
        if map_reference_info is not UNSET:
            field_dict["mapReferenceInfo"] = map_reference_info
        if page is not UNSET:
            field_dict["page"] = page
        if parcel is not UNSET:
            field_dict["parcel"] = parcel
        if parcel_area is not UNSET:
            field_dict["parcelArea"] = parcel_area
        if parcel_number is not UNSET:
            field_dict["parcelNumber"] = parcel_number
        if plan_area is not UNSET:
            field_dict["planArea"] = plan_area
        if range_ is not UNSET:
            field_dict["range"] = range_
        if section is not UNSET:
            field_dict["section"] = section
        if status is not UNSET:
            field_dict["status"] = status
        if subdivision is not UNSET:
            field_dict["subdivision"] = subdivision
        if supervisor_district is not UNSET:
            field_dict["supervisorDistrict"] = supervisor_district
        if township is not UNSET:
            field_dict["township"] = township
        if tract is not UNSET:
            field_dict["tract"] = tract

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_model import IdentifierModel

        d = src_dict.copy()
        block = d.pop("block", UNSET)

        book = d.pop("book", UNSET)

        census_tract = d.pop("censusTract", UNSET)

        council_district = d.pop("councilDistrict", UNSET)

        exemption_value = d.pop("exemptionValue", UNSET)

        gis_sequence_number = d.pop("gisSequenceNumber", UNSET)

        id = d.pop("id", UNSET)

        improved_value = d.pop("improvedValue", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        land_value = d.pop("landValue", UNSET)

        legal_description = d.pop("legalDescription", UNSET)

        lot = d.pop("lot", UNSET)

        map_number = d.pop("mapNumber", UNSET)

        map_reference_info = d.pop("mapReferenceInfo", UNSET)

        page = d.pop("page", UNSET)

        parcel = d.pop("parcel", UNSET)

        parcel_area = d.pop("parcelArea", UNSET)

        parcel_number = d.pop("parcelNumber", UNSET)

        plan_area = d.pop("planArea", UNSET)

        range_ = d.pop("range", UNSET)

        section = d.pop("section", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IdentifierModel]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IdentifierModel.from_dict(_status)

        _subdivision = d.pop("subdivision", UNSET)
        subdivision: Union[Unset, IdentifierModel]
        if isinstance(_subdivision, Unset):
            subdivision = UNSET
        else:
            subdivision = IdentifierModel.from_dict(_subdivision)

        supervisor_district = d.pop("supervisorDistrict", UNSET)

        township = d.pop("township", UNSET)

        tract = d.pop("tract", UNSET)

        parcel_model_1 = cls(
            block=block,
            book=book,
            census_tract=census_tract,
            council_district=council_district,
            exemption_value=exemption_value,
            gis_sequence_number=gis_sequence_number,
            id=id,
            improved_value=improved_value,
            is_primary=is_primary,
            land_value=land_value,
            legal_description=legal_description,
            lot=lot,
            map_number=map_number,
            map_reference_info=map_reference_info,
            page=page,
            parcel=parcel,
            parcel_area=parcel_area,
            parcel_number=parcel_number,
            plan_area=plan_area,
            range_=range_,
            section=section,
            status=status,
            subdivision=subdivision,
            supervisor_district=supervisor_district,
            township=township,
            tract=tract,
        )

        parcel_model_1.additional_properties = d
        return parcel_model_1

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
