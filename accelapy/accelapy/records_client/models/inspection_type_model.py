from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inspection_type_model_allow_fail_checklist_items import InspectionTypeModelAllowFailChecklistItems
from ..models.inspection_type_model_allow_multi_inspections import InspectionTypeModelAllowMultiInspections
from ..models.inspection_type_model_carryover_flag import InspectionTypeModelCarryoverFlag
from ..models.inspection_type_model_flow_enabled_flag import InspectionTypeModelFlowEnabledFlag
from ..models.inspection_type_model_has_cancel_permission import InspectionTypeModelHasCancelPermission
from ..models.inspection_type_model_has_flow_flag import InspectionTypeModelHasFlowFlag
from ..models.inspection_type_model_has_next_inspection_advance import InspectionTypeModelHasNextInspectionAdvance
from ..models.inspection_type_model_has_reschdule_permission import InspectionTypeModelHasReschdulePermission
from ..models.inspection_type_model_has_schdule_permission import InspectionTypeModelHasSchdulePermission
from ..models.inspection_type_model_inspection_editable import InspectionTypeModelInspectionEditable
from ..models.inspection_type_model_is_auto_assign import InspectionTypeModelIsAutoAssign
from ..models.inspection_type_model_is_required import InspectionTypeModelIsRequired
from ..models.inspection_type_model_public_visible import InspectionTypeModelPublicVisible
from ..models.inspection_type_model_total_score_option import InspectionTypeModelTotalScoreOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.department_model import DepartmentModel
    from ..models.inspection_restriction_model import InspectionRestrictionModel
    from ..models.inspection_type_associations_model import InspectionTypeAssociationsModel
    from ..models.inspection_type_model_group_name import InspectionTypeModelGroupName
    from ..models.r_guide_sheet_group_model import RGuideSheetGroupModel


T = TypeVar("T", bound="InspectionTypeModel")


@_attrs_define
class InspectionTypeModel:
    """
    Attributes:
        allow_fail_checklist_items (Union[Unset, InspectionTypeModelAllowFailChecklistItems]): Indicates whether or not
            to allow inspection to pass with failed checklist items for the current inspection type or from previous
            inspections.
        allow_multi_inspections (Union[Unset, InspectionTypeModelAllowMultiInspections]): Indicates whether or not to
            allow the scheduling of multiple inspections for this inspection type.
        associations (Union[Unset, InspectionTypeAssociationsModel]):
        cancel_restriction (Union[Unset, InspectionRestrictionModel]):
        carryover_flag (Union[Unset, InspectionTypeModelCarryoverFlag]): Indicates how failed guidesheet items for an
            inspection type are carried over to the next inspection guidesheet.

            NULL or empty string : Guidesheet items are not carried over.

            "A" : Automatic carry-over of failed guidesheet items to the next inspection guidesheet item.
        default_department (Union[Unset, DepartmentModel]):
        disciplines (Union[Unset, List[str]]): The inspection disciplines assigned to the inspection type.
        flow_enabled_flag (Union[Unset, InspectionTypeModelFlowEnabledFlag]): Indicates whether or not to include the
            inspection in the inspection flow process.
        grade (Union[Unset, str]): The name of the inspection grade.
        group (Union[Unset, str]): The name of a group of inspection types.
        group_name (Union[Unset, InspectionTypeModelGroupName]): The descriptive name associated to an inspection group
            code.
        guide_group (Union[Unset, RGuideSheetGroupModel]):
        has_cancel_permission (Union[Unset, InspectionTypeModelHasCancelPermission]): Indicates whether or not the user
            can reschedule the inspection.
        has_flow_flag (Union[Unset, InspectionTypeModelHasFlowFlag]): Indicates whether or not to include the inspection
            in the inspection flow process.
        has_next_inspection_advance (Union[Unset, InspectionTypeModelHasNextInspectionAdvance]): Indicates whether or
            not the next inspection can be scheduled in advance.
        has_reschdule_permission (Union[Unset, InspectionTypeModelHasReschdulePermission]): Indicates whether or not the
            user can reschedule the inspection.
        has_schdule_permission (Union[Unset, InspectionTypeModelHasSchdulePermission]): Indicates whether or not the
            user can schedule the inspection. Note that hasSchdulePermission returns "Y" if
            result.inspectionTypes.schdulePermission is either "REQUEST_ONLY_PENDING", "REQUEST_SAME_DAY_NEXT_DAY", or
            "SCHEDULE_USING_CALENDAR". If result.inspectionTypes.schdulePermission is "NONE" or null, hasSchdulePermission
            returns "N".
        id (Union[Unset, int]): The inspection type system id assigned by the Civic Platform server.
        inspection_editable (Union[Unset, InspectionTypeModelInspectionEditable]): Indicates whether or not inspection
            result, grade or checklist can be edited.
        is_auto_assign (Union[Unset, InspectionTypeModelIsAutoAssign]): Indicates whether or not you want to
            automatically reschedule the inspection when the previous inspection status attains Approved status.
        is_required (Union[Unset, InspectionTypeModelIsRequired]): Indicates whether or not the information is required.
        ivr_number (Union[Unset, int]): The IVR (Interactive Voice Response) number assigned to the inspection type.

            Added in Civic Platform 9.3.0
        max_points (Union[Unset, float]): The number of points allowed for an inspection, after which the inspection
            fails.
        priority (Union[Unset, str]): The priority level assigned to the inspection type.
        public_visible (Union[Unset, InspectionTypeModelPublicVisible]): Indicates whether or not Accela Citizen Access
            users can view comment about the inspection results.
        referece_number (Union[Unset, str]): The reference number associated with an inspection.
        reschedule_restriction (Union[Unset, InspectionRestrictionModel]):
        result_group (Union[Unset, str]): The name of a grouping of Inspection results, usually indicative of a range of
            inspection scores.
        schdule_permission (Union[Unset, str]): Returns one of the scheduling permissions in Citizen Access:

            NONE - Does not allow public users to schedule this inspection type online.

            REQUEST_ONLY_PENDING - Only allows public users to request for an inspection online. The agency coordinates the
            appointment for the inspection date and time.

            REQUEST_SAME_DAY_NEXT_DAY - Allows public users to request an inspection for the same day, next day, or next
            available day, based on the inspection type calendar parameters defined on the inspection type.

            SCHEDULE_USING_CALENDAR - Allows public users to schedule inspections based on the availability on the
            inspection type calendar.
        text (Union[Unset, str]): The localized display text.
        total_score (Union[Unset, int]): The overall score of the inspection that includes the inspection result,
            inspection grade, checklist total score and checklist major violation option.
        total_score_option (Union[Unset, InspectionTypeModelTotalScoreOption]): Indicates the method for calculating
            total scores of checklist items. There are four options:

            TOTAL - Gets the total score of all checklists as the inspection score.

            MAX - Gets the max score of all checklists as the inspection score.

            MIN - Gets the min score of all checklists as the inspection score.

            AVG - Gets the average score of all checklists as the inspection score.

            SUBTRACT - Subtracts the total score of all the checklist items from the Total Score defined for the inspection
            type.
        unit_number (Union[Unset, str]): The number of time units (see timeUnitDuration) comprising an inspection.
        units (Union[Unset, float]): The amount of time comprising the smallest time unit for conducting an inspection.
        value (Union[Unset, str]): The value for the specified parameter.
    """

    allow_fail_checklist_items: Union[Unset, InspectionTypeModelAllowFailChecklistItems] = UNSET
    allow_multi_inspections: Union[Unset, InspectionTypeModelAllowMultiInspections] = UNSET
    associations: Union[Unset, "InspectionTypeAssociationsModel"] = UNSET
    cancel_restriction: Union[Unset, "InspectionRestrictionModel"] = UNSET
    carryover_flag: Union[Unset, InspectionTypeModelCarryoverFlag] = UNSET
    default_department: Union[Unset, "DepartmentModel"] = UNSET
    disciplines: Union[Unset, List[str]] = UNSET
    flow_enabled_flag: Union[Unset, InspectionTypeModelFlowEnabledFlag] = UNSET
    grade: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    group_name: Union[Unset, "InspectionTypeModelGroupName"] = UNSET
    guide_group: Union[Unset, "RGuideSheetGroupModel"] = UNSET
    has_cancel_permission: Union[Unset, InspectionTypeModelHasCancelPermission] = UNSET
    has_flow_flag: Union[Unset, InspectionTypeModelHasFlowFlag] = UNSET
    has_next_inspection_advance: Union[Unset, InspectionTypeModelHasNextInspectionAdvance] = UNSET
    has_reschdule_permission: Union[Unset, InspectionTypeModelHasReschdulePermission] = UNSET
    has_schdule_permission: Union[Unset, InspectionTypeModelHasSchdulePermission] = UNSET
    id: Union[Unset, int] = UNSET
    inspection_editable: Union[Unset, InspectionTypeModelInspectionEditable] = UNSET
    is_auto_assign: Union[Unset, InspectionTypeModelIsAutoAssign] = UNSET
    is_required: Union[Unset, InspectionTypeModelIsRequired] = UNSET
    ivr_number: Union[Unset, int] = UNSET
    max_points: Union[Unset, float] = UNSET
    priority: Union[Unset, str] = UNSET
    public_visible: Union[Unset, InspectionTypeModelPublicVisible] = UNSET
    referece_number: Union[Unset, str] = UNSET
    reschedule_restriction: Union[Unset, "InspectionRestrictionModel"] = UNSET
    result_group: Union[Unset, str] = UNSET
    schdule_permission: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    total_score: Union[Unset, int] = UNSET
    total_score_option: Union[Unset, InspectionTypeModelTotalScoreOption] = UNSET
    unit_number: Union[Unset, str] = UNSET
    units: Union[Unset, float] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_fail_checklist_items: Union[Unset, str] = UNSET
        if not isinstance(self.allow_fail_checklist_items, Unset):
            allow_fail_checklist_items = self.allow_fail_checklist_items.value

        allow_multi_inspections: Union[Unset, str] = UNSET
        if not isinstance(self.allow_multi_inspections, Unset):
            allow_multi_inspections = self.allow_multi_inspections.value

        associations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.associations, Unset):
            associations = self.associations.to_dict()

        cancel_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cancel_restriction, Unset):
            cancel_restriction = self.cancel_restriction.to_dict()

        carryover_flag: Union[Unset, str] = UNSET
        if not isinstance(self.carryover_flag, Unset):
            carryover_flag = self.carryover_flag.value

        default_department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_department, Unset):
            default_department = self.default_department.to_dict()

        disciplines: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disciplines, Unset):
            disciplines = self.disciplines

        flow_enabled_flag: Union[Unset, str] = UNSET
        if not isinstance(self.flow_enabled_flag, Unset):
            flow_enabled_flag = self.flow_enabled_flag.value

        grade = self.grade
        group = self.group
        group_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_name, Unset):
            group_name = self.group_name.to_dict()

        guide_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guide_group, Unset):
            guide_group = self.guide_group.to_dict()

        has_cancel_permission: Union[Unset, str] = UNSET
        if not isinstance(self.has_cancel_permission, Unset):
            has_cancel_permission = self.has_cancel_permission.value

        has_flow_flag: Union[Unset, str] = UNSET
        if not isinstance(self.has_flow_flag, Unset):
            has_flow_flag = self.has_flow_flag.value

        has_next_inspection_advance: Union[Unset, str] = UNSET
        if not isinstance(self.has_next_inspection_advance, Unset):
            has_next_inspection_advance = self.has_next_inspection_advance.value

        has_reschdule_permission: Union[Unset, str] = UNSET
        if not isinstance(self.has_reschdule_permission, Unset):
            has_reschdule_permission = self.has_reschdule_permission.value

        has_schdule_permission: Union[Unset, str] = UNSET
        if not isinstance(self.has_schdule_permission, Unset):
            has_schdule_permission = self.has_schdule_permission.value

        id = self.id
        inspection_editable: Union[Unset, str] = UNSET
        if not isinstance(self.inspection_editable, Unset):
            inspection_editable = self.inspection_editable.value

        is_auto_assign: Union[Unset, str] = UNSET
        if not isinstance(self.is_auto_assign, Unset):
            is_auto_assign = self.is_auto_assign.value

        is_required: Union[Unset, str] = UNSET
        if not isinstance(self.is_required, Unset):
            is_required = self.is_required.value

        ivr_number = self.ivr_number
        max_points = self.max_points
        priority = self.priority
        public_visible: Union[Unset, str] = UNSET
        if not isinstance(self.public_visible, Unset):
            public_visible = self.public_visible.value

        referece_number = self.referece_number
        reschedule_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reschedule_restriction, Unset):
            reschedule_restriction = self.reschedule_restriction.to_dict()

        result_group = self.result_group
        schdule_permission = self.schdule_permission
        text = self.text
        total_score = self.total_score
        total_score_option: Union[Unset, str] = UNSET
        if not isinstance(self.total_score_option, Unset):
            total_score_option = self.total_score_option.value

        unit_number = self.unit_number
        units = self.units
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_fail_checklist_items is not UNSET:
            field_dict["allowFailChecklistItems"] = allow_fail_checklist_items
        if allow_multi_inspections is not UNSET:
            field_dict["allowMultiInspections"] = allow_multi_inspections
        if associations is not UNSET:
            field_dict["associations"] = associations
        if cancel_restriction is not UNSET:
            field_dict["cancelRestriction"] = cancel_restriction
        if carryover_flag is not UNSET:
            field_dict["carryoverFlag"] = carryover_flag
        if default_department is not UNSET:
            field_dict["defaultDepartment"] = default_department
        if disciplines is not UNSET:
            field_dict["disciplines"] = disciplines
        if flow_enabled_flag is not UNSET:
            field_dict["flowEnabledFlag"] = flow_enabled_flag
        if grade is not UNSET:
            field_dict["grade"] = grade
        if group is not UNSET:
            field_dict["group"] = group
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if guide_group is not UNSET:
            field_dict["guideGroup"] = guide_group
        if has_cancel_permission is not UNSET:
            field_dict["hasCancelPermission"] = has_cancel_permission
        if has_flow_flag is not UNSET:
            field_dict["hasFlowFlag"] = has_flow_flag
        if has_next_inspection_advance is not UNSET:
            field_dict["hasNextInspectionAdvance"] = has_next_inspection_advance
        if has_reschdule_permission is not UNSET:
            field_dict["hasReschdulePermission"] = has_reschdule_permission
        if has_schdule_permission is not UNSET:
            field_dict["hasSchdulePermission"] = has_schdule_permission
        if id is not UNSET:
            field_dict["id"] = id
        if inspection_editable is not UNSET:
            field_dict["inspectionEditable"] = inspection_editable
        if is_auto_assign is not UNSET:
            field_dict["isAutoAssign"] = is_auto_assign
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if ivr_number is not UNSET:
            field_dict["ivrNumber"] = ivr_number
        if max_points is not UNSET:
            field_dict["maxPoints"] = max_points
        if priority is not UNSET:
            field_dict["priority"] = priority
        if public_visible is not UNSET:
            field_dict["publicVisible"] = public_visible
        if referece_number is not UNSET:
            field_dict["refereceNumber"] = referece_number
        if reschedule_restriction is not UNSET:
            field_dict["rescheduleRestriction"] = reschedule_restriction
        if result_group is not UNSET:
            field_dict["resultGroup"] = result_group
        if schdule_permission is not UNSET:
            field_dict["schdulePermission"] = schdule_permission
        if text is not UNSET:
            field_dict["text"] = text
        if total_score is not UNSET:
            field_dict["totalScore"] = total_score
        if total_score_option is not UNSET:
            field_dict["totalScoreOption"] = total_score_option
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if units is not UNSET:
            field_dict["units"] = units
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.department_model import DepartmentModel
        from ..models.inspection_restriction_model import InspectionRestrictionModel
        from ..models.inspection_type_associations_model import InspectionTypeAssociationsModel
        from ..models.inspection_type_model_group_name import InspectionTypeModelGroupName
        from ..models.r_guide_sheet_group_model import RGuideSheetGroupModel

        d = src_dict.copy()
        _allow_fail_checklist_items = d.pop("allowFailChecklistItems", UNSET)
        allow_fail_checklist_items: Union[Unset, InspectionTypeModelAllowFailChecklistItems]
        if isinstance(_allow_fail_checklist_items, Unset):
            allow_fail_checklist_items = UNSET
        else:
            allow_fail_checklist_items = InspectionTypeModelAllowFailChecklistItems(_allow_fail_checklist_items)

        _allow_multi_inspections = d.pop("allowMultiInspections", UNSET)
        allow_multi_inspections: Union[Unset, InspectionTypeModelAllowMultiInspections]
        if isinstance(_allow_multi_inspections, Unset):
            allow_multi_inspections = UNSET
        else:
            allow_multi_inspections = InspectionTypeModelAllowMultiInspections(_allow_multi_inspections)

        _associations = d.pop("associations", UNSET)
        associations: Union[Unset, InspectionTypeAssociationsModel]
        if isinstance(_associations, Unset):
            associations = UNSET
        else:
            associations = InspectionTypeAssociationsModel.from_dict(_associations)

        _cancel_restriction = d.pop("cancelRestriction", UNSET)
        cancel_restriction: Union[Unset, InspectionRestrictionModel]
        if isinstance(_cancel_restriction, Unset):
            cancel_restriction = UNSET
        else:
            cancel_restriction = InspectionRestrictionModel.from_dict(_cancel_restriction)

        _carryover_flag = d.pop("carryoverFlag", UNSET)
        carryover_flag: Union[Unset, InspectionTypeModelCarryoverFlag]
        if isinstance(_carryover_flag, Unset):
            carryover_flag = UNSET
        else:
            carryover_flag = InspectionTypeModelCarryoverFlag(_carryover_flag)

        _default_department = d.pop("defaultDepartment", UNSET)
        default_department: Union[Unset, DepartmentModel]
        if isinstance(_default_department, Unset):
            default_department = UNSET
        else:
            default_department = DepartmentModel.from_dict(_default_department)

        disciplines = cast(List[str], d.pop("disciplines", UNSET))

        _flow_enabled_flag = d.pop("flowEnabledFlag", UNSET)
        flow_enabled_flag: Union[Unset, InspectionTypeModelFlowEnabledFlag]
        if isinstance(_flow_enabled_flag, Unset):
            flow_enabled_flag = UNSET
        else:
            flow_enabled_flag = InspectionTypeModelFlowEnabledFlag(_flow_enabled_flag)

        grade = d.pop("grade", UNSET)

        group = d.pop("group", UNSET)

        _group_name = d.pop("groupName", UNSET)
        group_name: Union[Unset, InspectionTypeModelGroupName]
        if isinstance(_group_name, Unset):
            group_name = UNSET
        else:
            group_name = InspectionTypeModelGroupName.from_dict(_group_name)

        _guide_group = d.pop("guideGroup", UNSET)
        guide_group: Union[Unset, RGuideSheetGroupModel]
        if isinstance(_guide_group, Unset):
            guide_group = UNSET
        else:
            guide_group = RGuideSheetGroupModel.from_dict(_guide_group)

        _has_cancel_permission = d.pop("hasCancelPermission", UNSET)
        has_cancel_permission: Union[Unset, InspectionTypeModelHasCancelPermission]
        if isinstance(_has_cancel_permission, Unset):
            has_cancel_permission = UNSET
        else:
            has_cancel_permission = InspectionTypeModelHasCancelPermission(_has_cancel_permission)

        _has_flow_flag = d.pop("hasFlowFlag", UNSET)
        has_flow_flag: Union[Unset, InspectionTypeModelHasFlowFlag]
        if isinstance(_has_flow_flag, Unset):
            has_flow_flag = UNSET
        else:
            has_flow_flag = InspectionTypeModelHasFlowFlag(_has_flow_flag)

        _has_next_inspection_advance = d.pop("hasNextInspectionAdvance", UNSET)
        has_next_inspection_advance: Union[Unset, InspectionTypeModelHasNextInspectionAdvance]
        if isinstance(_has_next_inspection_advance, Unset):
            has_next_inspection_advance = UNSET
        else:
            has_next_inspection_advance = InspectionTypeModelHasNextInspectionAdvance(_has_next_inspection_advance)

        _has_reschdule_permission = d.pop("hasReschdulePermission", UNSET)
        has_reschdule_permission: Union[Unset, InspectionTypeModelHasReschdulePermission]
        if isinstance(_has_reschdule_permission, Unset):
            has_reschdule_permission = UNSET
        else:
            has_reschdule_permission = InspectionTypeModelHasReschdulePermission(_has_reschdule_permission)

        _has_schdule_permission = d.pop("hasSchdulePermission", UNSET)
        has_schdule_permission: Union[Unset, InspectionTypeModelHasSchdulePermission]
        if isinstance(_has_schdule_permission, Unset):
            has_schdule_permission = UNSET
        else:
            has_schdule_permission = InspectionTypeModelHasSchdulePermission(_has_schdule_permission)

        id = d.pop("id", UNSET)

        _inspection_editable = d.pop("inspectionEditable", UNSET)
        inspection_editable: Union[Unset, InspectionTypeModelInspectionEditable]
        if isinstance(_inspection_editable, Unset):
            inspection_editable = UNSET
        else:
            inspection_editable = InspectionTypeModelInspectionEditable(_inspection_editable)

        _is_auto_assign = d.pop("isAutoAssign", UNSET)
        is_auto_assign: Union[Unset, InspectionTypeModelIsAutoAssign]
        if isinstance(_is_auto_assign, Unset):
            is_auto_assign = UNSET
        else:
            is_auto_assign = InspectionTypeModelIsAutoAssign(_is_auto_assign)

        _is_required = d.pop("isRequired", UNSET)
        is_required: Union[Unset, InspectionTypeModelIsRequired]
        if isinstance(_is_required, Unset):
            is_required = UNSET
        else:
            is_required = InspectionTypeModelIsRequired(_is_required)

        ivr_number = d.pop("ivrNumber", UNSET)

        max_points = d.pop("maxPoints", UNSET)

        priority = d.pop("priority", UNSET)

        _public_visible = d.pop("publicVisible", UNSET)
        public_visible: Union[Unset, InspectionTypeModelPublicVisible]
        if isinstance(_public_visible, Unset):
            public_visible = UNSET
        else:
            public_visible = InspectionTypeModelPublicVisible(_public_visible)

        referece_number = d.pop("refereceNumber", UNSET)

        _reschedule_restriction = d.pop("rescheduleRestriction", UNSET)
        reschedule_restriction: Union[Unset, InspectionRestrictionModel]
        if isinstance(_reschedule_restriction, Unset):
            reschedule_restriction = UNSET
        else:
            reschedule_restriction = InspectionRestrictionModel.from_dict(_reschedule_restriction)

        result_group = d.pop("resultGroup", UNSET)

        schdule_permission = d.pop("schdulePermission", UNSET)

        text = d.pop("text", UNSET)

        total_score = d.pop("totalScore", UNSET)

        _total_score_option = d.pop("totalScoreOption", UNSET)
        total_score_option: Union[Unset, InspectionTypeModelTotalScoreOption]
        if isinstance(_total_score_option, Unset):
            total_score_option = UNSET
        else:
            total_score_option = InspectionTypeModelTotalScoreOption(_total_score_option)

        unit_number = d.pop("unitNumber", UNSET)

        units = d.pop("units", UNSET)

        value = d.pop("value", UNSET)

        inspection_type_model = cls(
            allow_fail_checklist_items=allow_fail_checklist_items,
            allow_multi_inspections=allow_multi_inspections,
            associations=associations,
            cancel_restriction=cancel_restriction,
            carryover_flag=carryover_flag,
            default_department=default_department,
            disciplines=disciplines,
            flow_enabled_flag=flow_enabled_flag,
            grade=grade,
            group=group,
            group_name=group_name,
            guide_group=guide_group,
            has_cancel_permission=has_cancel_permission,
            has_flow_flag=has_flow_flag,
            has_next_inspection_advance=has_next_inspection_advance,
            has_reschdule_permission=has_reschdule_permission,
            has_schdule_permission=has_schdule_permission,
            id=id,
            inspection_editable=inspection_editable,
            is_auto_assign=is_auto_assign,
            is_required=is_required,
            ivr_number=ivr_number,
            max_points=max_points,
            priority=priority,
            public_visible=public_visible,
            referece_number=referece_number,
            reschedule_restriction=reschedule_restriction,
            result_group=result_group,
            schdule_permission=schdule_permission,
            text=text,
            total_score=total_score,
            total_score_option=total_score_option,
            unit_number=unit_number,
            units=units,
            value=value,
        )

        inspection_type_model.additional_properties = d
        return inspection_type_model

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
