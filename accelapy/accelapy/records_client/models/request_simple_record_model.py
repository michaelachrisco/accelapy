import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_expiration_model import RecordExpirationModel
    from ..models.request_simple_record_model_priority import RequestSimpleRecordModelPriority
    from ..models.request_simple_record_model_reported_channel import RequestSimpleRecordModelReportedChannel
    from ..models.request_simple_record_model_reported_type import RequestSimpleRecordModelReportedType
    from ..models.request_simple_record_model_severity import RequestSimpleRecordModelSeverity
    from ..models.request_simple_record_model_status import RequestSimpleRecordModelStatus
    from ..models.request_simple_record_model_status_reason import RequestSimpleRecordModelStatusReason


T = TypeVar("T", bound="RequestSimpleRecordModel")


@_attrs_define
class RequestSimpleRecordModel:
    """
    Attributes:
        actual_production_unit (Union[Unset, float]): Estimated cost per production unit.
        appearance_date (Union[Unset, datetime.datetime]): The date for a hearing appearance.
        appearance_day_of_week (Union[Unset, str]): The day for a hearing appearance.
        assigned_date (Union[Unset, datetime.datetime]): The date the application was assigned.
        assigned_to_department (Union[Unset, str]): The department responsible for the action. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        balance (Union[Unset, float]): The amount due.
        booking (Union[Unset, bool]): Indicates whether or not there was a booking in addition to a citation.
        closed_by_department (Union[Unset, str]): The department responsible for closing the record. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        closed_date (Union[Unset, datetime.datetime]): The date the application was closed.
        complete_date (Union[Unset, datetime.datetime]): The date the application was completed.
        completed_by_department (Union[Unset, str]): The department responsible for completion. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        defendant_signature (Union[Unset, bool]): Indicates whether or not a defendant's signature has been obtained.
        description (Union[Unset, str]): The description of the record or item.
        enforce_department (Union[Unset, str]): The name of the department responsible for enforcement. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        estimated_production_unit (Union[Unset, float]): The estimated number of production units.
        estimated_total_job_cost (Union[Unset, float]): The estimated cost of the job.
        first_issued_date (Union[Unset, datetime.datetime]): The first issued date for license
        infraction (Union[Unset, bool]): Indicates whether or not an infraction occurred.
        inspector_department (Union[Unset, str]): The name of the department where the inspector works. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        inspector_id (Union[Unset, str]): The ID number of the inspector. See [Get All Inspectors](./api-
            inspections.html#operation/v4.get.inspectors).
        inspector_name (Union[Unset, str]): The name of the inspector. See [Get All Inspectors](./api-
            inspections.html#operation/v4.get.inspectors).
        job_value (Union[Unset, float]): The value of the job.
        misdemeanor (Union[Unset, bool]): Indicates whether or not a misdemeanor occurred.
        name (Union[Unset, str]): The name associated to the record.
        offense_witnessed (Union[Unset, bool]): Indicates whether or not  there was a witness to the alleged offense.
        priority (Union[Unset, RequestSimpleRecordModelPriority]): The priority level assigned to the record. See [Get
            All Priorities](./api-settings.html#operation/v4.get.settings.priorities).
        public_owned (Union[Unset, bool]): Indicates whether or not the record is for the public.
        renewal_info (Union[Unset, RecordExpirationModel]):
        reported_channel (Union[Unset, RequestSimpleRecordModelReportedChannel]): The incoming channel through which the
            applicant submitted the application.
        reported_date (Union[Unset, datetime.datetime]): The date the complaint was reported.
        reported_type (Union[Unset, RequestSimpleRecordModelReportedType]): The type of complaint or incident being
            reported.
        scheduled_date (Union[Unset, datetime.datetime]): The date when the inspection gets scheduled.
        severity (Union[Unset, RequestSimpleRecordModelSeverity]): Indicates the severity of the condition.
        short_notes (Union[Unset, str]): A brief note about the record subject.
        status (Union[Unset, RequestSimpleRecordModelStatus]): The record status.
        status_reason (Union[Unset, RequestSimpleRecordModelStatusReason]): 	The reason for the status setting on the
            record.
        total_fee (Union[Unset, float]): The total amount of the fees invoiced to the record.
        total_pay (Union[Unset, float]): The total amount of pay.
    """

    actual_production_unit: Union[Unset, float] = UNSET
    appearance_date: Union[Unset, datetime.datetime] = UNSET
    appearance_day_of_week: Union[Unset, str] = UNSET
    assigned_date: Union[Unset, datetime.datetime] = UNSET
    assigned_to_department: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    booking: Union[Unset, bool] = UNSET
    closed_by_department: Union[Unset, str] = UNSET
    closed_date: Union[Unset, datetime.datetime] = UNSET
    complete_date: Union[Unset, datetime.datetime] = UNSET
    completed_by_department: Union[Unset, str] = UNSET
    defendant_signature: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    enforce_department: Union[Unset, str] = UNSET
    estimated_production_unit: Union[Unset, float] = UNSET
    estimated_total_job_cost: Union[Unset, float] = UNSET
    first_issued_date: Union[Unset, datetime.datetime] = UNSET
    infraction: Union[Unset, bool] = UNSET
    inspector_department: Union[Unset, str] = UNSET
    inspector_id: Union[Unset, str] = UNSET
    inspector_name: Union[Unset, str] = UNSET
    job_value: Union[Unset, float] = UNSET
    misdemeanor: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    offense_witnessed: Union[Unset, bool] = UNSET
    priority: Union[Unset, "RequestSimpleRecordModelPriority"] = UNSET
    public_owned: Union[Unset, bool] = UNSET
    renewal_info: Union[Unset, "RecordExpirationModel"] = UNSET
    reported_channel: Union[Unset, "RequestSimpleRecordModelReportedChannel"] = UNSET
    reported_date: Union[Unset, datetime.datetime] = UNSET
    reported_type: Union[Unset, "RequestSimpleRecordModelReportedType"] = UNSET
    scheduled_date: Union[Unset, datetime.datetime] = UNSET
    severity: Union[Unset, "RequestSimpleRecordModelSeverity"] = UNSET
    short_notes: Union[Unset, str] = UNSET
    status: Union[Unset, "RequestSimpleRecordModelStatus"] = UNSET
    status_reason: Union[Unset, "RequestSimpleRecordModelStatusReason"] = UNSET
    total_fee: Union[Unset, float] = UNSET
    total_pay: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actual_production_unit = self.actual_production_unit
        appearance_date: Union[Unset, str] = UNSET
        if not isinstance(self.appearance_date, Unset):
            appearance_date = self.appearance_date.isoformat()

        appearance_day_of_week = self.appearance_day_of_week
        assigned_date: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_date, Unset):
            assigned_date = self.assigned_date.isoformat()

        assigned_to_department = self.assigned_to_department
        balance = self.balance
        booking = self.booking
        closed_by_department = self.closed_by_department
        closed_date: Union[Unset, str] = UNSET
        if not isinstance(self.closed_date, Unset):
            closed_date = self.closed_date.isoformat()

        complete_date: Union[Unset, str] = UNSET
        if not isinstance(self.complete_date, Unset):
            complete_date = self.complete_date.isoformat()

        completed_by_department = self.completed_by_department
        defendant_signature = self.defendant_signature
        description = self.description
        enforce_department = self.enforce_department
        estimated_production_unit = self.estimated_production_unit
        estimated_total_job_cost = self.estimated_total_job_cost
        first_issued_date: Union[Unset, str] = UNSET
        if not isinstance(self.first_issued_date, Unset):
            first_issued_date = self.first_issued_date.isoformat()

        infraction = self.infraction
        inspector_department = self.inspector_department
        inspector_id = self.inspector_id
        inspector_name = self.inspector_name
        job_value = self.job_value
        misdemeanor = self.misdemeanor
        name = self.name
        offense_witnessed = self.offense_witnessed
        priority: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        public_owned = self.public_owned
        renewal_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.renewal_info, Unset):
            renewal_info = self.renewal_info.to_dict()

        reported_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reported_channel, Unset):
            reported_channel = self.reported_channel.to_dict()

        reported_date: Union[Unset, str] = UNSET
        if not isinstance(self.reported_date, Unset):
            reported_date = self.reported_date.isoformat()

        reported_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reported_type, Unset):
            reported_type = self.reported_type.to_dict()

        scheduled_date: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_date, Unset):
            scheduled_date = self.scheduled_date.isoformat()

        severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        short_notes = self.short_notes
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status_reason, Unset):
            status_reason = self.status_reason.to_dict()

        total_fee = self.total_fee
        total_pay = self.total_pay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_production_unit is not UNSET:
            field_dict["actualProductionUnit"] = actual_production_unit
        if appearance_date is not UNSET:
            field_dict["appearanceDate"] = appearance_date
        if appearance_day_of_week is not UNSET:
            field_dict["appearanceDayOfWeek"] = appearance_day_of_week
        if assigned_date is not UNSET:
            field_dict["assignedDate"] = assigned_date
        if assigned_to_department is not UNSET:
            field_dict["assignedToDepartment"] = assigned_to_department
        if balance is not UNSET:
            field_dict["balance"] = balance
        if booking is not UNSET:
            field_dict["booking"] = booking
        if closed_by_department is not UNSET:
            field_dict["closedByDepartment"] = closed_by_department
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if complete_date is not UNSET:
            field_dict["completeDate"] = complete_date
        if completed_by_department is not UNSET:
            field_dict["completedByDepartment"] = completed_by_department
        if defendant_signature is not UNSET:
            field_dict["defendantSignature"] = defendant_signature
        if description is not UNSET:
            field_dict["description"] = description
        if enforce_department is not UNSET:
            field_dict["enforceDepartment"] = enforce_department
        if estimated_production_unit is not UNSET:
            field_dict["estimatedProductionUnit"] = estimated_production_unit
        if estimated_total_job_cost is not UNSET:
            field_dict["estimatedTotalJobCost"] = estimated_total_job_cost
        if first_issued_date is not UNSET:
            field_dict["firstIssuedDate"] = first_issued_date
        if infraction is not UNSET:
            field_dict["infraction"] = infraction
        if inspector_department is not UNSET:
            field_dict["inspectorDepartment"] = inspector_department
        if inspector_id is not UNSET:
            field_dict["inspectorId"] = inspector_id
        if inspector_name is not UNSET:
            field_dict["inspectorName"] = inspector_name
        if job_value is not UNSET:
            field_dict["jobValue"] = job_value
        if misdemeanor is not UNSET:
            field_dict["misdemeanor"] = misdemeanor
        if name is not UNSET:
            field_dict["name"] = name
        if offense_witnessed is not UNSET:
            field_dict["offenseWitnessed"] = offense_witnessed
        if priority is not UNSET:
            field_dict["priority"] = priority
        if public_owned is not UNSET:
            field_dict["publicOwned"] = public_owned
        if renewal_info is not UNSET:
            field_dict["renewalInfo"] = renewal_info
        if reported_channel is not UNSET:
            field_dict["reportedChannel"] = reported_channel
        if reported_date is not UNSET:
            field_dict["reportedDate"] = reported_date
        if reported_type is not UNSET:
            field_dict["reportedType"] = reported_type
        if scheduled_date is not UNSET:
            field_dict["scheduledDate"] = scheduled_date
        if severity is not UNSET:
            field_dict["severity"] = severity
        if short_notes is not UNSET:
            field_dict["shortNotes"] = short_notes
        if status is not UNSET:
            field_dict["status"] = status
        if status_reason is not UNSET:
            field_dict["statusReason"] = status_reason
        if total_fee is not UNSET:
            field_dict["totalFee"] = total_fee
        if total_pay is not UNSET:
            field_dict["totalPay"] = total_pay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_expiration_model import RecordExpirationModel
        from ..models.request_simple_record_model_priority import RequestSimpleRecordModelPriority
        from ..models.request_simple_record_model_reported_channel import RequestSimpleRecordModelReportedChannel
        from ..models.request_simple_record_model_reported_type import RequestSimpleRecordModelReportedType
        from ..models.request_simple_record_model_severity import RequestSimpleRecordModelSeverity
        from ..models.request_simple_record_model_status import RequestSimpleRecordModelStatus
        from ..models.request_simple_record_model_status_reason import RequestSimpleRecordModelStatusReason

        d = src_dict.copy()
        actual_production_unit = d.pop("actualProductionUnit", UNSET)

        _appearance_date = d.pop("appearanceDate", UNSET)
        appearance_date: Union[Unset, datetime.datetime]
        if isinstance(_appearance_date, Unset):
            appearance_date = UNSET
        else:
            appearance_date = isoparse(_appearance_date)

        appearance_day_of_week = d.pop("appearanceDayOfWeek", UNSET)

        _assigned_date = d.pop("assignedDate", UNSET)
        assigned_date: Union[Unset, datetime.datetime]
        if isinstance(_assigned_date, Unset):
            assigned_date = UNSET
        else:
            assigned_date = isoparse(_assigned_date)

        assigned_to_department = d.pop("assignedToDepartment", UNSET)

        balance = d.pop("balance", UNSET)

        booking = d.pop("booking", UNSET)

        closed_by_department = d.pop("closedByDepartment", UNSET)

        _closed_date = d.pop("closedDate", UNSET)
        closed_date: Union[Unset, datetime.datetime]
        if isinstance(_closed_date, Unset):
            closed_date = UNSET
        else:
            closed_date = isoparse(_closed_date)

        _complete_date = d.pop("completeDate", UNSET)
        complete_date: Union[Unset, datetime.datetime]
        if isinstance(_complete_date, Unset):
            complete_date = UNSET
        else:
            complete_date = isoparse(_complete_date)

        completed_by_department = d.pop("completedByDepartment", UNSET)

        defendant_signature = d.pop("defendantSignature", UNSET)

        description = d.pop("description", UNSET)

        enforce_department = d.pop("enforceDepartment", UNSET)

        estimated_production_unit = d.pop("estimatedProductionUnit", UNSET)

        estimated_total_job_cost = d.pop("estimatedTotalJobCost", UNSET)

        _first_issued_date = d.pop("firstIssuedDate", UNSET)
        first_issued_date: Union[Unset, datetime.datetime]
        if isinstance(_first_issued_date, Unset):
            first_issued_date = UNSET
        else:
            first_issued_date = isoparse(_first_issued_date)

        infraction = d.pop("infraction", UNSET)

        inspector_department = d.pop("inspectorDepartment", UNSET)

        inspector_id = d.pop("inspectorId", UNSET)

        inspector_name = d.pop("inspectorName", UNSET)

        job_value = d.pop("jobValue", UNSET)

        misdemeanor = d.pop("misdemeanor", UNSET)

        name = d.pop("name", UNSET)

        offense_witnessed = d.pop("offenseWitnessed", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, RequestSimpleRecordModelPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = RequestSimpleRecordModelPriority.from_dict(_priority)

        public_owned = d.pop("publicOwned", UNSET)

        _renewal_info = d.pop("renewalInfo", UNSET)
        renewal_info: Union[Unset, RecordExpirationModel]
        if isinstance(_renewal_info, Unset):
            renewal_info = UNSET
        else:
            renewal_info = RecordExpirationModel.from_dict(_renewal_info)

        _reported_channel = d.pop("reportedChannel", UNSET)
        reported_channel: Union[Unset, RequestSimpleRecordModelReportedChannel]
        if isinstance(_reported_channel, Unset):
            reported_channel = UNSET
        else:
            reported_channel = RequestSimpleRecordModelReportedChannel.from_dict(_reported_channel)

        _reported_date = d.pop("reportedDate", UNSET)
        reported_date: Union[Unset, datetime.datetime]
        if isinstance(_reported_date, Unset):
            reported_date = UNSET
        else:
            reported_date = isoparse(_reported_date)

        _reported_type = d.pop("reportedType", UNSET)
        reported_type: Union[Unset, RequestSimpleRecordModelReportedType]
        if isinstance(_reported_type, Unset):
            reported_type = UNSET
        else:
            reported_type = RequestSimpleRecordModelReportedType.from_dict(_reported_type)

        _scheduled_date = d.pop("scheduledDate", UNSET)
        scheduled_date: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_date, Unset):
            scheduled_date = UNSET
        else:
            scheduled_date = isoparse(_scheduled_date)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, RequestSimpleRecordModelSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = RequestSimpleRecordModelSeverity.from_dict(_severity)

        short_notes = d.pop("shortNotes", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RequestSimpleRecordModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestSimpleRecordModelStatus.from_dict(_status)

        _status_reason = d.pop("statusReason", UNSET)
        status_reason: Union[Unset, RequestSimpleRecordModelStatusReason]
        if isinstance(_status_reason, Unset):
            status_reason = UNSET
        else:
            status_reason = RequestSimpleRecordModelStatusReason.from_dict(_status_reason)

        total_fee = d.pop("totalFee", UNSET)

        total_pay = d.pop("totalPay", UNSET)

        request_simple_record_model = cls(
            actual_production_unit=actual_production_unit,
            appearance_date=appearance_date,
            appearance_day_of_week=appearance_day_of_week,
            assigned_date=assigned_date,
            assigned_to_department=assigned_to_department,
            balance=balance,
            booking=booking,
            closed_by_department=closed_by_department,
            closed_date=closed_date,
            complete_date=complete_date,
            completed_by_department=completed_by_department,
            defendant_signature=defendant_signature,
            description=description,
            enforce_department=enforce_department,
            estimated_production_unit=estimated_production_unit,
            estimated_total_job_cost=estimated_total_job_cost,
            first_issued_date=first_issued_date,
            infraction=infraction,
            inspector_department=inspector_department,
            inspector_id=inspector_id,
            inspector_name=inspector_name,
            job_value=job_value,
            misdemeanor=misdemeanor,
            name=name,
            offense_witnessed=offense_witnessed,
            priority=priority,
            public_owned=public_owned,
            renewal_info=renewal_info,
            reported_channel=reported_channel,
            reported_date=reported_date,
            reported_type=reported_type,
            scheduled_date=scheduled_date,
            severity=severity,
            short_notes=short_notes,
            status=status,
            status_reason=status_reason,
            total_fee=total_fee,
            total_pay=total_pay,
        )

        request_simple_record_model.additional_properties = d
        return request_simple_record_model

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
