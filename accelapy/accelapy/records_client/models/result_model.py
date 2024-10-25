from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultModel")


@_attrs_define
class ResultModel:
    """
    Attributes:
        code (Union[Unset, str]): The error code, if an error is encountered.
        id (Union[Unset, int]): The system id of the object in this operation.
        is_success (Union[Unset, bool]): Indicates whether or not the operation on the object is successful.
        message (Union[Unset, str]): The error message, if an error is encountered
    """

    code: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_success: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        id = self.id
        is_success = self.is_success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if is_success is not UNSET:
            field_dict["isSuccess"] = is_success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        is_success = d.pop("isSuccess", UNSET)

        message = d.pop("message", UNSET)

        result_model = cls(
            code=code,
            id=id,
            is_success=is_success,
            message=message,
        )

        result_model.additional_properties = d
        return result_model

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
