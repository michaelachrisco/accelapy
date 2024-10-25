from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GISObjectModel")


@_attrs_define
class GISObjectModel:
    """
    Attributes:
        gis_id (Union[Unset, str]): The GIS object id.
        layer_id (Union[Unset, str]): The map layer id.
        service_id (Union[Unset, str]): The map service id.
    """

    gis_id: Union[Unset, str] = UNSET
    layer_id: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gis_id = self.gis_id
        layer_id = self.layer_id
        service_id = self.service_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gis_id is not UNSET:
            field_dict["gisId"] = gis_id
        if layer_id is not UNSET:
            field_dict["layerId"] = layer_id
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gis_id = d.pop("gisId", UNSET)

        layer_id = d.pop("layerId", UNSET)

        service_id = d.pop("serviceId", UNSET)

        gis_object_model = cls(
            gis_id=gis_id,
            layer_id=layer_id,
            service_id=service_id,
        )

        gis_object_model.additional_properties = d
        return gis_object_model

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
