from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordIdModel")


@_attrs_define
class RecordIdModel:
    """
    Attributes:
        custom_id (Union[Unset, str]): An ID based on a different numbering convention from the numbering convention
            used by the record ID (xxxxx-xx-xxxxx). Accela Automation auto-generates and applies an alternate ID value when
            you submit a new application.
        id (Union[Unset, str]): The record system id assigned by the Civic Platform server.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        tracking_id (Union[Unset, int]): The application tracking number (IVR tracking number).
        value (Union[Unset, str]): The alphanumeric record id.
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

        record_id_model = cls(
            custom_id=custom_id,
            id=id,
            service_provider_code=service_provider_code,
            tracking_id=tracking_id,
            value=value,
        )

        record_id_model.additional_properties = d
        return record_id_model

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
