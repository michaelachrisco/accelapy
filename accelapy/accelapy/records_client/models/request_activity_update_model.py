import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_activity_update_model_activity_status import RequestActivityUpdateModelActivityStatus
    from ..models.request_activity_update_model_assigned_department import RequestActivityUpdateModelAssignedDepartment
    from ..models.request_activity_update_model_assigned_user import RequestActivityUpdateModelAssignedUser
    from ..models.request_activity_update_model_priority import RequestActivityUpdateModelPriority
    from ..models.request_activity_update_model_status import RequestActivityUpdateModelStatus
    from ..models.request_activity_update_model_type import RequestActivityUpdateModelType


T = TypeVar("T", bound="RequestActivityUpdateModel")


@_attrs_define
class RequestActivityUpdateModel:
    """
    Attributes:
        activity_status (Union[Unset, RequestActivityUpdateModelActivityStatus]): The status of the record activity.
        assigned_department (Union[Unset, RequestActivityUpdateModelAssignedDepartment]): The department responsible for
            the activity.
        assigned_user (Union[Unset, RequestActivityUpdateModelAssignedUser]): The staff member responsible for the
            activity.
        description (Union[Unset, str]): The activity description
        due_date (Union[Unset, datetime.datetime]): The desired completion date of the task.
        name (Union[Unset, str]): The activity name.
        priority (Union[Unset, RequestActivityUpdateModelPriority]): The priority level assigned to the activity.
        start_date (Union[Unset, datetime.datetime]): The activity start date.
        status (Union[Unset, RequestActivityUpdateModelStatus]): The activity status.
        type (Union[Unset, RequestActivityUpdateModelType]): The activity type.
    """

    activity_status: Union[Unset, "RequestActivityUpdateModelActivityStatus"] = UNSET
    assigned_department: Union[Unset, "RequestActivityUpdateModelAssignedDepartment"] = UNSET
    assigned_user: Union[Unset, "RequestActivityUpdateModelAssignedUser"] = UNSET
    description: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    priority: Union[Unset, "RequestActivityUpdateModelPriority"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, "RequestActivityUpdateModelStatus"] = UNSET
    type: Union[Unset, "RequestActivityUpdateModelType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity_status, Unset):
            activity_status = self.activity_status.to_dict()

        assigned_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_department, Unset):
            assigned_department = self.assigned_department.to_dict()

        assigned_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_user, Unset):
            assigned_user = self.assigned_user.to_dict()

        description = self.description
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        name = self.name
        priority: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_status is not UNSET:
            field_dict["activityStatus"] = activity_status
        if assigned_department is not UNSET:
            field_dict["assignedDepartment"] = assigned_department
        if assigned_user is not UNSET:
            field_dict["assignedUser"] = assigned_user
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.request_activity_update_model_activity_status import RequestActivityUpdateModelActivityStatus
        from ..models.request_activity_update_model_assigned_department import (
            RequestActivityUpdateModelAssignedDepartment,
        )
        from ..models.request_activity_update_model_assigned_user import RequestActivityUpdateModelAssignedUser
        from ..models.request_activity_update_model_priority import RequestActivityUpdateModelPriority
        from ..models.request_activity_update_model_status import RequestActivityUpdateModelStatus
        from ..models.request_activity_update_model_type import RequestActivityUpdateModelType

        d = src_dict.copy()
        _activity_status = d.pop("activityStatus", UNSET)
        activity_status: Union[Unset, RequestActivityUpdateModelActivityStatus]
        if isinstance(_activity_status, Unset):
            activity_status = UNSET
        else:
            activity_status = RequestActivityUpdateModelActivityStatus.from_dict(_activity_status)

        _assigned_department = d.pop("assignedDepartment", UNSET)
        assigned_department: Union[Unset, RequestActivityUpdateModelAssignedDepartment]
        if isinstance(_assigned_department, Unset):
            assigned_department = UNSET
        else:
            assigned_department = RequestActivityUpdateModelAssignedDepartment.from_dict(_assigned_department)

        _assigned_user = d.pop("assignedUser", UNSET)
        assigned_user: Union[Unset, RequestActivityUpdateModelAssignedUser]
        if isinstance(_assigned_user, Unset):
            assigned_user = UNSET
        else:
            assigned_user = RequestActivityUpdateModelAssignedUser.from_dict(_assigned_user)

        description = d.pop("description", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        name = d.pop("name", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, RequestActivityUpdateModelPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = RequestActivityUpdateModelPriority.from_dict(_priority)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RequestActivityUpdateModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestActivityUpdateModelStatus.from_dict(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RequestActivityUpdateModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RequestActivityUpdateModelType.from_dict(_type)

        request_activity_update_model = cls(
            activity_status=activity_status,
            assigned_department=assigned_department,
            assigned_user=assigned_user,
            description=description,
            due_date=due_date,
            name=name,
            priority=priority,
            start_date=start_date,
            status=status,
            type=type,
        )

        request_activity_update_model.additional_properties = d
        return request_activity_update_model

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
