from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_model_display_on_inspection import CommentModelDisplayOnInspection
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentModel")


@_attrs_define
class CommentModel:
    """
    Attributes:
        display_on_inspection (Union[Unset, CommentModelDisplayOnInspection]): Indicates whether or not the comment is
            displayed on inspection.
        text (Union[Unset, str]): The comment text.
    """

    display_on_inspection: Union[Unset, CommentModelDisplayOnInspection] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_on_inspection: Union[Unset, str] = UNSET
        if not isinstance(self.display_on_inspection, Unset):
            display_on_inspection = self.display_on_inspection.value

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_on_inspection is not UNSET:
            field_dict["displayOnInspection"] = display_on_inspection
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _display_on_inspection = d.pop("displayOnInspection", UNSET)
        display_on_inspection: Union[Unset, CommentModelDisplayOnInspection]
        if isinstance(_display_on_inspection, Unset):
            display_on_inspection = UNSET
        else:
            display_on_inspection = CommentModelDisplayOnInspection(_display_on_inspection)

        text = d.pop("text", UNSET)

        comment_model = cls(
            display_on_inspection=display_on_inspection,
            text=text,
        )

        comment_model.additional_properties = d
        return comment_model

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
