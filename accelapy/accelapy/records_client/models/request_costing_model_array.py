import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.request_costing_model_array_distribute_flag import RequestCostingModelArrayDistributeFlag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.costing_quantity_model import CostingQuantityModel
    from ..models.request_costing_model_array_cost_factor import RequestCostingModelArrayCostFactor
    from ..models.request_costing_model_array_status import RequestCostingModelArrayStatus
    from ..models.request_costing_model_array_type import RequestCostingModelArrayType
    from ..models.request_costing_model_array_unit_of_measure import RequestCostingModelArrayUnitOfMeasure


T = TypeVar("T", bound="RequestCostingModelArray")


@_attrs_define
class RequestCostingModelArray:
    """
    Attributes:
        comments (Union[Unset, str]): Comments about the cost.
        cost_account (Union[Unset, str]): The cost account name.
        cost_date (Union[Unset, datetime.datetime]): The date when the cost applied.
        cost_factor (Union[Unset, RequestCostingModelArrayCostFactor]): The cost factor.
        cost_item (Union[Unset, str]): The cost item name.
        disp_costing_cost_item (Union[Unset, str]): The cost item display name.
        distribute_flag (Union[Unset, RequestCostingModelArrayDistributeFlag]): Indicates whether or not costing is
            distributed.
        end_time (Union[Unset, str]): The end time associated to the cost item.
        fixed_rate (Union[Unset, float]): The fixed rate associated to the cost item.
        id (Union[Unset, int]): The cost item system id assigned by the Civic Platform server.
        quantity (Union[Unset, float]): The cost item quantity.
        quantity_detail (Union[Unset, str]): Details about the cost item quantity.
        quantity_detail_list (Union[Unset, CostingQuantityModel]):
        related_asgn_nbr (Union[Unset, int]): Related cost item.
        start_time (Union[Unset, str]): The start time associated to the cost item.
        status (Union[Unset, RequestCostingModelArrayStatus]): The cost item status.
        total_cost (Union[Unset, float]): The total cost.
        type (Union[Unset, RequestCostingModelArrayType]): The cost item type.
        unit_of_measure (Union[Unset, RequestCostingModelArrayUnitOfMeasure]): The cost item's unit of measure.
        unit_rate (Union[Unset, float]): The cost unit rate.
        work_order_task_code (Union[Unset, str]): The work order task code associated to the cost item.
        work_order_task_code_index (Union[Unset, int]): The order of the work order task.
    """

    comments: Union[Unset, str] = UNSET
    cost_account: Union[Unset, str] = UNSET
    cost_date: Union[Unset, datetime.datetime] = UNSET
    cost_factor: Union[Unset, "RequestCostingModelArrayCostFactor"] = UNSET
    cost_item: Union[Unset, str] = UNSET
    disp_costing_cost_item: Union[Unset, str] = UNSET
    distribute_flag: Union[Unset, RequestCostingModelArrayDistributeFlag] = UNSET
    end_time: Union[Unset, str] = UNSET
    fixed_rate: Union[Unset, float] = UNSET
    id: Union[Unset, int] = UNSET
    quantity: Union[Unset, float] = UNSET
    quantity_detail: Union[Unset, str] = UNSET
    quantity_detail_list: Union[Unset, "CostingQuantityModel"] = UNSET
    related_asgn_nbr: Union[Unset, int] = UNSET
    start_time: Union[Unset, str] = UNSET
    status: Union[Unset, "RequestCostingModelArrayStatus"] = UNSET
    total_cost: Union[Unset, float] = UNSET
    type: Union[Unset, "RequestCostingModelArrayType"] = UNSET
    unit_of_measure: Union[Unset, "RequestCostingModelArrayUnitOfMeasure"] = UNSET
    unit_rate: Union[Unset, float] = UNSET
    work_order_task_code: Union[Unset, str] = UNSET
    work_order_task_code_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comments = self.comments
        cost_account = self.cost_account
        cost_date: Union[Unset, str] = UNSET
        if not isinstance(self.cost_date, Unset):
            cost_date = self.cost_date.isoformat()

        cost_factor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_factor, Unset):
            cost_factor = self.cost_factor.to_dict()

        cost_item = self.cost_item
        disp_costing_cost_item = self.disp_costing_cost_item
        distribute_flag: Union[Unset, str] = UNSET
        if not isinstance(self.distribute_flag, Unset):
            distribute_flag = self.distribute_flag.value

        end_time = self.end_time
        fixed_rate = self.fixed_rate
        id = self.id
        quantity = self.quantity
        quantity_detail = self.quantity_detail
        quantity_detail_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quantity_detail_list, Unset):
            quantity_detail_list = self.quantity_detail_list.to_dict()

        related_asgn_nbr = self.related_asgn_nbr
        start_time = self.start_time
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        total_cost = self.total_cost
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        unit_of_measure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit_of_measure, Unset):
            unit_of_measure = self.unit_of_measure.to_dict()

        unit_rate = self.unit_rate
        work_order_task_code = self.work_order_task_code
        work_order_task_code_index = self.work_order_task_code_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if cost_account is not UNSET:
            field_dict["costAccount"] = cost_account
        if cost_date is not UNSET:
            field_dict["costDate"] = cost_date
        if cost_factor is not UNSET:
            field_dict["costFactor"] = cost_factor
        if cost_item is not UNSET:
            field_dict["costItem"] = cost_item
        if disp_costing_cost_item is not UNSET:
            field_dict["dispCostingCostItem"] = disp_costing_cost_item
        if distribute_flag is not UNSET:
            field_dict["distributeFlag"] = distribute_flag
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if fixed_rate is not UNSET:
            field_dict["fixedRate"] = fixed_rate
        if id is not UNSET:
            field_dict["id"] = id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_detail is not UNSET:
            field_dict["quantityDetail"] = quantity_detail
        if quantity_detail_list is not UNSET:
            field_dict["quantityDetailList"] = quantity_detail_list
        if related_asgn_nbr is not UNSET:
            field_dict["relatedAsgnNbr"] = related_asgn_nbr
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if type is not UNSET:
            field_dict["type"] = type
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if unit_rate is not UNSET:
            field_dict["unitRate"] = unit_rate
        if work_order_task_code is not UNSET:
            field_dict["workOrderTaskCode"] = work_order_task_code
        if work_order_task_code_index is not UNSET:
            field_dict["workOrderTaskCodeIndex"] = work_order_task_code_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.costing_quantity_model import CostingQuantityModel
        from ..models.request_costing_model_array_cost_factor import RequestCostingModelArrayCostFactor
        from ..models.request_costing_model_array_status import RequestCostingModelArrayStatus
        from ..models.request_costing_model_array_type import RequestCostingModelArrayType
        from ..models.request_costing_model_array_unit_of_measure import RequestCostingModelArrayUnitOfMeasure

        d = src_dict.copy()
        comments = d.pop("comments", UNSET)

        cost_account = d.pop("costAccount", UNSET)

        _cost_date = d.pop("costDate", UNSET)
        cost_date: Union[Unset, datetime.datetime]
        if isinstance(_cost_date, Unset):
            cost_date = UNSET
        else:
            cost_date = isoparse(_cost_date)

        _cost_factor = d.pop("costFactor", UNSET)
        cost_factor: Union[Unset, RequestCostingModelArrayCostFactor]
        if isinstance(_cost_factor, Unset):
            cost_factor = UNSET
        else:
            cost_factor = RequestCostingModelArrayCostFactor.from_dict(_cost_factor)

        cost_item = d.pop("costItem", UNSET)

        disp_costing_cost_item = d.pop("dispCostingCostItem", UNSET)

        _distribute_flag = d.pop("distributeFlag", UNSET)
        distribute_flag: Union[Unset, RequestCostingModelArrayDistributeFlag]
        if isinstance(_distribute_flag, Unset):
            distribute_flag = UNSET
        else:
            distribute_flag = RequestCostingModelArrayDistributeFlag(_distribute_flag)

        end_time = d.pop("endTime", UNSET)

        fixed_rate = d.pop("fixedRate", UNSET)

        id = d.pop("id", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_detail = d.pop("quantityDetail", UNSET)

        _quantity_detail_list = d.pop("quantityDetailList", UNSET)
        quantity_detail_list: Union[Unset, CostingQuantityModel]
        if isinstance(_quantity_detail_list, Unset):
            quantity_detail_list = UNSET
        else:
            quantity_detail_list = CostingQuantityModel.from_dict(_quantity_detail_list)

        related_asgn_nbr = d.pop("relatedAsgnNbr", UNSET)

        start_time = d.pop("startTime", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RequestCostingModelArrayStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestCostingModelArrayStatus.from_dict(_status)

        total_cost = d.pop("totalCost", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RequestCostingModelArrayType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RequestCostingModelArrayType.from_dict(_type)

        _unit_of_measure = d.pop("unitOfMeasure", UNSET)
        unit_of_measure: Union[Unset, RequestCostingModelArrayUnitOfMeasure]
        if isinstance(_unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = RequestCostingModelArrayUnitOfMeasure.from_dict(_unit_of_measure)

        unit_rate = d.pop("unitRate", UNSET)

        work_order_task_code = d.pop("workOrderTaskCode", UNSET)

        work_order_task_code_index = d.pop("workOrderTaskCodeIndex", UNSET)

        request_costing_model_array = cls(
            comments=comments,
            cost_account=cost_account,
            cost_date=cost_date,
            cost_factor=cost_factor,
            cost_item=cost_item,
            disp_costing_cost_item=disp_costing_cost_item,
            distribute_flag=distribute_flag,
            end_time=end_time,
            fixed_rate=fixed_rate,
            id=id,
            quantity=quantity,
            quantity_detail=quantity_detail,
            quantity_detail_list=quantity_detail_list,
            related_asgn_nbr=related_asgn_nbr,
            start_time=start_time,
            status=status,
            total_cost=total_cost,
            type=type,
            unit_of_measure=unit_of_measure,
            unit_rate=unit_rate,
            work_order_task_code=work_order_task_code,
            work_order_task_code_index=work_order_task_code_index,
        )

        request_costing_model_array.additional_properties = d
        return request_costing_model_array

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
