from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_additional_model_construction_type import RecordAdditionalModelConstructionType
    from ..models.record_id_simple_model import RecordIdSimpleModel


T = TypeVar("T", bound="RecordAdditionalModel")


@_attrs_define
class RecordAdditionalModel:
    """
    Attributes:
        building_count (Union[Unset, int]): The number of buildings associated with the record.
        construction_type (Union[Unset, RecordAdditionalModelConstructionType]): The US Census Bureau construction type
            code.
        estimated_value (Union[Unset, float]): The application's estimated value.
        house_unit (Union[Unset, int]): The house unit associated with the application.
        public_owned (Union[Unset, str]): A flag that indicates whether or not the public owns the item.
        record_id (Union[Unset, RecordIdSimpleModel]):
    """

    building_count: Union[Unset, int] = UNSET
    construction_type: Union[Unset, "RecordAdditionalModelConstructionType"] = UNSET
    estimated_value: Union[Unset, float] = UNSET
    house_unit: Union[Unset, int] = UNSET
    public_owned: Union[Unset, str] = UNSET
    record_id: Union[Unset, "RecordIdSimpleModel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        building_count = self.building_count
        construction_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.construction_type, Unset):
            construction_type = self.construction_type.to_dict()

        estimated_value = self.estimated_value
        house_unit = self.house_unit
        public_owned = self.public_owned
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if building_count is not UNSET:
            field_dict["buildingCount"] = building_count
        if construction_type is not UNSET:
            field_dict["constructionType"] = construction_type
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if house_unit is not UNSET:
            field_dict["houseUnit"] = house_unit
        if public_owned is not UNSET:
            field_dict["publicOwned"] = public_owned
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_additional_model_construction_type import RecordAdditionalModelConstructionType
        from ..models.record_id_simple_model import RecordIdSimpleModel

        d = src_dict.copy()
        building_count = d.pop("buildingCount", UNSET)

        _construction_type = d.pop("constructionType", UNSET)
        construction_type: Union[Unset, RecordAdditionalModelConstructionType]
        if isinstance(_construction_type, Unset):
            construction_type = UNSET
        else:
            construction_type = RecordAdditionalModelConstructionType.from_dict(_construction_type)

        estimated_value = d.pop("estimatedValue", UNSET)

        house_unit = d.pop("houseUnit", UNSET)

        public_owned = d.pop("publicOwned", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdSimpleModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdSimpleModel.from_dict(_record_id)

        record_additional_model = cls(
            building_count=building_count,
            construction_type=construction_type,
            estimated_value=estimated_value,
            house_unit=house_unit,
            public_owned=public_owned,
            record_id=record_id,
        )

        record_additional_model.additional_properties = d
        return record_additional_model

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
