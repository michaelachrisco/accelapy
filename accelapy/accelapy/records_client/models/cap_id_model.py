from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapIDModel")


@_attrs_define
class CapIDModel:
    """
    Attributes:
        custom_id (Union[Unset, str]):
        id (Union[Unset, str]):
        service_provider_code (Union[Unset, str]):
        tracking_id (Union[Unset, int]):
        value (Union[Unset, str]):
    """

    custom_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    tracking_id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_id = self.custom_id
        id = self.id
        service_provider_code = self.service_provider_code
        tracking_id = self.tracking_id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if id is not UNSET:
            field_dict["id"] = id
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if tracking_id is not UNSET:
            field_dict["trackingId"] = tracking_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_id = d.pop("customId", UNSET)

        id = d.pop("id", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        tracking_id = d.pop("trackingId", UNSET)

        value = d.pop("value", UNSET)

        cap_id_model = cls(
            custom_id=custom_id,
            id=id,
            service_provider_code=service_provider_code,
            tracking_id=tracking_id,
            value=value,
        )

        cap_id_model.additional_properties = d
        return cap_id_model

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
