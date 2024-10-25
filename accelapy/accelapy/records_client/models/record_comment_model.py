import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.record_comment_model_display_on_inspection import RecordCommentModelDisplayOnInspection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="RecordCommentModel")


@_attrs_define
class RecordCommentModel:
    """
    Attributes:
        created_by (Union[Unset, str]): The user who added the record comment.
        created_date (Union[Unset, datetime.datetime]): The date when the record comment was added.
        display_on_inspection (Union[Unset, RecordCommentModelDisplayOnInspection]): Indicates whether or not the
            comment is displayed on inspection.
        id (Union[Unset, int]): The comment system id assigned by the Civic Platform server.
        record_id (Union[Unset, RecordIdModel]):
        text (Union[Unset, str]): The comment text.
    """

    created_by: Union[Unset, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    display_on_inspection: Union[Unset, RecordCommentModelDisplayOnInspection] = UNSET
    id: Union[Unset, int] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_by = self.created_by
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        display_on_inspection: Union[Unset, str] = UNSET
        if not isinstance(self.display_on_inspection, Unset):
            display_on_inspection = self.display_on_inspection.value

        id = self.id
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if display_on_inspection is not UNSET:
            field_dict["displayOnInspection"] = display_on_inspection
        if id is not UNSET:
            field_dict["id"] = id
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        created_by = d.pop("createdBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _display_on_inspection = d.pop("displayOnInspection", UNSET)
        display_on_inspection: Union[Unset, RecordCommentModelDisplayOnInspection]
        if isinstance(_display_on_inspection, Unset):
            display_on_inspection = UNSET
        else:
            display_on_inspection = RecordCommentModelDisplayOnInspection(_display_on_inspection)

        id = d.pop("id", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        text = d.pop("text", UNSET)

        record_comment_model = cls(
            created_by=created_by,
            created_date=created_date,
            display_on_inspection=display_on_inspection,
            id=id,
            record_id=record_id,
            text=text,
        )

        record_comment_model.additional_properties = d
        return record_comment_model

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
