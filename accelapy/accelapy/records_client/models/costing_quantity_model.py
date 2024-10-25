from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostingQuantityModel")


@_attrs_define
class CostingQuantityModel:
    """
    Attributes:
        factor (Union[Unset, float]): The cost factor.
        minutes (Union[Unset, float]): The number of minutes associated to the cost.
    """

    factor: Union[Unset, float] = UNSET
    minutes: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        factor = self.factor
        minutes = self.minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if factor is not UNSET:
            field_dict["factor"] = factor
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        factor = d.pop("factor", UNSET)

        minutes = d.pop("minutes", UNSET)

        costing_quantity_model = cls(
            factor=factor,
            minutes=minutes,
        )

        costing_quantity_model.additional_properties = d
        return costing_quantity_model

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
