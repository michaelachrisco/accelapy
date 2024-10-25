import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_item_action_model_billable import TaskItemActionModelBillable
from ..models.task_item_action_model_is_active import TaskItemActionModelIsActive
from ..models.task_item_action_model_is_completed import TaskItemActionModelIsCompleted
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_id_model import RecordIdModel
    from ..models.task_item_action_model_actionby_department import TaskItemActionModelActionbyDepartment
    from ..models.task_item_action_model_actionby_user import TaskItemActionModelActionbyUser
    from ..models.task_item_action_model_assigned_to_department import TaskItemActionModelAssignedToDepartment
    from ..models.task_item_action_model_assigned_user import TaskItemActionModelAssignedUser
    from ..models.task_item_action_model_status import TaskItemActionModelStatus


T = TypeVar("T", bound="TaskItemActionModel")


@_attrs_define
class TaskItemActionModel:
    """
    Attributes:
        action (Union[Unset, str]): Audit trail action type like "payment allocation"
        actionby_department (Union[Unset, TaskItemActionModelActionbyDepartment]): The department responsible for the
            action.
        actionby_user (Union[Unset, TaskItemActionModelActionbyUser]): The individual responsible for the action.
        approval (Union[Unset, str]): Used to indicate supervisory approval of an adhoc task.
        assign_email_display (Union[Unset, str]): Indicates whether or not to display the agency employeeâ€™s email
            address in ACA. Public users can then click the e-mail hyperlink and send an e-mail to the agency employee.
            â€œYâ€ : display the email address. â€œNâ€ : hide the email address.
        assigned_date (Union[Unset, datetime.datetime]): The date of the assigned action.
        assigned_to_department (Union[Unset, TaskItemActionModelAssignedToDepartment]): The department responsible for
            the action.
        assigned_user (Union[Unset, TaskItemActionModelAssignedUser]): The staff member responsible for the action.
        billable (Union[Unset, TaskItemActionModelBillable]): Indicates whether or not the item is billable.
        comment (Union[Unset, str]): Comments or notes about the current context.
        comment_display (Union[Unset, str]): Indicates whether or not Accela Citizen Access users can view the
            inspection results comments.
        comment_public_visible (Union[Unset, List[str]]): Specifies the type of user who can view the inspection result
            comments. <br/>"All ACA Users" - Both registered and anonymous Accela Citizen Access users can view the comments
            for inspection results. <br/>"Record Creator Only" - the user who created the record can see the comments for
            the inspection results. <br/>"Record Creator and Licensed Professional" - The user who created the record and
            the licensed professional associated with the record can see the comments for the inspection results.
        current_task_id (Union[Unset, str]): The ID of the current workflow task.
        days_due (Union[Unset, int]): The amount of time to complete a task (measured in days).
        description (Union[Unset, str]): The description of the record or item.
        disposition_note (Union[Unset, str]): A note describing the disposition of the current task.
        due_date (Union[Unset, datetime.datetime]): The desired completion date of the task.
        end_time (Union[Unset, datetime.datetime]): The time the workflow task was completed.
        estimated_due_date (Union[Unset, datetime.datetime]): The estimated date of completion.
        estimated_hours (Union[Unset, float]): The estimated hours necessary to complete this task.
        hours_spent (Union[Unset, float]): Number of hours used for a workflow or workflow task.
        id (Union[Unset, str]): The workflow task system id assigned by the Civic Platform server.
        in_possession_time (Union[Unset, float]): The application level in possession time of the time tracking feature.
        is_active (Union[Unset, TaskItemActionModelIsActive]): Indicates whether or not the workflow task is active.
        is_completed (Union[Unset, TaskItemActionModelIsCompleted]): Indicates whether or not the workflow task is
            completed.
        last_modified_date (Union[Unset, datetime.datetime]): The date when the task item was last changed.
        last_modified_date_string (Union[Unset, str]): A string represents the date when the task item was last changed.
        next_task_id (Union[Unset, str]): The id of the next task in a workflow.
        over_time (Union[Unset, str]): A labor cost factor that indicates time worked beyond a worker's regular working
            hours.
        process_code (Union[Unset, str]): The process code for the next task in a workflow.
        record_id (Union[Unset, RecordIdModel]):
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        start_time (Union[Unset, datetime.datetime]): The time the workflow task started.
        status (Union[Unset, TaskItemActionModelStatus]): The workflow task status.
        status_date (Union[Unset, datetime.datetime]): The date when the current status changed.
        track_start_date (Union[Unset, datetime.datetime]): The date that time tracking is set to begin.
    """

    action: Union[Unset, str] = UNSET
    actionby_department: Union[Unset, "TaskItemActionModelActionbyDepartment"] = UNSET
    actionby_user: Union[Unset, "TaskItemActionModelActionbyUser"] = UNSET
    approval: Union[Unset, str] = UNSET
    assign_email_display: Union[Unset, str] = UNSET
    assigned_date: Union[Unset, datetime.datetime] = UNSET
    assigned_to_department: Union[Unset, "TaskItemActionModelAssignedToDepartment"] = UNSET
    assigned_user: Union[Unset, "TaskItemActionModelAssignedUser"] = UNSET
    billable: Union[Unset, TaskItemActionModelBillable] = UNSET
    comment: Union[Unset, str] = UNSET
    comment_display: Union[Unset, str] = UNSET
    comment_public_visible: Union[Unset, List[str]] = UNSET
    current_task_id: Union[Unset, str] = UNSET
    days_due: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    disposition_note: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    estimated_due_date: Union[Unset, datetime.datetime] = UNSET
    estimated_hours: Union[Unset, float] = UNSET
    hours_spent: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    in_possession_time: Union[Unset, float] = UNSET
    is_active: Union[Unset, TaskItemActionModelIsActive] = UNSET
    is_completed: Union[Unset, TaskItemActionModelIsCompleted] = UNSET
    last_modified_date: Union[Unset, datetime.datetime] = UNSET
    last_modified_date_string: Union[Unset, str] = UNSET
    next_task_id: Union[Unset, str] = UNSET
    over_time: Union[Unset, str] = UNSET
    process_code: Union[Unset, str] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, "TaskItemActionModelStatus"] = UNSET
    status_date: Union[Unset, datetime.datetime] = UNSET
    track_start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action
        actionby_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionby_department, Unset):
            actionby_department = self.actionby_department.to_dict()

        actionby_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionby_user, Unset):
            actionby_user = self.actionby_user.to_dict()

        approval = self.approval
        assign_email_display = self.assign_email_display
        assigned_date: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_date, Unset):
            assigned_date = self.assigned_date.isoformat()

        assigned_to_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to_department, Unset):
            assigned_to_department = self.assigned_to_department.to_dict()

        assigned_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_user, Unset):
            assigned_user = self.assigned_user.to_dict()

        billable: Union[Unset, str] = UNSET
        if not isinstance(self.billable, Unset):
            billable = self.billable.value

        comment = self.comment
        comment_display = self.comment_display
        comment_public_visible: Union[Unset, List[str]] = UNSET
        if not isinstance(self.comment_public_visible, Unset):
            comment_public_visible = self.comment_public_visible

        current_task_id = self.current_task_id
        days_due = self.days_due
        description = self.description
        disposition_note = self.disposition_note
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        estimated_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_due_date, Unset):
            estimated_due_date = self.estimated_due_date.isoformat()

        estimated_hours = self.estimated_hours
        hours_spent = self.hours_spent
        id = self.id
        in_possession_time = self.in_possession_time
        is_active: Union[Unset, str] = UNSET
        if not isinstance(self.is_active, Unset):
            is_active = self.is_active.value

        is_completed: Union[Unset, str] = UNSET
        if not isinstance(self.is_completed, Unset):
            is_completed = self.is_completed.value

        last_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_date, Unset):
            last_modified_date = self.last_modified_date.isoformat()

        last_modified_date_string = self.last_modified_date_string
        next_task_id = self.next_task_id
        over_time = self.over_time
        process_code = self.process_code
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        service_provider_code = self.service_provider_code
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        track_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.track_start_date, Unset):
            track_start_date = self.track_start_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if actionby_department is not UNSET:
            field_dict["actionbyDepartment"] = actionby_department
        if actionby_user is not UNSET:
            field_dict["actionbyUser"] = actionby_user
        if approval is not UNSET:
            field_dict["approval"] = approval
        if assign_email_display is not UNSET:
            field_dict["assignEmailDisplay"] = assign_email_display
        if assigned_date is not UNSET:
            field_dict["assignedDate"] = assigned_date
        if assigned_to_department is not UNSET:
            field_dict["assignedToDepartment"] = assigned_to_department
        if assigned_user is not UNSET:
            field_dict["assignedUser"] = assigned_user
        if billable is not UNSET:
            field_dict["billable"] = billable
        if comment is not UNSET:
            field_dict["comment"] = comment
        if comment_display is not UNSET:
            field_dict["commentDisplay"] = comment_display
        if comment_public_visible is not UNSET:
            field_dict["commentPublicVisible"] = comment_public_visible
        if current_task_id is not UNSET:
            field_dict["currentTaskId"] = current_task_id
        if days_due is not UNSET:
            field_dict["daysDue"] = days_due
        if description is not UNSET:
            field_dict["description"] = description
        if disposition_note is not UNSET:
            field_dict["dispositionNote"] = disposition_note
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if estimated_due_date is not UNSET:
            field_dict["estimatedDueDate"] = estimated_due_date
        if estimated_hours is not UNSET:
            field_dict["estimatedHours"] = estimated_hours
        if hours_spent is not UNSET:
            field_dict["hoursSpent"] = hours_spent
        if id is not UNSET:
            field_dict["id"] = id
        if in_possession_time is not UNSET:
            field_dict["inPossessionTime"] = in_possession_time
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date
        if last_modified_date_string is not UNSET:
            field_dict["lastModifiedDateString"] = last_modified_date_string
        if next_task_id is not UNSET:
            field_dict["nextTaskId"] = next_task_id
        if over_time is not UNSET:
            field_dict["overTime"] = over_time
        if process_code is not UNSET:
            field_dict["processCode"] = process_code
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if status_date is not UNSET:
            field_dict["statusDate"] = status_date
        if track_start_date is not UNSET:
            field_dict["trackStartDate"] = track_start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_id_model import RecordIdModel
        from ..models.task_item_action_model_actionby_department import TaskItemActionModelActionbyDepartment
        from ..models.task_item_action_model_actionby_user import TaskItemActionModelActionbyUser
        from ..models.task_item_action_model_assigned_to_department import TaskItemActionModelAssignedToDepartment
        from ..models.task_item_action_model_assigned_user import TaskItemActionModelAssignedUser
        from ..models.task_item_action_model_status import TaskItemActionModelStatus

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        _actionby_department = d.pop("actionbyDepartment", UNSET)
        actionby_department: Union[Unset, TaskItemActionModelActionbyDepartment]
        if isinstance(_actionby_department, Unset):
            actionby_department = UNSET
        else:
            actionby_department = TaskItemActionModelActionbyDepartment.from_dict(_actionby_department)

        _actionby_user = d.pop("actionbyUser", UNSET)
        actionby_user: Union[Unset, TaskItemActionModelActionbyUser]
        if isinstance(_actionby_user, Unset):
            actionby_user = UNSET
        else:
            actionby_user = TaskItemActionModelActionbyUser.from_dict(_actionby_user)

        approval = d.pop("approval", UNSET)

        assign_email_display = d.pop("assignEmailDisplay", UNSET)

        _assigned_date = d.pop("assignedDate", UNSET)
        assigned_date: Union[Unset, datetime.datetime]
        if isinstance(_assigned_date, Unset):
            assigned_date = UNSET
        else:
            assigned_date = isoparse(_assigned_date)

        _assigned_to_department = d.pop("assignedToDepartment", UNSET)
        assigned_to_department: Union[Unset, TaskItemActionModelAssignedToDepartment]
        if isinstance(_assigned_to_department, Unset):
            assigned_to_department = UNSET
        else:
            assigned_to_department = TaskItemActionModelAssignedToDepartment.from_dict(_assigned_to_department)

        _assigned_user = d.pop("assignedUser", UNSET)
        assigned_user: Union[Unset, TaskItemActionModelAssignedUser]
        if isinstance(_assigned_user, Unset):
            assigned_user = UNSET
        else:
            assigned_user = TaskItemActionModelAssignedUser.from_dict(_assigned_user)

        _billable = d.pop("billable", UNSET)
        billable: Union[Unset, TaskItemActionModelBillable]
        if isinstance(_billable, Unset):
            billable = UNSET
        else:
            billable = TaskItemActionModelBillable(_billable)

        comment = d.pop("comment", UNSET)

        comment_display = d.pop("commentDisplay", UNSET)

        comment_public_visible = cast(List[str], d.pop("commentPublicVisible", UNSET))

        current_task_id = d.pop("currentTaskId", UNSET)

        days_due = d.pop("daysDue", UNSET)

        description = d.pop("description", UNSET)

        disposition_note = d.pop("dispositionNote", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _estimated_due_date = d.pop("estimatedDueDate", UNSET)
        estimated_due_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_due_date, Unset):
            estimated_due_date = UNSET
        else:
            estimated_due_date = isoparse(_estimated_due_date)

        estimated_hours = d.pop("estimatedHours", UNSET)

        hours_spent = d.pop("hoursSpent", UNSET)

        id = d.pop("id", UNSET)

        in_possession_time = d.pop("inPossessionTime", UNSET)

        _is_active = d.pop("isActive", UNSET)
        is_active: Union[Unset, TaskItemActionModelIsActive]
        if isinstance(_is_active, Unset):
            is_active = UNSET
        else:
            is_active = TaskItemActionModelIsActive(_is_active)

        _is_completed = d.pop("isCompleted", UNSET)
        is_completed: Union[Unset, TaskItemActionModelIsCompleted]
        if isinstance(_is_completed, Unset):
            is_completed = UNSET
        else:
            is_completed = TaskItemActionModelIsCompleted(_is_completed)

        _last_modified_date = d.pop("lastModifiedDate", UNSET)
        last_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_date, Unset):
            last_modified_date = UNSET
        else:
            last_modified_date = isoparse(_last_modified_date)

        last_modified_date_string = d.pop("lastModifiedDateString", UNSET)

        next_task_id = d.pop("nextTaskId", UNSET)

        over_time = d.pop("overTime", UNSET)

        process_code = d.pop("processCode", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, TaskItemActionModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskItemActionModelStatus.from_dict(_status)

        _status_date = d.pop("statusDate", UNSET)
        status_date: Union[Unset, datetime.datetime]
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        _track_start_date = d.pop("trackStartDate", UNSET)
        track_start_date: Union[Unset, datetime.datetime]
        if isinstance(_track_start_date, Unset):
            track_start_date = UNSET
        else:
            track_start_date = isoparse(_track_start_date)

        task_item_action_model = cls(
            action=action,
            actionby_department=actionby_department,
            actionby_user=actionby_user,
            approval=approval,
            assign_email_display=assign_email_display,
            assigned_date=assigned_date,
            assigned_to_department=assigned_to_department,
            assigned_user=assigned_user,
            billable=billable,
            comment=comment,
            comment_display=comment_display,
            comment_public_visible=comment_public_visible,
            current_task_id=current_task_id,
            days_due=days_due,
            description=description,
            disposition_note=disposition_note,
            due_date=due_date,
            end_time=end_time,
            estimated_due_date=estimated_due_date,
            estimated_hours=estimated_hours,
            hours_spent=hours_spent,
            id=id,
            in_possession_time=in_possession_time,
            is_active=is_active,
            is_completed=is_completed,
            last_modified_date=last_modified_date,
            last_modified_date_string=last_modified_date_string,
            next_task_id=next_task_id,
            over_time=over_time,
            process_code=process_code,
            record_id=record_id,
            service_provider_code=service_provider_code,
            start_time=start_time,
            status=status,
            status_date=status_date,
            track_start_date=track_start_date,
        )

        task_item_action_model.additional_properties = d
        return task_item_action_model

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
