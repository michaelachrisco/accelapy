from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EstimateFeeModel")


@_attrs_define
class EstimateFeeModel:
    """
    Attributes:
        currency_code (Union[Unset, str]): The standard ISO 4217 currency code. For example, "USD" for US Dollars
        fee_total (Union[Unset, float]): The total fee.
    """

    currency_code: Union[Unset, str] = UNSET
    fee_total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code
        fee_total = self.fee_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if fee_total is not UNSET:
            field_dict["feeTotal"] = fee_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = d.pop("currencyCode", UNSET)

        fee_total = d.pop("feeTotal", UNSET)

        estimate_fee_model = cls(
            currency_code=currency_code,
            fee_total=fee_total,
        )

        estimate_fee_model.additional_properties = d
        return estimate_fee_model

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
