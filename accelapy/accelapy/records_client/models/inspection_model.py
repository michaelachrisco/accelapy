import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.inspection_model_billable import InspectionModelBillable
from ..models.inspection_model_schedule_end_ampm import InspectionModelScheduleEndAMPM
from ..models.inspection_model_schedule_start_ampm import InspectionModelScheduleStartAMPM
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_contact_model import InspectionContactModel
    from ..models.inspection_model_status import InspectionModelStatus
    from ..models.inspection_type_simple_model import InspectionTypeSimpleModel
    from ..models.record_address_model import RecordAddressModel
    from ..models.record_id_model import RecordIdModel
    from ..models.record_type_no_alias_model import RecordTypeNoAliasModel
    from ..models.simple_record_model import SimpleRecordModel


T = TypeVar("T", bound="InspectionModel")


@_attrs_define
class InspectionModel:
    """
    Attributes:
        team_name (Union[Unset, str]): Inspection Team name.
        floor (Union[Unset, str]): Inspection Floor.
        floor_unit (Union[Unset, str]): Inspection Floor Unit.
        address (Union[Unset, RecordAddressModel]):
        billable (Union[Unset, InspectionModelBillable]): This defines whether or not the item is billable.
        category (Union[Unset, str]): The inspection category, which is used to organize inspection types. An inspection
            type is assigned to one or more inspection categories.
        comment_display (Union[Unset, str]): Indicates whether or not Accela Citizen Access users can view the
            inspection results comments.
        comment_public_visible (Union[Unset, List[str]]): Specifies the type of user who can view the inspection result
            comments. "All ACA Users" - Both registered and anonymous Accela Citizen Access users can view the comments for
            inspection results. "Record Creator Only" - the user who created the record can see the comments for the
            inspection results. "Record Creator and Licensed Professional" - The user who created the record and the
            licensed professional associated with the record can see the comments for the inspection results.
        completed_ampm (Union[Unset, str]): Indicates whether completed time is "AM" or "PM".
        completed_date (Union[Unset, datetime.datetime]): The date of completion.
        completed_time (Union[Unset, str]): The time of completion.
        contact (Union[Unset, InspectionContactModel]):
        contact_first_name (Union[Unset, str]): The contact's first name. This field is only active when the Contact
            Type selected is Individual.
        contact_last_name (Union[Unset, str]): The last name of the contact.
        contact_middle_name (Union[Unset, str]): The middle name of the contact.
        desired_ampm (Union[Unset, str]): Indicates whether the desired inspection time is AM or PM.
        desired_date (Union[Unset, datetime.datetime]): The desired inspection date.
        desired_time (Union[Unset, str]): The desired inspection time.
        end_mileage (Union[Unset, float]): The ending mileage for the inspection.
        end_time (Union[Unset, datetime.datetime]): The time the inspection was completed.
        estimated_end_time (Union[Unset, str]): inspection estimated end time.
        estimated_start_time (Union[Unset, str]): The scheduled start time for the inspection.
        gis_area_name (Union[Unset, str]): The GIS Object ID of the parent application if the application that the
            inspection is scheduled for has a parent application that is a project application.
        grade (Union[Unset, str]): The name of the inspection grade.
        id (Union[Unset, int]): The inspection system id assigned by the Civic Platform server.
        inspector_full_name (Union[Unset, str]): The name of the inspector performing the assessment.
        inspector_id (Union[Unset, str]): The ID number of the inspector. See [Get All Inspectors](./api-
            inspections.html#operation/v4.get.inspectors).
        is_auto_assign (Union[Unset, str]): This defines whether or not you want to automatically reschedule the
            inspection when the previous inspection status attains Approved status.
        latitude (Union[Unset, float]): The angular distance of a place north or south of the earth's equator, usually
            expressed in degrees and minutes.
        longitude (Union[Unset, float]): The angular distance of a place east or west of the meridian at Greenwich,
            England, usually expressed in degrees and minutes.
        major_violation (Union[Unset, int]): The number of major violations.
        overtime (Union[Unset, str]): A labor cost factor that indicates time worked beyond a worker's regular working
            hours.
        priority (Union[Unset, float]): The priority level assigned to the inspection.
        public_visible (Union[Unset, str]): This defines whether or not Accela Citizen Access users can view comment
            about the inspection results.
        record (Union[Unset, SimpleRecordModel]):
        record_id (Union[Unset, RecordIdModel]):
        record_type (Union[Unset, RecordTypeNoAliasModel]):
        request_ampm (Union[Unset, str]): The time segment, AM or PM, for the time specified in the requestTime field.
        request_comment (Union[Unset, str]): Comments about the new inspection. For example, you may identify who
            requested the inspection.
        request_date (Union[Unset, datetime.datetime]): The date when an inspection request is submitted.
        request_time (Union[Unset, str]): This time is automatically generated when a new inspection is scheduled and
            submitted.
        requestor_first_name (Union[Unset, str]): The first name of the person requesting an inspection-related
            operation.
        requestor_last_name (Union[Unset, str]): The last name of the person requesting an inspection-related operation.
        requestor_middle_name (Union[Unset, str]): The middle name of the person requesting an inspection-related
            operation.
        requestor_phone (Union[Unset, str]): The telephone number for the person who processes the inspection request or
            schedules the inspection.
        requestor_phone_idd (Union[Unset, str]): The telephone number for the person who processes the inspection
            request or schedules the inspection.
        requestor_user_id (Union[Unset, str]): The user Id of the person requesting an inspection-related operation.
        required_inspection (Union[Unset, str]): This defines whether the inspection is optional or required.
        result_comment (Union[Unset, str]): The inspection result comments.
        result_type (Union[Unset, str]): The type of result that can be ascibed to an inspection. There are three result
            types: Approved: Approves (passes) the checklist item. Denied: Denies (fails) the checklist item. Informational:
            Indicates that the checklist items do not need a status of app
        schedule_date (Union[Unset, datetime.datetime]): The date when the inspection gets scheduled.
        schedule_end_ampm (Union[Unset, InspectionModelScheduleEndAMPM]): Indicates whether the scheduleEndTime is in
            the AM or PM.
        schedule_end_time (Union[Unset, str]): The scheduled end time for the inspection.
        schedule_start_ampm (Union[Unset, InspectionModelScheduleStartAMPM]): AM indicates the 12 hour period from
            midnight to noon. PM indicates the 12 hour period from noon to midnight.
        schedule_start_time (Union[Unset, str]): The scheduled start time for the inspection.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        start_mileage (Union[Unset, float]): The starting mileage for the inspection.
        start_time (Union[Unset, datetime.datetime]): The time when you started the inspection.
        status (Union[Unset, InspectionModelStatus]): The inspection status. See [Get All Inspection Statuses](./api-
            settings.html#operation/v4.get.settings.inspections.statuses).
        submit_ampm (Union[Unset, str]): The time block for the scheduled inspection.
        submit_date (Union[Unset, datetime.datetime]): The date that the inspection was submitted.
        submit_time (Union[Unset, str]): The time that a new inspection is submitted. Civic Platform generates this
            value.
        total_mileage (Union[Unset, float]): The total mileage for the inspection.
        total_score (Union[Unset, int]): The overall score of the inspection that includes the inspection result,
            inspection grade, checklist total score and checklist major violation option.
        total_time (Union[Unset, float]): The total amount of time used to do an inspection.
        type (Union[Unset, InspectionTypeSimpleModel]):
        unit_number (Union[Unset, str]): The number of time units (see timeUnitDuration) comprising an inspection.
        units (Union[Unset, float]): The amount of time comprising the smallest time unit for conducting an inspection.
        vehicle_id (Union[Unset, str]): A number, such as the license plate number or VIN, that identifies the vehicle
            used to complete an inspection.
    """

    team_name: Union[Unset, str] = UNSET
    floor: Union[Unset, str] = UNSET
    floor_unit: Union[Unset, str] = UNSET
    address: Union[Unset, "RecordAddressModel"] = UNSET
    billable: Union[Unset, InspectionModelBillable] = UNSET
    category: Union[Unset, str] = UNSET
    comment_display: Union[Unset, str] = UNSET
    comment_public_visible: Union[Unset, List[str]] = UNSET
    completed_ampm: Union[Unset, str] = UNSET
    completed_date: Union[Unset, datetime.datetime] = UNSET
    completed_time: Union[Unset, str] = UNSET
    contact: Union[Unset, "InspectionContactModel"] = UNSET
    contact_first_name: Union[Unset, str] = UNSET
    contact_last_name: Union[Unset, str] = UNSET
    contact_middle_name: Union[Unset, str] = UNSET
    desired_ampm: Union[Unset, str] = UNSET
    desired_date: Union[Unset, datetime.datetime] = UNSET
    desired_time: Union[Unset, str] = UNSET
    end_mileage: Union[Unset, float] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    estimated_end_time: Union[Unset, str] = UNSET
    estimated_start_time: Union[Unset, str] = UNSET
    gis_area_name: Union[Unset, str] = UNSET
    grade: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    inspector_full_name: Union[Unset, str] = UNSET
    inspector_id: Union[Unset, str] = UNSET
    is_auto_assign: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    major_violation: Union[Unset, int] = UNSET
    overtime: Union[Unset, str] = UNSET
    priority: Union[Unset, float] = UNSET
    public_visible: Union[Unset, str] = UNSET
    record: Union[Unset, "SimpleRecordModel"] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    record_type: Union[Unset, "RecordTypeNoAliasModel"] = UNSET
    request_ampm: Union[Unset, str] = UNSET
    request_comment: Union[Unset, str] = UNSET
    request_date: Union[Unset, datetime.datetime] = UNSET
    request_time: Union[Unset, str] = UNSET
    requestor_first_name: Union[Unset, str] = UNSET
    requestor_last_name: Union[Unset, str] = UNSET
    requestor_middle_name: Union[Unset, str] = UNSET
    requestor_phone: Union[Unset, str] = UNSET
    requestor_phone_idd: Union[Unset, str] = UNSET
    requestor_user_id: Union[Unset, str] = UNSET
    required_inspection: Union[Unset, str] = UNSET
    result_comment: Union[Unset, str] = UNSET
    result_type: Union[Unset, str] = UNSET
    schedule_date: Union[Unset, datetime.datetime] = UNSET
    schedule_end_ampm: Union[Unset, InspectionModelScheduleEndAMPM] = UNSET
    schedule_end_time: Union[Unset, str] = UNSET
    schedule_start_ampm: Union[Unset, InspectionModelScheduleStartAMPM] = UNSET
    schedule_start_time: Union[Unset, str] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    start_mileage: Union[Unset, float] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, "InspectionModelStatus"] = UNSET
    submit_ampm: Union[Unset, str] = UNSET
    submit_date: Union[Unset, datetime.datetime] = UNSET
    submit_time: Union[Unset, str] = UNSET
    total_mileage: Union[Unset, float] = UNSET
    total_score: Union[Unset, int] = UNSET
    total_time: Union[Unset, float] = UNSET
    type: Union[Unset, "InspectionTypeSimpleModel"] = UNSET
    unit_number: Union[Unset, str] = UNSET
    units: Union[Unset, float] = UNSET
    vehicle_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_name = self.team_name
        floor = self.floor
        floor_unit = self.floor_unit
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        billable: Union[Unset, str] = UNSET
        if not isinstance(self.billable, Unset):
            billable = self.billable.value

        category = self.category
        comment_display = self.comment_display
        comment_public_visible: Union[Unset, List[str]] = UNSET
        if not isinstance(self.comment_public_visible, Unset):
            comment_public_visible = self.comment_public_visible

        completed_ampm = self.completed_ampm
        completed_date: Union[Unset, str] = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        completed_time = self.completed_time
        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        contact_first_name = self.contact_first_name
        contact_last_name = self.contact_last_name
        contact_middle_name = self.contact_middle_name
        desired_ampm = self.desired_ampm
        desired_date: Union[Unset, str] = UNSET
        if not isinstance(self.desired_date, Unset):
            desired_date = self.desired_date.isoformat()

        desired_time = self.desired_time
        end_mileage = self.end_mileage
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        estimated_end_time = self.estimated_end_time
        estimated_start_time = self.estimated_start_time
        gis_area_name = self.gis_area_name
        grade = self.grade
        id = self.id
        inspector_full_name = self.inspector_full_name
        inspector_id = self.inspector_id
        is_auto_assign = self.is_auto_assign
        latitude = self.latitude
        longitude = self.longitude
        major_violation = self.major_violation
        overtime = self.overtime
        priority = self.priority
        public_visible = self.public_visible
        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        record_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_type, Unset):
            record_type = self.record_type.to_dict()

        request_ampm = self.request_ampm
        request_comment = self.request_comment
        request_date: Union[Unset, str] = UNSET
        if not isinstance(self.request_date, Unset):
            request_date = self.request_date.isoformat()

        request_time = self.request_time
        requestor_first_name = self.requestor_first_name
        requestor_last_name = self.requestor_last_name
        requestor_middle_name = self.requestor_middle_name
        requestor_phone = self.requestor_phone
        requestor_phone_idd = self.requestor_phone_idd
        requestor_user_id = self.requestor_user_id
        required_inspection = self.required_inspection
        result_comment = self.result_comment
        result_type = self.result_type
        schedule_date: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_date, Unset):
            schedule_date = self.schedule_date.isoformat()

        schedule_end_ampm: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_end_ampm, Unset):
            schedule_end_ampm = self.schedule_end_ampm.value

        schedule_end_time = self.schedule_end_time
        schedule_start_ampm: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_start_ampm, Unset):
            schedule_start_ampm = self.schedule_start_ampm.value

        schedule_start_time = self.schedule_start_time
        service_provider_code = self.service_provider_code
        start_mileage = self.start_mileage
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        submit_ampm = self.submit_ampm
        submit_date: Union[Unset, str] = UNSET
        if not isinstance(self.submit_date, Unset):
            submit_date = self.submit_date.isoformat()

        submit_time = self.submit_time
        total_mileage = self.total_mileage
        total_score = self.total_score
        total_time = self.total_time
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        unit_number = self.unit_number
        units = self.units
        vehicle_id = self.vehicle_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if floor is not UNSET:
            field_dict["floor"] = floor
        if floor_unit is not UNSET:
            field_dict["floorUnit"] = floor_unit
        if address is not UNSET:
            field_dict["address"] = address
        if billable is not UNSET:
            field_dict["billable"] = billable
        if category is not UNSET:
            field_dict["category"] = category
        if comment_display is not UNSET:
            field_dict["commentDisplay"] = comment_display
        if comment_public_visible is not UNSET:
            field_dict["commentPublicVisible"] = comment_public_visible
        if completed_ampm is not UNSET:
            field_dict["completedAMPM"] = completed_ampm
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if completed_time is not UNSET:
            field_dict["completedTime"] = completed_time
        if contact is not UNSET:
            field_dict["contact"] = contact
        if contact_first_name is not UNSET:
            field_dict["contactFirstName"] = contact_first_name
        if contact_last_name is not UNSET:
            field_dict["contactLastName"] = contact_last_name
        if contact_middle_name is not UNSET:
            field_dict["contactMiddleName"] = contact_middle_name
        if desired_ampm is not UNSET:
            field_dict["desiredAMPM"] = desired_ampm
        if desired_date is not UNSET:
            field_dict["desiredDate"] = desired_date
        if desired_time is not UNSET:
            field_dict["desiredTime"] = desired_time
        if end_mileage is not UNSET:
            field_dict["endMileage"] = end_mileage
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if estimated_end_time is not UNSET:
            field_dict["estimatedEndTime"] = estimated_end_time
        if estimated_start_time is not UNSET:
            field_dict["estimatedStartTime"] = estimated_start_time
        if gis_area_name is not UNSET:
            field_dict["gisAreaName"] = gis_area_name
        if grade is not UNSET:
            field_dict["grade"] = grade
        if id is not UNSET:
            field_dict["id"] = id
        if inspector_full_name is not UNSET:
            field_dict["inspectorFullName"] = inspector_full_name
        if inspector_id is not UNSET:
            field_dict["inspectorId"] = inspector_id
        if is_auto_assign is not UNSET:
            field_dict["isAutoAssign"] = is_auto_assign
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if major_violation is not UNSET:
            field_dict["majorViolation"] = major_violation
        if overtime is not UNSET:
            field_dict["overtime"] = overtime
        if priority is not UNSET:
            field_dict["priority"] = priority
        if public_visible is not UNSET:
            field_dict["publicVisible"] = public_visible
        if record is not UNSET:
            field_dict["record"] = record
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if record_type is not UNSET:
            field_dict["recordType"] = record_type
        if request_ampm is not UNSET:
            field_dict["requestAMPM"] = request_ampm
        if request_comment is not UNSET:
            field_dict["requestComment"] = request_comment
        if request_date is not UNSET:
            field_dict["requestDate"] = request_date
        if request_time is not UNSET:
            field_dict["requestTime"] = request_time
        if requestor_first_name is not UNSET:
            field_dict["requestorFirstName"] = requestor_first_name
        if requestor_last_name is not UNSET:
            field_dict["requestorLastName"] = requestor_last_name
        if requestor_middle_name is not UNSET:
            field_dict["requestorMiddleName"] = requestor_middle_name
        if requestor_phone is not UNSET:
            field_dict["requestorPhone"] = requestor_phone
        if requestor_phone_idd is not UNSET:
            field_dict["requestorPhoneIDD"] = requestor_phone_idd
        if requestor_user_id is not UNSET:
            field_dict["requestorUserId"] = requestor_user_id
        if required_inspection is not UNSET:
            field_dict["requiredInspection"] = required_inspection
        if result_comment is not UNSET:
            field_dict["resultComment"] = result_comment
        if result_type is not UNSET:
            field_dict["resultType"] = result_type
        if schedule_date is not UNSET:
            field_dict["scheduleDate"] = schedule_date
        if schedule_end_ampm is not UNSET:
            field_dict["scheduleEndAMPM"] = schedule_end_ampm
        if schedule_end_time is not UNSET:
            field_dict["scheduleEndTime"] = schedule_end_time
        if schedule_start_ampm is not UNSET:
            field_dict["scheduleStartAMPM"] = schedule_start_ampm
        if schedule_start_time is not UNSET:
            field_dict["scheduleStartTime"] = schedule_start_time
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if start_mileage is not UNSET:
            field_dict["startMileage"] = start_mileage
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if submit_ampm is not UNSET:
            field_dict["submitAMPM"] = submit_ampm
        if submit_date is not UNSET:
            field_dict["submitDate"] = submit_date
        if submit_time is not UNSET:
            field_dict["submitTime"] = submit_time
        if total_mileage is not UNSET:
            field_dict["totalMileage"] = total_mileage
        if total_score is not UNSET:
            field_dict["totalScore"] = total_score
        if total_time is not UNSET:
            field_dict["totalTime"] = total_time
        if type is not UNSET:
            field_dict["type"] = type
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if units is not UNSET:
            field_dict["units"] = units
        if vehicle_id is not UNSET:
            field_dict["vehicleId"] = vehicle_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inspection_contact_model import InspectionContactModel
        from ..models.inspection_model_status import InspectionModelStatus
        from ..models.inspection_type_simple_model import InspectionTypeSimpleModel
        from ..models.record_address_model import RecordAddressModel
        from ..models.record_id_model import RecordIdModel
        from ..models.record_type_no_alias_model import RecordTypeNoAliasModel
        from ..models.simple_record_model import SimpleRecordModel

        d = src_dict.copy()
        team_name = d.pop("teamName", UNSET)

        floor = d.pop("floor", UNSET)

        floor_unit = d.pop("floorUnit", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, RecordAddressModel]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = RecordAddressModel.from_dict(_address)

        _billable = d.pop("billable", UNSET)
        billable: Union[Unset, InspectionModelBillable]
        if isinstance(_billable, Unset):
            billable = UNSET
        else:
            billable = InspectionModelBillable(_billable)

        category = d.pop("category", UNSET)

        comment_display = d.pop("commentDisplay", UNSET)

        comment_public_visible = cast(List[str], d.pop("commentPublicVisible", UNSET))

        completed_ampm = d.pop("completedAMPM", UNSET)

        _completed_date = d.pop("completedDate", UNSET)
        completed_date: Union[Unset, datetime.datetime]
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        completed_time = d.pop("completedTime", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, InspectionContactModel]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = InspectionContactModel.from_dict(_contact)

        contact_first_name = d.pop("contactFirstName", UNSET)

        contact_last_name = d.pop("contactLastName", UNSET)

        contact_middle_name = d.pop("contactMiddleName", UNSET)

        desired_ampm = d.pop("desiredAMPM", UNSET)

        _desired_date = d.pop("desiredDate", UNSET)
        desired_date: Union[Unset, datetime.datetime]
        if isinstance(_desired_date, Unset):
            desired_date = UNSET
        else:
            desired_date = isoparse(_desired_date)

        desired_time = d.pop("desiredTime", UNSET)

        end_mileage = d.pop("endMileage", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        estimated_end_time = d.pop("estimatedEndTime", UNSET)

        estimated_start_time = d.pop("estimatedStartTime", UNSET)

        gis_area_name = d.pop("gisAreaName", UNSET)

        grade = d.pop("grade", UNSET)

        id = d.pop("id", UNSET)

        inspector_full_name = d.pop("inspectorFullName", UNSET)

        inspector_id = d.pop("inspectorId", UNSET)

        is_auto_assign = d.pop("isAutoAssign", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        major_violation = d.pop("majorViolation", UNSET)

        overtime = d.pop("overtime", UNSET)

        priority = d.pop("priority", UNSET)

        public_visible = d.pop("publicVisible", UNSET)

        _record = d.pop("record", UNSET)
        record: Union[Unset, SimpleRecordModel]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = SimpleRecordModel.from_dict(_record)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        _record_type = d.pop("recordType", UNSET)
        record_type: Union[Unset, RecordTypeNoAliasModel]
        if isinstance(_record_type, Unset):
            record_type = UNSET
        else:
            record_type = RecordTypeNoAliasModel.from_dict(_record_type)

        request_ampm = d.pop("requestAMPM", UNSET)

        request_comment = d.pop("requestComment", UNSET)

        _request_date = d.pop("requestDate", UNSET)
        request_date: Union[Unset, datetime.datetime]
        if isinstance(_request_date, Unset):
            request_date = UNSET
        else:
            request_date = isoparse(_request_date)

        request_time = d.pop("requestTime", UNSET)

        requestor_first_name = d.pop("requestorFirstName", UNSET)

        requestor_last_name = d.pop("requestorLastName", UNSET)

        requestor_middle_name = d.pop("requestorMiddleName", UNSET)

        requestor_phone = d.pop("requestorPhone", UNSET)

        requestor_phone_idd = d.pop("requestorPhoneIDD", UNSET)

        requestor_user_id = d.pop("requestorUserId", UNSET)

        required_inspection = d.pop("requiredInspection", UNSET)

        result_comment = d.pop("resultComment", UNSET)

        result_type = d.pop("resultType", UNSET)

        _schedule_date = d.pop("scheduleDate", UNSET)
        schedule_date: Union[Unset, datetime.datetime]
        if isinstance(_schedule_date, Unset):
            schedule_date = UNSET
        else:
            schedule_date = isoparse(_schedule_date)

        _schedule_end_ampm = d.pop("scheduleEndAMPM", UNSET)
        schedule_end_ampm: Union[Unset, InspectionModelScheduleEndAMPM]
        if isinstance(_schedule_end_ampm, Unset):
            schedule_end_ampm = UNSET
        else:
            schedule_end_ampm = InspectionModelScheduleEndAMPM(_schedule_end_ampm)

        schedule_end_time = d.pop("scheduleEndTime", UNSET)

        _schedule_start_ampm = d.pop("scheduleStartAMPM", UNSET)
        schedule_start_ampm: Union[Unset, InspectionModelScheduleStartAMPM]
        if isinstance(_schedule_start_ampm, Unset):
            schedule_start_ampm = UNSET
        else:
            schedule_start_ampm = InspectionModelScheduleStartAMPM(_schedule_start_ampm)

        schedule_start_time = d.pop("scheduleStartTime", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        start_mileage = d.pop("startMileage", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InspectionModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InspectionModelStatus.from_dict(_status)

        submit_ampm = d.pop("submitAMPM", UNSET)

        _submit_date = d.pop("submitDate", UNSET)
        submit_date: Union[Unset, datetime.datetime]
        if isinstance(_submit_date, Unset):
            submit_date = UNSET
        else:
            submit_date = isoparse(_submit_date)

        submit_time = d.pop("submitTime", UNSET)

        total_mileage = d.pop("totalMileage", UNSET)

        total_score = d.pop("totalScore", UNSET)

        total_time = d.pop("totalTime", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InspectionTypeSimpleModel]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InspectionTypeSimpleModel.from_dict(_type)

        unit_number = d.pop("unitNumber", UNSET)

        units = d.pop("units", UNSET)

        vehicle_id = d.pop("vehicleId", UNSET)

        inspection_model = cls(
            team_name=team_name,
            floor=floor,
            floor_unit=floor_unit,
            address=address,
            billable=billable,
            category=category,
            comment_display=comment_display,
            comment_public_visible=comment_public_visible,
            completed_ampm=completed_ampm,
            completed_date=completed_date,
            completed_time=completed_time,
            contact=contact,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            contact_middle_name=contact_middle_name,
            desired_ampm=desired_ampm,
            desired_date=desired_date,
            desired_time=desired_time,
            end_mileage=end_mileage,
            end_time=end_time,
            estimated_end_time=estimated_end_time,
            estimated_start_time=estimated_start_time,
            gis_area_name=gis_area_name,
            grade=grade,
            id=id,
            inspector_full_name=inspector_full_name,
            inspector_id=inspector_id,
            is_auto_assign=is_auto_assign,
            latitude=latitude,
            longitude=longitude,
            major_violation=major_violation,
            overtime=overtime,
            priority=priority,
            public_visible=public_visible,
            record=record,
            record_id=record_id,
            record_type=record_type,
            request_ampm=request_ampm,
            request_comment=request_comment,
            request_date=request_date,
            request_time=request_time,
            requestor_first_name=requestor_first_name,
            requestor_last_name=requestor_last_name,
            requestor_middle_name=requestor_middle_name,
            requestor_phone=requestor_phone,
            requestor_phone_idd=requestor_phone_idd,
            requestor_user_id=requestor_user_id,
            required_inspection=required_inspection,
            result_comment=result_comment,
            result_type=result_type,
            schedule_date=schedule_date,
            schedule_end_ampm=schedule_end_ampm,
            schedule_end_time=schedule_end_time,
            schedule_start_ampm=schedule_start_ampm,
            schedule_start_time=schedule_start_time,
            service_provider_code=service_provider_code,
            start_mileage=start_mileage,
            start_time=start_time,
            status=status,
            submit_ampm=submit_ampm,
            submit_date=submit_date,
            submit_time=submit_time,
            total_mileage=total_mileage,
            total_score=total_score,
            total_time=total_time,
            type=type,
            unit_number=unit_number,
            units=units,
            vehicle_id=vehicle_id,
        )

        inspection_model.additional_properties = d
        return inspection_model

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
