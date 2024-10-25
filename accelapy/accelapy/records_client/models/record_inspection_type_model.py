from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_type_model import InspectionTypeModel


T = TypeVar("T", bound="RecordInspectionTypeModel")


@_attrs_define
class RecordInspectionTypeModel:
    """
    Attributes:
        inspection_types (Union[Unset, List['InspectionTypeModel']]):
        record_id (Union[Unset, str]): The unique ID associated with a record.
    """

    inspection_types: Union[Unset, List["InspectionTypeModel"]] = UNSET
    record_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inspection_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inspection_types, Unset):
            inspection_types = []
            for inspection_types_item_data in self.inspection_types:
                inspection_types_item = inspection_types_item_data.to_dict()

                inspection_types.append(inspection_types_item)

        record_id = self.record_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inspection_types is not UNSET:
            field_dict["inspectionTypes"] = inspection_types
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inspection_type_model import InspectionTypeModel

        d = src_dict.copy()
        inspection_types = []
        _inspection_types = d.pop("inspectionTypes", UNSET)
        for inspection_types_item_data in _inspection_types or []:
            inspection_types_item = InspectionTypeModel.from_dict(inspection_types_item_data)

            inspection_types.append(inspection_types_item)

        record_id = d.pop("recordId", UNSET)

        record_inspection_type_model = cls(
            inspection_types=inspection_types,
            record_id=record_id,
        )

        record_inspection_type_model.additional_properties = d
        return record_inspection_type_model

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
