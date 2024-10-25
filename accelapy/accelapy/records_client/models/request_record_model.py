import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.request_record_model_created_by_cloning import RequestRecordModelCreatedByCloning
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_attribute_model import CustomAttributeModel
    from ..models.license_professional_model import LicenseProfessionalModel
    from ..models.parcel_model_1 import ParcelModel1
    from ..models.record_address_model import RecordAddressModel
    from ..models.record_contact_model import RecordContactModel
    from ..models.record_expiration_model import RecordExpirationModel
    from ..models.record_type_model import RecordTypeModel
    from ..models.ref_owner_model import RefOwnerModel
    from ..models.request_record_model_construction_type import RequestRecordModelConstructionType
    from ..models.request_record_model_priority import RequestRecordModelPriority
    from ..models.request_record_model_reported_channel import RequestRecordModelReportedChannel
    from ..models.request_record_model_reported_type import RequestRecordModelReportedType
    from ..models.request_record_model_severity import RequestRecordModelSeverity
    from ..models.request_record_model_status import RequestRecordModelStatus
    from ..models.request_record_model_status_reason import RequestRecordModelStatusReason
    from ..models.table_model import TableModel


T = TypeVar("T", bound="RequestRecordModel")


@_attrs_define
class RequestRecordModel:
    """
    Attributes:
        actual_production_unit (Union[Unset, float]): Estimated cost per production unit.
        addresses (Union[Unset, List['RecordAddressModel']]):
        appearance_date (Union[Unset, datetime.datetime]): The date for a hearing appearance.
        appearance_day_of_week (Union[Unset, str]): The day for a hearing appearance.
        assigned_date (Union[Unset, datetime.datetime]): The date the application was assigned.
        assigned_to_department (Union[Unset, str]): The department responsible for the action. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        assigned_user (Union[Unset, str]): The staff member responsible for the action.
        booking (Union[Unset, bool]): Indicates whether or not there was a booking in addition to a citation.
        closed_by_department (Union[Unset, str]): The department responsible for closing the record. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        closed_by_user (Union[Unset, str]): The staff member responsible for closure.
        closed_date (Union[Unset, datetime.datetime]): The date the application was closed.
        complete_date (Union[Unset, datetime.datetime]): The date the application was completed.
        completed_by_department (Union[Unset, str]): The department responsible for completion. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        completed_by_user (Union[Unset, str]): The staff member responsible for completion.
        construction_type (Union[Unset, RequestRecordModelConstructionType]): The US Census Bureau construction type
            code. See [Get All Record Construction Types](./api-
            settings.html#operation/v4.get.settings.records.constructionTypes).
        contact (Union[Unset, RecordContactModel]):
        cost_per_unit (Union[Unset, float]): The cost for one unit associated to the record.
        created_by (Union[Unset, str]): The unique user id of the individual that created the entry.
        created_by_cloning (Union[Unset, RequestRecordModelCreatedByCloning]): Indictes whether or not the record was
            cloned.
        custom_forms (Union[Unset, List['CustomAttributeModel']]):
        custom_id (Union[Unset, str]): An ID based on a different numbering convention from the numbering convention
            used by the record ID (xxxxx-xx-xxxxx). Civic Platform auto-generates and applies an alternate ID value when you
            submit a new application.
        custom_tables (Union[Unset, List['TableModel']]):
        defendant_signature (Union[Unset, bool]): Indicates whether or not a defendant's signature has been obtained.
        description (Union[Unset, str]): The description of the record or item.
        enforce_department (Union[Unset, str]): The name of the department responsible for enforcement. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        enforce_user (Union[Unset, str]): Name of the enforcement officer.
        enforce_user_id (Union[Unset, str]): ID number of the enforcement officer.
        estimated_cost_per_unit (Union[Unset, float]): The estimated cost per unit.
        estimated_due_date (Union[Unset, datetime.datetime]): The estimated date of completion.
        estimated_production_unit (Union[Unset, float]): The estimated number of production units.
        estimated_total_job_cost (Union[Unset, float]): The estimated cost of the job.
        first_issued_date (Union[Unset, datetime.datetime]): The first issued date for license
        housing_units (Union[Unset, int]): The number of housing units.
        id (Union[Unset, str]): The record system id assigned by the Civic Platform server.
        initiated_product (Union[Unset, str]): The product or app that created the record. If initiatedProduct is null
            or not specified in the request, the default is "AV360" (Civic Platform application).

            Added in Civic Platform version: 9.2.0
        in_possession_time (Union[Unset, float]): The application level in possession time of the time tracking feature.
        infraction (Union[Unset, bool]): Indicates whether or not an infraction occurred.
        inspector_department (Union[Unset, str]): The name of the department where the inspector works. See [Get All
            Departments](./api-settings.html#operation/v4.get.settings.departments).
        inspector_id (Union[Unset, str]): The ID number of the inspector. See [Get All Inspectors](./api-
            inspections.html#operation/v4.get.inspectors).
        inspector_name (Union[Unset, str]): The name of the inspector. See [Get All Inspectors](./api-
            inspections.html#operation/v4.get.inspectors).
        job_value (Union[Unset, float]): The value of the job.
        misdemeanor (Union[Unset, bool]): Indicates whether or not a misdemeanor occurred.
        module (Union[Unset, str]): The module the record belongs to. See [Get All Modules](./api-
            settings.html#operation/v4.get.settings.modules).
        name (Union[Unset, str]): The name associated to the record.
        number_of_buildings (Union[Unset, int]): The number of buildings.
        offense_witnessed (Union[Unset, bool]): Indicates whether or not  there was a witness to the alleged offense.
        owner (Union[Unset, List['RefOwnerModel']]):
        parcel (Union[Unset, List['ParcelModel1']]):
        priority (Union[Unset, RequestRecordModelPriority]): The priority level assigned to the record. See [Get All
            Priorities](./api-settings.html#operation/v4.get.settings.priorities).
        professional (Union[Unset, List['LicenseProfessionalModel']]):
        public_owned (Union[Unset, bool]): Indicates whether or not the record is for the public.
        record_class (Union[Unset, str]): General information about the record.
        renewal_info (Union[Unset, RecordExpirationModel]):
        reported_channel (Union[Unset, RequestRecordModelReportedChannel]): The incoming channel through which the
            applicant submitted the application.
        reported_date (Union[Unset, datetime.datetime]): The date the complaint was reported.
        reported_type (Union[Unset, RequestRecordModelReportedType]): The type of complaint or incident being reported.
        scheduled_date (Union[Unset, datetime.datetime]): The date when the inspection gets scheduled.
        severity (Union[Unset, RequestRecordModelSeverity]): Indicates the severity of the condition.
        short_notes (Union[Unset, str]): A brief note about the record subject.
        status (Union[Unset, RequestRecordModelStatus]): The record status.
        status_reason (Union[Unset, RequestRecordModelStatusReason]): 	The reason for the status setting on the record.
        total_job_cost (Union[Unset, float]): The combination of work order assignments (labor) and costs.
        type (Union[Unset, RecordTypeModel]):
        undistributed_cost (Union[Unset, float]): The undistributed costs for this work order.
    """

    actual_production_unit: Union[Unset, float] = UNSET
    addresses: Union[Unset, List["RecordAddressModel"]] = UNSET
    appearance_date: Union[Unset, datetime.datetime] = UNSET
    appearance_day_of_week: Union[Unset, str] = UNSET
    assigned_date: Union[Unset, datetime.datetime] = UNSET
    assigned_to_department: Union[Unset, str] = UNSET
    assigned_user: Union[Unset, str] = UNSET
    booking: Union[Unset, bool] = UNSET
    closed_by_department: Union[Unset, str] = UNSET
    closed_by_user: Union[Unset, str] = UNSET
    closed_date: Union[Unset, datetime.datetime] = UNSET
    complete_date: Union[Unset, datetime.datetime] = UNSET
    completed_by_department: Union[Unset, str] = UNSET
    completed_by_user: Union[Unset, str] = UNSET
    construction_type: Union[Unset, "RequestRecordModelConstructionType"] = UNSET
    contact: Union[Unset, "RecordContactModel"] = UNSET
    cost_per_unit: Union[Unset, float] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_cloning: Union[Unset, RequestRecordModelCreatedByCloning] = UNSET
    custom_forms: Union[Unset, List["CustomAttributeModel"]] = UNSET
    custom_id: Union[Unset, str] = UNSET
    custom_tables: Union[Unset, List["TableModel"]] = UNSET
    defendant_signature: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    enforce_department: Union[Unset, str] = UNSET
    enforce_user: Union[Unset, str] = UNSET
    enforce_user_id: Union[Unset, str] = UNSET
    estimated_cost_per_unit: Union[Unset, float] = UNSET
    estimated_due_date: Union[Unset, datetime.datetime] = UNSET
    estimated_production_unit: Union[Unset, float] = UNSET
    estimated_total_job_cost: Union[Unset, float] = UNSET
    first_issued_date: Union[Unset, datetime.datetime] = UNSET
    housing_units: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    initiated_product: Union[Unset, str] = UNSET
    in_possession_time: Union[Unset, float] = UNSET
    infraction: Union[Unset, bool] = UNSET
    inspector_department: Union[Unset, str] = UNSET
    inspector_id: Union[Unset, str] = UNSET
    inspector_name: Union[Unset, str] = UNSET
    job_value: Union[Unset, float] = UNSET
    misdemeanor: Union[Unset, bool] = UNSET
    module: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    number_of_buildings: Union[Unset, int] = UNSET
    offense_witnessed: Union[Unset, bool] = UNSET
    owner: Union[Unset, List["RefOwnerModel"]] = UNSET
    parcel: Union[Unset, List["ParcelModel1"]] = UNSET
    priority: Union[Unset, "RequestRecordModelPriority"] = UNSET
    professional: Union[Unset, List["LicenseProfessionalModel"]] = UNSET
    public_owned: Union[Unset, bool] = UNSET
    record_class: Union[Unset, str] = UNSET
    renewal_info: Union[Unset, "RecordExpirationModel"] = UNSET
    reported_channel: Union[Unset, "RequestRecordModelReportedChannel"] = UNSET
    reported_date: Union[Unset, datetime.datetime] = UNSET
    reported_type: Union[Unset, "RequestRecordModelReportedType"] = UNSET
    scheduled_date: Union[Unset, datetime.datetime] = UNSET
    severity: Union[Unset, "RequestRecordModelSeverity"] = UNSET
    short_notes: Union[Unset, str] = UNSET
    status: Union[Unset, "RequestRecordModelStatus"] = UNSET
    status_reason: Union[Unset, "RequestRecordModelStatusReason"] = UNSET
    total_job_cost: Union[Unset, float] = UNSET
    type: Union[Unset, "RecordTypeModel"] = UNSET
    undistributed_cost: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actual_production_unit = self.actual_production_unit
        addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()

                addresses.append(addresses_item)

        appearance_date: Union[Unset, str] = UNSET
        if not isinstance(self.appearance_date, Unset):
            appearance_date = self.appearance_date.isoformat()

        appearance_day_of_week = self.appearance_day_of_week
        assigned_date: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_date, Unset):
            assigned_date = self.assigned_date.isoformat()

        assigned_to_department = self.assigned_to_department
        assigned_user = self.assigned_user
        booking = self.booking
        closed_by_department = self.closed_by_department
        closed_by_user = self.closed_by_user
        closed_date: Union[Unset, str] = UNSET
        if not isinstance(self.closed_date, Unset):
            closed_date = self.closed_date.isoformat()

        complete_date: Union[Unset, str] = UNSET
        if not isinstance(self.complete_date, Unset):
            complete_date = self.complete_date.isoformat()

        completed_by_department = self.completed_by_department
        completed_by_user = self.completed_by_user
        construction_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.construction_type, Unset):
            construction_type = self.construction_type.to_dict()

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        cost_per_unit = self.cost_per_unit
        created_by = self.created_by
        created_by_cloning: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_cloning, Unset):
            created_by_cloning = self.created_by_cloning.value

        custom_forms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_forms, Unset):
            custom_forms = []
            for custom_forms_item_data in self.custom_forms:
                custom_forms_item = custom_forms_item_data.to_dict()

                custom_forms.append(custom_forms_item)

        custom_id = self.custom_id
        custom_tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_tables, Unset):
            custom_tables = []
            for custom_tables_item_data in self.custom_tables:
                custom_tables_item = custom_tables_item_data.to_dict()

                custom_tables.append(custom_tables_item)

        defendant_signature = self.defendant_signature
        description = self.description
        enforce_department = self.enforce_department
        enforce_user = self.enforce_user
        enforce_user_id = self.enforce_user_id
        estimated_cost_per_unit = self.estimated_cost_per_unit
        estimated_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_due_date, Unset):
            estimated_due_date = self.estimated_due_date.isoformat()

        estimated_production_unit = self.estimated_production_unit
        estimated_total_job_cost = self.estimated_total_job_cost
        first_issued_date: Union[Unset, str] = UNSET
        if not isinstance(self.first_issued_date, Unset):
            first_issued_date = self.first_issued_date.isoformat()

        housing_units = self.housing_units
        id = self.id
        initiated_product = self.initiated_product
        in_possession_time = self.in_possession_time
        infraction = self.infraction
        inspector_department = self.inspector_department
        inspector_id = self.inspector_id
        inspector_name = self.inspector_name
        job_value = self.job_value
        misdemeanor = self.misdemeanor
        module = self.module
        name = self.name
        number_of_buildings = self.number_of_buildings
        offense_witnessed = self.offense_witnessed
        owner: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = []
            for owner_item_data in self.owner:
                owner_item = owner_item_data.to_dict()

                owner.append(owner_item)

        parcel: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parcel, Unset):
            parcel = []
            for parcel_item_data in self.parcel:
                parcel_item = parcel_item_data.to_dict()

                parcel.append(parcel_item)

        priority: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        professional: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.professional, Unset):
            professional = []
            for professional_item_data in self.professional:
                professional_item = professional_item_data.to_dict()

                professional.append(professional_item)

        public_owned = self.public_owned
        record_class = self.record_class
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

        total_job_cost = self.total_job_cost
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        undistributed_cost = self.undistributed_cost

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_production_unit is not UNSET:
            field_dict["actualProductionUnit"] = actual_production_unit
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if appearance_date is not UNSET:
            field_dict["appearanceDate"] = appearance_date
        if appearance_day_of_week is not UNSET:
            field_dict["appearanceDayOfWeek"] = appearance_day_of_week
        if assigned_date is not UNSET:
            field_dict["assignedDate"] = assigned_date
        if assigned_to_department is not UNSET:
            field_dict["assignedToDepartment"] = assigned_to_department
        if assigned_user is not UNSET:
            field_dict["assignedUser"] = assigned_user
        if booking is not UNSET:
            field_dict["booking"] = booking
        if closed_by_department is not UNSET:
            field_dict["closedByDepartment"] = closed_by_department
        if closed_by_user is not UNSET:
            field_dict["closedByUser"] = closed_by_user
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if complete_date is not UNSET:
            field_dict["completeDate"] = complete_date
        if completed_by_department is not UNSET:
            field_dict["completedByDepartment"] = completed_by_department
        if completed_by_user is not UNSET:
            field_dict["completedByUser"] = completed_by_user
        if construction_type is not UNSET:
            field_dict["constructionType"] = construction_type
        if contact is not UNSET:
            field_dict["contact"] = contact
        if cost_per_unit is not UNSET:
            field_dict["costPerUnit"] = cost_per_unit
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_cloning is not UNSET:
            field_dict["createdByCloning"] = created_by_cloning
        if custom_forms is not UNSET:
            field_dict["customForms"] = custom_forms
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if custom_tables is not UNSET:
            field_dict["customTables"] = custom_tables
        if defendant_signature is not UNSET:
            field_dict["defendantSignature"] = defendant_signature
        if description is not UNSET:
            field_dict["description"] = description
        if enforce_department is not UNSET:
            field_dict["enforceDepartment"] = enforce_department
        if enforce_user is not UNSET:
            field_dict["enforceUser"] = enforce_user
        if enforce_user_id is not UNSET:
            field_dict["enforceUserId"] = enforce_user_id
        if estimated_cost_per_unit is not UNSET:
            field_dict["estimatedCostPerUnit"] = estimated_cost_per_unit
        if estimated_due_date is not UNSET:
            field_dict["estimatedDueDate"] = estimated_due_date
        if estimated_production_unit is not UNSET:
            field_dict["estimatedProductionUnit"] = estimated_production_unit
        if estimated_total_job_cost is not UNSET:
            field_dict["estimatedTotalJobCost"] = estimated_total_job_cost
        if first_issued_date is not UNSET:
            field_dict["firstIssuedDate"] = first_issued_date
        if housing_units is not UNSET:
            field_dict["housingUnits"] = housing_units
        if id is not UNSET:
            field_dict["id"] = id
        if initiated_product is not UNSET:
            field_dict["initiatedProduct"] = initiated_product
        if in_possession_time is not UNSET:
            field_dict["inPossessionTime"] = in_possession_time
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
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
        if number_of_buildings is not UNSET:
            field_dict["numberOfBuildings"] = number_of_buildings
        if offense_witnessed is not UNSET:
            field_dict["offenseWitnessed"] = offense_witnessed
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parcel is not UNSET:
            field_dict["parcel"] = parcel
        if priority is not UNSET:
            field_dict["priority"] = priority
        if professional is not UNSET:
            field_dict["professional"] = professional
        if public_owned is not UNSET:
            field_dict["publicOwned"] = public_owned
        if record_class is not UNSET:
            field_dict["recordClass"] = record_class
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
        if total_job_cost is not UNSET:
            field_dict["totalJobCost"] = total_job_cost
        if type is not UNSET:
            field_dict["type"] = type
        if undistributed_cost is not UNSET:
            field_dict["undistributedCost"] = undistributed_cost

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_attribute_model import CustomAttributeModel
        from ..models.license_professional_model import LicenseProfessionalModel
        from ..models.parcel_model_1 import ParcelModel1
        from ..models.record_address_model import RecordAddressModel
        from ..models.record_contact_model import RecordContactModel
        from ..models.record_expiration_model import RecordExpirationModel
        from ..models.record_type_model import RecordTypeModel
        from ..models.ref_owner_model import RefOwnerModel
        from ..models.request_record_model_construction_type import RequestRecordModelConstructionType
        from ..models.request_record_model_priority import RequestRecordModelPriority
        from ..models.request_record_model_reported_channel import RequestRecordModelReportedChannel
        from ..models.request_record_model_reported_type import RequestRecordModelReportedType
        from ..models.request_record_model_severity import RequestRecordModelSeverity
        from ..models.request_record_model_status import RequestRecordModelStatus
        from ..models.request_record_model_status_reason import RequestRecordModelStatusReason
        from ..models.table_model import TableModel

        d = src_dict.copy()
        actual_production_unit = d.pop("actualProductionUnit", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = RecordAddressModel.from_dict(addresses_item_data)

            addresses.append(addresses_item)

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

        assigned_user = d.pop("assignedUser", UNSET)

        booking = d.pop("booking", UNSET)

        closed_by_department = d.pop("closedByDepartment", UNSET)

        closed_by_user = d.pop("closedByUser", UNSET)

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

        completed_by_user = d.pop("completedByUser", UNSET)

        _construction_type = d.pop("constructionType", UNSET)
        construction_type: Union[Unset, RequestRecordModelConstructionType]
        if isinstance(_construction_type, Unset):
            construction_type = UNSET
        else:
            construction_type = RequestRecordModelConstructionType.from_dict(_construction_type)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, RecordContactModel]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = RecordContactModel.from_dict(_contact)

        cost_per_unit = d.pop("costPerUnit", UNSET)

        created_by = d.pop("createdBy", UNSET)

        _created_by_cloning = d.pop("createdByCloning", UNSET)
        created_by_cloning: Union[Unset, RequestRecordModelCreatedByCloning]
        if isinstance(_created_by_cloning, Unset):
            created_by_cloning = UNSET
        else:
            created_by_cloning = RequestRecordModelCreatedByCloning(_created_by_cloning)

        custom_forms = []
        _custom_forms = d.pop("customForms", UNSET)
        for custom_forms_item_data in _custom_forms or []:
            custom_forms_item = CustomAttributeModel.from_dict(custom_forms_item_data)

            custom_forms.append(custom_forms_item)

        custom_id = d.pop("customId", UNSET)

        custom_tables = []
        _custom_tables = d.pop("customTables", UNSET)
        for custom_tables_item_data in _custom_tables or []:
            custom_tables_item = TableModel.from_dict(custom_tables_item_data)

            custom_tables.append(custom_tables_item)

        defendant_signature = d.pop("defendantSignature", UNSET)

        description = d.pop("description", UNSET)

        enforce_department = d.pop("enforceDepartment", UNSET)

        enforce_user = d.pop("enforceUser", UNSET)

        enforce_user_id = d.pop("enforceUserId", UNSET)

        estimated_cost_per_unit = d.pop("estimatedCostPerUnit", UNSET)

        _estimated_due_date = d.pop("estimatedDueDate", UNSET)
        estimated_due_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_due_date, Unset):
            estimated_due_date = UNSET
        else:
            estimated_due_date = isoparse(_estimated_due_date)

        estimated_production_unit = d.pop("estimatedProductionUnit", UNSET)

        estimated_total_job_cost = d.pop("estimatedTotalJobCost", UNSET)

        _first_issued_date = d.pop("firstIssuedDate", UNSET)
        first_issued_date: Union[Unset, datetime.datetime]
        if isinstance(_first_issued_date, Unset):
            first_issued_date = UNSET
        else:
            first_issued_date = isoparse(_first_issued_date)

        housing_units = d.pop("housingUnits", UNSET)

        id = d.pop("id", UNSET)

        initiated_product = d.pop("initiatedProduct", UNSET)

        in_possession_time = d.pop("inPossessionTime", UNSET)

        infraction = d.pop("infraction", UNSET)

        inspector_department = d.pop("inspectorDepartment", UNSET)

        inspector_id = d.pop("inspectorId", UNSET)

        inspector_name = d.pop("inspectorName", UNSET)

        job_value = d.pop("jobValue", UNSET)

        misdemeanor = d.pop("misdemeanor", UNSET)

        module = d.pop("module", UNSET)

        name = d.pop("name", UNSET)

        number_of_buildings = d.pop("numberOfBuildings", UNSET)

        offense_witnessed = d.pop("offenseWitnessed", UNSET)

        owner = []
        _owner = d.pop("owner", UNSET)
        for owner_item_data in _owner or []:
            owner_item = RefOwnerModel.from_dict(owner_item_data)

            owner.append(owner_item)

        parcel = []
        _parcel = d.pop("parcel", UNSET)
        for parcel_item_data in _parcel or []:
            parcel_item = ParcelModel1.from_dict(parcel_item_data)

            parcel.append(parcel_item)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, RequestRecordModelPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = RequestRecordModelPriority.from_dict(_priority)

        professional = []
        _professional = d.pop("professional", UNSET)
        for professional_item_data in _professional or []:
            professional_item = LicenseProfessionalModel.from_dict(professional_item_data)

            professional.append(professional_item)

        public_owned = d.pop("publicOwned", UNSET)

        record_class = d.pop("recordClass", UNSET)

        _renewal_info = d.pop("renewalInfo", UNSET)
        renewal_info: Union[Unset, RecordExpirationModel]
        if isinstance(_renewal_info, Unset):
            renewal_info = UNSET
        else:
            renewal_info = RecordExpirationModel.from_dict(_renewal_info)

        _reported_channel = d.pop("reportedChannel", UNSET)
        reported_channel: Union[Unset, RequestRecordModelReportedChannel]
        if isinstance(_reported_channel, Unset):
            reported_channel = UNSET
        else:
            reported_channel = RequestRecordModelReportedChannel.from_dict(_reported_channel)

        _reported_date = d.pop("reportedDate", UNSET)
        reported_date: Union[Unset, datetime.datetime]
        if isinstance(_reported_date, Unset):
            reported_date = UNSET
        else:
            reported_date = isoparse(_reported_date)

        _reported_type = d.pop("reportedType", UNSET)
        reported_type: Union[Unset, RequestRecordModelReportedType]
        if isinstance(_reported_type, Unset):
            reported_type = UNSET
        else:
            reported_type = RequestRecordModelReportedType.from_dict(_reported_type)

        _scheduled_date = d.pop("scheduledDate", UNSET)
        scheduled_date: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_date, Unset):
            scheduled_date = UNSET
        else:
            scheduled_date = isoparse(_scheduled_date)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, RequestRecordModelSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = RequestRecordModelSeverity.from_dict(_severity)

        short_notes = d.pop("shortNotes", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RequestRecordModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestRecordModelStatus.from_dict(_status)

        _status_reason = d.pop("statusReason", UNSET)
        status_reason: Union[Unset, RequestRecordModelStatusReason]
        if isinstance(_status_reason, Unset):
            status_reason = UNSET
        else:
            status_reason = RequestRecordModelStatusReason.from_dict(_status_reason)

        total_job_cost = d.pop("totalJobCost", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RecordTypeModel]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RecordTypeModel.from_dict(_type)

        undistributed_cost = d.pop("undistributedCost", UNSET)

        request_record_model = cls(
            actual_production_unit=actual_production_unit,
            addresses=addresses,
            appearance_date=appearance_date,
            appearance_day_of_week=appearance_day_of_week,
            assigned_date=assigned_date,
            assigned_to_department=assigned_to_department,
            assigned_user=assigned_user,
            booking=booking,
            closed_by_department=closed_by_department,
            closed_by_user=closed_by_user,
            closed_date=closed_date,
            complete_date=complete_date,
            completed_by_department=completed_by_department,
            completed_by_user=completed_by_user,
            construction_type=construction_type,
            contact=contact,
            cost_per_unit=cost_per_unit,
            created_by=created_by,
            created_by_cloning=created_by_cloning,
            custom_forms=custom_forms,
            custom_id=custom_id,
            custom_tables=custom_tables,
            defendant_signature=defendant_signature,
            description=description,
            enforce_department=enforce_department,
            enforce_user=enforce_user,
            enforce_user_id=enforce_user_id,
            estimated_cost_per_unit=estimated_cost_per_unit,
            estimated_due_date=estimated_due_date,
            estimated_production_unit=estimated_production_unit,
            estimated_total_job_cost=estimated_total_job_cost,
            first_issued_date=first_issued_date,
            housing_units=housing_units,
            id=id,
            initiated_product=initiated_product,
            in_possession_time=in_possession_time,
            infraction=infraction,
            inspector_department=inspector_department,
            inspector_id=inspector_id,
            inspector_name=inspector_name,
            job_value=job_value,
            misdemeanor=misdemeanor,
            module=module,
            name=name,
            number_of_buildings=number_of_buildings,
            offense_witnessed=offense_witnessed,
            owner=owner,
            parcel=parcel,
            priority=priority,
            professional=professional,
            public_owned=public_owned,
            record_class=record_class,
            renewal_info=renewal_info,
            reported_channel=reported_channel,
            reported_date=reported_date,
            reported_type=reported_type,
            scheduled_date=scheduled_date,
            severity=severity,
            short_notes=short_notes,
            status=status,
            status_reason=status_reason,
            total_job_cost=total_job_cost,
            type=type,
            undistributed_cost=undistributed_cost,
        )

        request_record_model.additional_properties = d
        return request_record_model

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
