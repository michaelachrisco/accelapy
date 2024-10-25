from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_type_associations_model_standard_comment_group import (
        InspectionTypeAssociationsModelStandardCommentGroup,
    )


T = TypeVar("T", bound="InspectionTypeAssociationsModel")


@_attrs_define
class InspectionTypeAssociationsModel:
    """
    Attributes:
        standard_comment_group (Union[Unset, InspectionTypeAssociationsModelStandardCommentGroup]): The name of the
            standard comment group associated with the inspection type.
    """

    standard_comment_group: Union[Unset, "InspectionTypeAssociationsModelStandardCommentGroup"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        standard_comment_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_comment_group, Unset):
            standard_comment_group = self.standard_comment_group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if standard_comment_group is not UNSET:
            field_dict["standardCommentGroup"] = standard_comment_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inspection_type_associations_model_standard_comment_group import (
            InspectionTypeAssociationsModelStandardCommentGroup,
        )

        d = src_dict.copy()
        _standard_comment_group = d.pop("standardCommentGroup", UNSET)
        standard_comment_group: Union[Unset, InspectionTypeAssociationsModelStandardCommentGroup]
        if isinstance(_standard_comment_group, Unset):
            standard_comment_group = UNSET
        else:
            standard_comment_group = InspectionTypeAssociationsModelStandardCommentGroup.from_dict(
                _standard_comment_group
            )

        inspection_type_associations_model = cls(
            standard_comment_group=standard_comment_group,
        )

        inspection_type_associations_model.additional_properties = d
        return inspection_type_associations_model

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
