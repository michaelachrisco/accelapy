from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseError")


@_attrs_define
class ResponseError:
    """
    Attributes:
        error (Union[Unset, str]): The error code. Refer [here](https://tools.ietf.org/html/rfc6749#section-4.1.2) for
            details.
        error_description (Union[Unset, str]): The error description text.
        error_uri (Union[Unset, str]): The URI of web page with more information about the error.
        state (Union[Unset, str]): The exact value received from the client.
    """

    error: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    error_uri: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        error_description = self.error_description
        error_uri = self.error_uri
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_uri is not UNSET:
            field_dict["error_uri"] = error_uri
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        error_description = d.pop("error_description", UNSET)

        error_uri = d.pop("error_uri", UNSET)

        state = d.pop("state", UNSET)

        response_error = cls(
            error=error,
            error_description=error_description,
            error_uri=error_uri,
            state=state,
        )

        response_error.additional_properties = d
        return response_error

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
