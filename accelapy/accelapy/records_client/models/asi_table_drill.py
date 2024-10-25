from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.child_drill import ChildDrill


T = TypeVar("T", bound="ASITableDrill")


@_attrs_define
class ASITableDrill:
    """
    Attributes:
        children (Union[Unset, List['ChildDrill']]):
        is_root (Union[Unset, bool]):
    """

    children: Union[Unset, List["ChildDrill"]] = UNSET
    is_root: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()

                children.append(children_item)

        is_root = self.is_root

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if is_root is not UNSET:
            field_dict["isRoot"] = is_root

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.child_drill import ChildDrill

        d = src_dict.copy()
        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = ChildDrill.from_dict(children_item_data)

            children.append(children_item)

        is_root = d.pop("isRoot", UNSET)

        asi_table_drill = cls(
            children=children,
            is_root=is_root,
        )

        asi_table_drill.additional_properties = d
        return asi_table_drill

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
