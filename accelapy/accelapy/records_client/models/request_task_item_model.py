import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.request_task_item_model_billable import RequestTaskItemModelBillable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_task_item_model_actionby_department import RequestTaskItemModelActionbyDepartment
    from ..models.request_task_item_model_actionby_user import RequestTaskItemModelActionbyUser
    from ..models.request_task_item_model_status import RequestTaskItemModelStatus


T = TypeVar("T", bound="RequestTaskItemModel")


@_attrs_define
class RequestTaskItemModel:
    """
    Attributes:
        actionby_department (Union[Unset, RequestTaskItemModelActionbyDepartment]): The department responsible for the
            action.
        actionby_user (Union[Unset, RequestTaskItemModelActionbyUser]): The individual responsible for the action.
        approval (Union[Unset, str]): Used to indicate supervisory approval of an adhoc task.
        assign_email_display (Union[Unset, str]): Indicates whether or not to display the agency employeeâ€™s email
            address in ACA. Public users can then click the e-mail hyperlink and send an e-mail to the agency employee.
            â€œYâ€ : display the email address. â€œNâ€ : hide the email address.
        billable (Union[Unset, RequestTaskItemModelBillable]): Indicates whether or not the item is billable.
        comment (Union[Unset, str]): Comments or notes about the current context.
        comment_display (Union[Unset, str]): Indicates whether or not Accela Citizen Access users can view the
            inspection results comments.
        comment_public_visible (Union[Unset, List[str]]): Specifies the type of user who can view the inspection result
            comments. <br/>"All ACA Users" - Both registered and anonymous Accela Citizen Access users can view the comments
            for inspection results. <br/>"Record Creator Only" - the user who created the record can see the comments for
            the inspection results. <br/>"Record Creator and Licensed Professional" - The user who created the record and
            the licensed professional associated with the record can see the comments for the inspection results.
        due_date (Union[Unset, datetime.datetime]): The desired completion date of the task.
        end_time (Union[Unset, datetime.datetime]): The time the workflow task was completed.
        hours_spent (Union[Unset, float]): Number of hours used for a workflow or workflow task.
        over_time (Union[Unset, str]): A labor cost factor that indicates time worked beyond a worker's regular working
            hours.
        start_time (Union[Unset, datetime.datetime]): The time the workflow task started.
        status (Union[Unset, RequestTaskItemModelStatus]): The workflow task status.
        status_date (Union[Unset, datetime.datetime]): The date when the current status changed.
    """

    actionby_department: Union[Unset, "RequestTaskItemModelActionbyDepartment"] = UNSET
    actionby_user: Union[Unset, "RequestTaskItemModelActionbyUser"] = UNSET
    approval: Union[Unset, str] = UNSET
    assign_email_display: Union[Unset, str] = UNSET
    billable: Union[Unset, RequestTaskItemModelBillable] = UNSET
    comment: Union[Unset, str] = UNSET
    comment_display: Union[Unset, str] = UNSET
    comment_public_visible: Union[Unset, List[str]] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    hours_spent: Union[Unset, float] = UNSET
    over_time: Union[Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, "RequestTaskItemModelStatus"] = UNSET
    status_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actionby_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionby_department, Unset):
            actionby_department = self.actionby_department.to_dict()

        actionby_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionby_user, Unset):
            actionby_user = self.actionby_user.to_dict()

        approval = self.approval
        assign_email_display = self.assign_email_display
        billable: Union[Unset, str] = UNSET
        if not isinstance(self.billable, Unset):
            billable = self.billable.value

        comment = self.comment
        comment_display = self.comment_display
        comment_public_visible: Union[Unset, List[str]] = UNSET
        if not isinstance(self.comment_public_visible, Unset):
            comment_public_visible = self.comment_public_visible

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        hours_spent = self.hours_spent
        over_time = self.over_time
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actionby_department is not UNSET:
            field_dict["actionbyDepartment"] = actionby_department
        if actionby_user is not UNSET:
            field_dict["actionbyUser"] = actionby_user
        if approval is not UNSET:
            field_dict["approval"] = approval
        if assign_email_display is not UNSET:
            field_dict["assignEmailDisplay"] = assign_email_display
        if billable is not UNSET:
            field_dict["billable"] = billable
        if comment is not UNSET:
            field_dict["comment"] = comment
        if comment_display is not UNSET:
            field_dict["commentDisplay"] = comment_display
        if comment_public_visible is not UNSET:
            field_dict["commentPublicVisible"] = comment_public_visible
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if hours_spent is not UNSET:
            field_dict["hoursSpent"] = hours_spent
        if over_time is not UNSET:
            field_dict["overTime"] = over_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if status_date is not UNSET:
            field_dict["statusDate"] = status_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.request_task_item_model_actionby_department import RequestTaskItemModelActionbyDepartment
        from ..models.request_task_item_model_actionby_user import RequestTaskItemModelActionbyUser
        from ..models.request_task_item_model_status import RequestTaskItemModelStatus

        d = src_dict.copy()
        _actionby_department = d.pop("actionbyDepartment", UNSET)
        actionby_department: Union[Unset, RequestTaskItemModelActionbyDepartment]
        if isinstance(_actionby_department, Unset):
            actionby_department = UNSET
        else:
            actionby_department = RequestTaskItemModelActionbyDepartment.from_dict(_actionby_department)

        _actionby_user = d.pop("actionbyUser", UNSET)
        actionby_user: Union[Unset, RequestTaskItemModelActionbyUser]
        if isinstance(_actionby_user, Unset):
            actionby_user = UNSET
        else:
            actionby_user = RequestTaskItemModelActionbyUser.from_dict(_actionby_user)

        approval = d.pop("approval", UNSET)

        assign_email_display = d.pop("assignEmailDisplay", UNSET)

        _billable = d.pop("billable", UNSET)
        billable: Union[Unset, RequestTaskItemModelBillable]
        if isinstance(_billable, Unset):
            billable = UNSET
        else:
            billable = RequestTaskItemModelBillable(_billable)

        comment = d.pop("comment", UNSET)

        comment_display = d.pop("commentDisplay", UNSET)

        comment_public_visible = cast(List[str], d.pop("commentPublicVisible", UNSET))

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

        hours_spent = d.pop("hoursSpent", UNSET)

        over_time = d.pop("overTime", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RequestTaskItemModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestTaskItemModelStatus.from_dict(_status)

        _status_date = d.pop("statusDate", UNSET)
        status_date: Union[Unset, datetime.datetime]
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        request_task_item_model = cls(
            actionby_department=actionby_department,
            actionby_user=actionby_user,
            approval=approval,
            assign_email_display=assign_email_display,
            billable=billable,
            comment=comment,
            comment_display=comment_display,
            comment_public_visible=comment_public_visible,
            due_date=due_date,
            end_time=end_time,
            hours_spent=hours_spent,
            over_time=over_time,
            start_time=start_time,
            status=status,
            status_date=status_date,
        )

        request_task_item_model.additional_properties = d
        return request_task_item_model

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
