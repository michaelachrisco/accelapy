from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseStatus")


@_attrs_define
class ResponseStatus:
    """
    Attributes:
        status (Union[Unset, str]): The HTTP error code.
        code (Union[Unset, str]): The error code.
        message (Union[Unset, str]): The error message.
        trace_id (Union[Unset, str]): The traceid for debugging purposes.
    """

    status: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    trace_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        code = self.code
        message = self.message
        trace_id = self.trace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        trace_id = d.pop("traceId", UNSET)

        response_status = cls(
            status=status,
            code=code,
            message=message,
            trace_id=trace_id,
        )

        response_status.additional_properties = d
        return response_status

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
