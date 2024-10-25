import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="WorkflowTaskCommentModel")


@_attrs_define
class WorkflowTaskCommentModel:
    """
    Attributes:
        action (Union[Unset, str]): Audit trail action type like 'payment allocation'
        created_by (Union[Unset, str]): The unique user id of the individual that created the entry.
        created_date (Union[Unset, datetime.datetime]): The date the entry was created.
        record_id (Union[Unset, RecordIdModel]):
        text (Union[Unset, str]): The comment text.
        workflow_task_id (Union[Unset, str]): The id of the workflow task.
    """

    action: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    text: Union[Unset, str] = UNSET
    workflow_task_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action
        created_by = self.created_by
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        text = self.text
        workflow_task_id = self.workflow_task_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if text is not UNSET:
            field_dict["text"] = text
        if workflow_task_id is not UNSET:
            field_dict["workflowTaskId"] = workflow_task_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        created_by = d.pop("createdBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        text = d.pop("text", UNSET)

        workflow_task_id = d.pop("workflowTaskId", UNSET)

        workflow_task_comment_model = cls(
            action=action,
            created_by=created_by,
            created_date=created_date,
            record_id=record_id,
            text=text,
            workflow_task_id=workflow_task_id,
        )

        workflow_task_comment_model.additional_properties = d
        return workflow_task_comment_model

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
