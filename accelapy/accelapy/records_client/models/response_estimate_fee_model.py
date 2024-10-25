from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimate_fee_model import EstimateFeeModel


T = TypeVar("T", bound="ResponseEstimateFeeModel")


@_attrs_define
class ResponseEstimateFeeModel:
    """
    Attributes:
        result (Union[Unset, EstimateFeeModel]):
        status (Union[Unset, int]): The HTTP return status.
    """

    result: Union[Unset, "EstimateFeeModel"] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.estimate_fee_model import EstimateFeeModel

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, EstimateFeeModel]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = EstimateFeeModel.from_dict(_result)

        status = d.pop("status", UNSET)

        response_estimate_fee_model = cls(
            result=result,
            status=status,
        )

        response_estimate_fee_model.additional_properties = d
        return response_estimate_fee_model

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
