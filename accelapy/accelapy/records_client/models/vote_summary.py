from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoteSummary")


@_attrs_define
class VoteSummary:
    """
    Attributes:
        down_count (Union[Unset, int]): The number of votes that disapprove the specified record.
        up_count (Union[Unset, int]): The number of votes that approve the specified record.
    """

    down_count: Union[Unset, int] = UNSET
    up_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        down_count = self.down_count
        up_count = self.up_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if down_count is not UNSET:
            field_dict["downCount"] = down_count
        if up_count is not UNSET:
            field_dict["upCount"] = up_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        down_count = d.pop("downCount", UNSET)

        up_count = d.pop("upCount", UNSET)

        vote_summary = cls(
            down_count=down_count,
            up_count=up_count,
        )

        vote_summary.additional_properties = d
        return vote_summary

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
