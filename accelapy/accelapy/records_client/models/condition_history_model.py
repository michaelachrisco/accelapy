import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_history_model_actionby_department import ConditionHistoryModelActionbyDepartment
    from ..models.condition_history_model_actionby_user import ConditionHistoryModelActionbyUser
    from ..models.condition_history_model_active_status import ConditionHistoryModelActiveStatus
    from ..models.condition_history_model_appliedby_department import ConditionHistoryModelAppliedbyDepartment
    from ..models.condition_history_model_appliedby_user import ConditionHistoryModelAppliedbyUser
    from ..models.condition_history_model_group import ConditionHistoryModelGroup
    from ..models.condition_history_model_inheritable import ConditionHistoryModelInheritable
    from ..models.condition_history_model_priority import ConditionHistoryModelPriority
    from ..models.condition_history_model_severity import ConditionHistoryModelSeverity
    from ..models.condition_history_model_status import ConditionHistoryModelStatus
    from ..models.condition_history_model_type import ConditionHistoryModelType


T = TypeVar("T", bound="ConditionHistoryModel")


@_attrs_define
class ConditionHistoryModel:
    """
    Attributes:
        actionby_department (Union[Unset, ConditionHistoryModelActionbyDepartment]): The department responsible for the
            action.
        actionby_user (Union[Unset, ConditionHistoryModelActionbyUser]): The individual responsible for the action.
        active_status (Union[Unset, ConditionHistoryModelActiveStatus]): Indicates whether or not the condition is
            active.
        additional_information (Union[Unset, str]): An unlimited text field to use if other fields are filled.
        additional_information_plain_text (Union[Unset, str]): An unlimited text field to use if other fields are
            filled.
        applied_date (Union[Unset, datetime.datetime]): The date the standard condition was applied.
        appliedby_department (Union[Unset, ConditionHistoryModelAppliedbyDepartment]): The department responsible for
            applying a condition.
        appliedby_user (Union[Unset, ConditionHistoryModelAppliedbyUser]): The staff member responsible for applying a
            condition.
        disp_additional_information_plain_text (Union[Unset, str]): An unlimited text field to use if other fields are
            filled.
        display_notice_in_agency (Union[Unset, bool]): Indicates whether or not to display the condition notice in
            Accela Automation when a condition to a record or parcel is applied.
        display_notice_in_citizens (Union[Unset, bool]): Indicates whether or not to display the condition notice in
            Accela Citizen Access when a condition to a record or parcel is applied.
        display_notice_in_citizens_fee (Union[Unset, bool]): Indicates whether or not to display the condition notice in
            Accela Citizen Access Fee Estimate page when a condition to a record or parcel is applied.
        effective_date (Union[Unset, datetime.datetime]): The date when you want the condition to become effective.
        expiration_date (Union[Unset, datetime.datetime]): The date when the condition expires.
        group (Union[Unset, ConditionHistoryModelGroup]): The condition group is an attribute of a condition that
            organizes condition types. Your agency defines these groups.
        id (Union[Unset, int]): The condition system id assigned by the Civic Platform server.
        inheritable (Union[Unset, ConditionHistoryModelInheritable]): This defines whether or not Accela Automation
            checks for inheritable conditions when a user associates a child record with a parent record.
        is_include_name_in_notice (Union[Unset, bool]): Indicates whether or not to display the condition name in the
            notice.
        is_include_short_comments_in_notice (Union[Unset, bool]): Indicates whether or not to display the condition
            comments in the notice.
        long_comments (Union[Unset, str]): Narrative comments to help identify the purpose or uses of the standard
            condition.
        name (Union[Unset, str]): The name of the standard condition.
        priority (Union[Unset, ConditionHistoryModelPriority]): The priority level assigned to the condition.
        public_display_message (Union[Unset, str]): Text entered into this field displays in the condition notice or
            condition status bar for the Condition Name for the public user in Accela IVR (AIVR) and Accela Citizen Access
            (ACA).
        res_additional_information_plain_text (Union[Unset, str]): An unlimited text field to use if other fields are
            filled.
        resolution_action (Union[Unset, str]): he action performed in response to a condition.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        severity (Union[Unset, ConditionHistoryModelSeverity]): The severity of the condition.
        short_comments (Union[Unset, str]): A brief description of the condition name. For example, the text may
            describe the situation that requires the system to apply the condition. You can set these short comments to
            display when a user accesses an application with this condition applied to it
        status (Union[Unset, ConditionHistoryModelStatus]): The condition status.
        status_date (Union[Unset, datetime.datetime]): The date when the current status changed.
        status_type (Union[Unset, str]): The status type for a standard condition or an approval condition, applied or
            not applied for example.
        type (Union[Unset, ConditionHistoryModelType]): The condition type.
    """

    actionby_department: Union[Unset, "ConditionHistoryModelActionbyDepartment"] = UNSET
    actionby_user: Union[Unset, "ConditionHistoryModelActionbyUser"] = UNSET
    active_status: Union[Unset, "ConditionHistoryModelActiveStatus"] = UNSET
    additional_information: Union[Unset, str] = UNSET
    additional_information_plain_text: Union[Unset, str] = UNSET
    applied_date: Union[Unset, datetime.datetime] = UNSET
    appliedby_department: Union[Unset, "ConditionHistoryModelAppliedbyDepartment"] = UNSET
    appliedby_user: Union[Unset, "ConditionHistoryModelAppliedbyUser"] = UNSET
    disp_additional_information_plain_text: Union[Unset, str] = UNSET
    display_notice_in_agency: Union[Unset, bool] = UNSET
    display_notice_in_citizens: Union[Unset, bool] = UNSET
    display_notice_in_citizens_fee: Union[Unset, bool] = UNSET
    effective_date: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    group: Union[Unset, "ConditionHistoryModelGroup"] = UNSET
    id: Union[Unset, int] = UNSET
    inheritable: Union[Unset, "ConditionHistoryModelInheritable"] = UNSET
    is_include_name_in_notice: Union[Unset, bool] = UNSET
    is_include_short_comments_in_notice: Union[Unset, bool] = UNSET
    long_comments: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    priority: Union[Unset, "ConditionHistoryModelPriority"] = UNSET
    public_display_message: Union[Unset, str] = UNSET
    res_additional_information_plain_text: Union[Unset, str] = UNSET
    resolution_action: Union[Unset, str] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    severity: Union[Unset, "ConditionHistoryModelSeverity"] = UNSET
    short_comments: Union[Unset, str] = UNSET
    status: Union[Unset, "ConditionHistoryModelStatus"] = UNSET
    status_date: Union[Unset, datetime.datetime] = UNSET
    status_type: Union[Unset, str] = UNSET
    type: Union[Unset, "ConditionHistoryModelType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actionby_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionby_department, Unset):
            actionby_department = self.actionby_department.to_dict()

        actionby_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionby_user, Unset):
            actionby_user = self.actionby_user.to_dict()

        active_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_status, Unset):
            active_status = self.active_status.to_dict()

        additional_information = self.additional_information
        additional_information_plain_text = self.additional_information_plain_text
        applied_date: Union[Unset, str] = UNSET
        if not isinstance(self.applied_date, Unset):
            applied_date = self.applied_date.isoformat()

        appliedby_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appliedby_department, Unset):
            appliedby_department = self.appliedby_department.to_dict()

        appliedby_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appliedby_user, Unset):
            appliedby_user = self.appliedby_user.to_dict()

        disp_additional_information_plain_text = self.disp_additional_information_plain_text
        display_notice_in_agency = self.display_notice_in_agency
        display_notice_in_citizens = self.display_notice_in_citizens
        display_notice_in_citizens_fee = self.display_notice_in_citizens_fee
        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id
        inheritable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inheritable, Unset):
            inheritable = self.inheritable.to_dict()

        is_include_name_in_notice = self.is_include_name_in_notice
        is_include_short_comments_in_notice = self.is_include_short_comments_in_notice
        long_comments = self.long_comments
        name = self.name
        priority: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        public_display_message = self.public_display_message
        res_additional_information_plain_text = self.res_additional_information_plain_text
        resolution_action = self.resolution_action
        service_provider_code = self.service_provider_code
        severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        short_comments = self.short_comments
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        status_type = self.status_type
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actionby_department is not UNSET:
            field_dict["actionbyDepartment"] = actionby_department
        if actionby_user is not UNSET:
            field_dict["actionbyUser"] = actionby_user
        if active_status is not UNSET:
            field_dict["activeStatus"] = active_status
        if additional_information is not UNSET:
            field_dict["additionalInformation"] = additional_information
        if additional_information_plain_text is not UNSET:
            field_dict["additionalInformationPlainText"] = additional_information_plain_text
        if applied_date is not UNSET:
            field_dict["appliedDate"] = applied_date
        if appliedby_department is not UNSET:
            field_dict["appliedbyDepartment"] = appliedby_department
        if appliedby_user is not UNSET:
            field_dict["appliedbyUser"] = appliedby_user
        if disp_additional_information_plain_text is not UNSET:
            field_dict["dispAdditionalInformationPlainText"] = disp_additional_information_plain_text
        if display_notice_in_agency is not UNSET:
            field_dict["displayNoticeInAgency"] = display_notice_in_agency
        if display_notice_in_citizens is not UNSET:
            field_dict["displayNoticeInCitizens"] = display_notice_in_citizens
        if display_notice_in_citizens_fee is not UNSET:
            field_dict["displayNoticeInCitizensFee"] = display_notice_in_citizens_fee
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if inheritable is not UNSET:
            field_dict["inheritable"] = inheritable
        if is_include_name_in_notice is not UNSET:
            field_dict["isIncludeNameInNotice"] = is_include_name_in_notice
        if is_include_short_comments_in_notice is not UNSET:
            field_dict["isIncludeShortCommentsInNotice"] = is_include_short_comments_in_notice
        if long_comments is not UNSET:
            field_dict["longComments"] = long_comments
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if public_display_message is not UNSET:
            field_dict["publicDisplayMessage"] = public_display_message
        if res_additional_information_plain_text is not UNSET:
            field_dict["resAdditionalInformationPlainText"] = res_additional_information_plain_text
        if resolution_action is not UNSET:
            field_dict["resolutionAction"] = resolution_action
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if severity is not UNSET:
            field_dict["severity"] = severity
        if short_comments is not UNSET:
            field_dict["shortComments"] = short_comments
        if status is not UNSET:
            field_dict["status"] = status
        if status_date is not UNSET:
            field_dict["statusDate"] = status_date
        if status_type is not UNSET:
            field_dict["statusType"] = status_type
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_history_model_actionby_department import ConditionHistoryModelActionbyDepartment
        from ..models.condition_history_model_actionby_user import ConditionHistoryModelActionbyUser
        from ..models.condition_history_model_active_status import ConditionHistoryModelActiveStatus
        from ..models.condition_history_model_appliedby_department import ConditionHistoryModelAppliedbyDepartment
        from ..models.condition_history_model_appliedby_user import ConditionHistoryModelAppliedbyUser
        from ..models.condition_history_model_group import ConditionHistoryModelGroup
        from ..models.condition_history_model_inheritable import ConditionHistoryModelInheritable
        from ..models.condition_history_model_priority import ConditionHistoryModelPriority
        from ..models.condition_history_model_severity import ConditionHistoryModelSeverity
        from ..models.condition_history_model_status import ConditionHistoryModelStatus
        from ..models.condition_history_model_type import ConditionHistoryModelType

        d = src_dict.copy()
        _actionby_department = d.pop("actionbyDepartment", UNSET)
        actionby_department: Union[Unset, ConditionHistoryModelActionbyDepartment]
        if isinstance(_actionby_department, Unset):
            actionby_department = UNSET
        else:
            actionby_department = ConditionHistoryModelActionbyDepartment.from_dict(_actionby_department)

        _actionby_user = d.pop("actionbyUser", UNSET)
        actionby_user: Union[Unset, ConditionHistoryModelActionbyUser]
        if isinstance(_actionby_user, Unset):
            actionby_user = UNSET
        else:
            actionby_user = ConditionHistoryModelActionbyUser.from_dict(_actionby_user)

        _active_status = d.pop("activeStatus", UNSET)
        active_status: Union[Unset, ConditionHistoryModelActiveStatus]
        if isinstance(_active_status, Unset):
            active_status = UNSET
        else:
            active_status = ConditionHistoryModelActiveStatus.from_dict(_active_status)

        additional_information = d.pop("additionalInformation", UNSET)

        additional_information_plain_text = d.pop("additionalInformationPlainText", UNSET)

        _applied_date = d.pop("appliedDate", UNSET)
        applied_date: Union[Unset, datetime.datetime]
        if isinstance(_applied_date, Unset):
            applied_date = UNSET
        else:
            applied_date = isoparse(_applied_date)

        _appliedby_department = d.pop("appliedbyDepartment", UNSET)
        appliedby_department: Union[Unset, ConditionHistoryModelAppliedbyDepartment]
        if isinstance(_appliedby_department, Unset):
            appliedby_department = UNSET
        else:
            appliedby_department = ConditionHistoryModelAppliedbyDepartment.from_dict(_appliedby_department)

        _appliedby_user = d.pop("appliedbyUser", UNSET)
        appliedby_user: Union[Unset, ConditionHistoryModelAppliedbyUser]
        if isinstance(_appliedby_user, Unset):
            appliedby_user = UNSET
        else:
            appliedby_user = ConditionHistoryModelAppliedbyUser.from_dict(_appliedby_user)

        disp_additional_information_plain_text = d.pop("dispAdditionalInformationPlainText", UNSET)

        display_notice_in_agency = d.pop("displayNoticeInAgency", UNSET)

        display_notice_in_citizens = d.pop("displayNoticeInCitizens", UNSET)

        display_notice_in_citizens_fee = d.pop("displayNoticeInCitizensFee", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.datetime]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        _group = d.pop("group", UNSET)
        group: Union[Unset, ConditionHistoryModelGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = ConditionHistoryModelGroup.from_dict(_group)

        id = d.pop("id", UNSET)

        _inheritable = d.pop("inheritable", UNSET)
        inheritable: Union[Unset, ConditionHistoryModelInheritable]
        if isinstance(_inheritable, Unset):
            inheritable = UNSET
        else:
            inheritable = ConditionHistoryModelInheritable.from_dict(_inheritable)

        is_include_name_in_notice = d.pop("isIncludeNameInNotice", UNSET)

        is_include_short_comments_in_notice = d.pop("isIncludeShortCommentsInNotice", UNSET)

        long_comments = d.pop("longComments", UNSET)

        name = d.pop("name", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, ConditionHistoryModelPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ConditionHistoryModelPriority.from_dict(_priority)

        public_display_message = d.pop("publicDisplayMessage", UNSET)

        res_additional_information_plain_text = d.pop("resAdditionalInformationPlainText", UNSET)

        resolution_action = d.pop("resolutionAction", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, ConditionHistoryModelSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = ConditionHistoryModelSeverity.from_dict(_severity)

        short_comments = d.pop("shortComments", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ConditionHistoryModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConditionHistoryModelStatus.from_dict(_status)

        _status_date = d.pop("statusDate", UNSET)
        status_date: Union[Unset, datetime.datetime]
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        status_type = d.pop("statusType", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ConditionHistoryModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ConditionHistoryModelType.from_dict(_type)

        condition_history_model = cls(
            actionby_department=actionby_department,
            actionby_user=actionby_user,
            active_status=active_status,
            additional_information=additional_information,
            additional_information_plain_text=additional_information_plain_text,
            applied_date=applied_date,
            appliedby_department=appliedby_department,
            appliedby_user=appliedby_user,
            disp_additional_information_plain_text=disp_additional_information_plain_text,
            display_notice_in_agency=display_notice_in_agency,
            display_notice_in_citizens=display_notice_in_citizens,
            display_notice_in_citizens_fee=display_notice_in_citizens_fee,
            effective_date=effective_date,
            expiration_date=expiration_date,
            group=group,
            id=id,
            inheritable=inheritable,
            is_include_name_in_notice=is_include_name_in_notice,
            is_include_short_comments_in_notice=is_include_short_comments_in_notice,
            long_comments=long_comments,
            name=name,
            priority=priority,
            public_display_message=public_display_message,
            res_additional_information_plain_text=res_additional_information_plain_text,
            resolution_action=resolution_action,
            service_provider_code=service_provider_code,
            severity=severity,
            short_comments=short_comments,
            status=status,
            status_date=status_date,
            status_type=status_type,
            type=type,
        )

        condition_history_model.additional_properties = d
        return condition_history_model

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
