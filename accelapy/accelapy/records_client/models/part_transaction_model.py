import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.part_transaction_model_hard_reservation import PartTransactionModelHardReservation
from ..models.part_transaction_model_taxable import PartTransactionModelTaxable
from ..models.part_transaction_model_transaction_type import PartTransactionModelTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.part_transaction_model_status import PartTransactionModelStatus
    from ..models.part_transaction_model_type import PartTransactionModelType
    from ..models.part_transaction_model_unit_measurement import PartTransactionModelUnitMeasurement
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="PartTransactionModel")


@_attrs_define
class PartTransactionModel:
    """
    Attributes:
        account_name (Union[Unset, str]): The budget account name associated with the part transaction.
        account_number (Union[Unset, str]): The budget account number associated with the part transaction.
        comments (Union[Unset, str]): Comments or notes about the current context.
        cost_total (Union[Unset, float]): The total cost of the part transaction.
        hard_reservation (Union[Unset, PartTransactionModelHardReservation]): Indicates whether or not the part
            transaction is a hard reservation. "Y": A hard reservation which guarantees the reservation, and subtract the
            order from the quantity on hand. "N" : A soft reservation which alerts the warehouse that houses the part that
            someone may request the part. The quantity on hand of the part does not change.
        id (Union[Unset, int]): The part transaction system id assigned by the Civic Platform server.
        location_id (Union[Unset, int]): The location ID associated with the part transaction.
        part_bin (Union[Unset, str]): The name of the part bin.
        part_brand (Union[Unset, str]): The name of the part brand.
        part_description (Union[Unset, str]): The description of the part.
        part_id (Union[Unset, int]): The part ID.
        part_location (Union[Unset, str]): The location of the part.
        part_number (Union[Unset, str]): The number of the part.
        quantity (Union[Unset, float]): The number of units for which the same fee applies.
        record_id (Union[Unset, RecordIdModel]):
        res_to_part_location (Union[Unset, str]):
        reservation_number (Union[Unset, int]): The part reservation number.
        reservation_status (Union[Unset, str]): The status of the part reservation.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        status (Union[Unset, PartTransactionModelStatus]): The part transaction status.
        taxable (Union[Unset, PartTransactionModelTaxable]): Indicates whether or not the part is taxable.
        transaction_cost (Union[Unset, float]): The part transaction cost.
        transaction_date (Union[Unset, datetime.datetime]): The part transaction date.
        transaction_type (Union[Unset, PartTransactionModelTransactionType]): The part transaction type. Possible
            values:

            "Issue" : occurs either when someone requests and receives a part on the spot, or when someone receives a
            reserved part.

            "Receive" : occurs when someone purchases a part or returns a part to a location.

            "Transfer" : occurs when someone moves a part from one location to another.

            "Adjust" : occurs when someone makes quantity adjustments for cycle counts.

            "Reserve" : occurs when someone sets aside parts so they can issue them at a later date.
        type (Union[Unset, PartTransactionModelType]):
        unit_cost (Union[Unset, float]): The unit cost per part.
        unit_measurement (Union[Unset, PartTransactionModelUnitMeasurement]): The unit of measurement for quantifying
            the part.
        updated_by (Union[Unset, str]): The user who last updated the checklist or checklist item.
        work_order_task_code (Union[Unset, str]): The work order task code associated with the part transactionmodel.
        work_order_task_code_index (Union[Unset, int]): The work order task code index associated with the part
            transactionmodel.
    """

    account_name: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    cost_total: Union[Unset, float] = UNSET
    hard_reservation: Union[Unset, PartTransactionModelHardReservation] = UNSET
    id: Union[Unset, int] = UNSET
    location_id: Union[Unset, int] = UNSET
    part_bin: Union[Unset, str] = UNSET
    part_brand: Union[Unset, str] = UNSET
    part_description: Union[Unset, str] = UNSET
    part_id: Union[Unset, int] = UNSET
    part_location: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    res_to_part_location: Union[Unset, str] = UNSET
    reservation_number: Union[Unset, int] = UNSET
    reservation_status: Union[Unset, str] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    status: Union[Unset, "PartTransactionModelStatus"] = UNSET
    taxable: Union[Unset, PartTransactionModelTaxable] = UNSET
    transaction_cost: Union[Unset, float] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    transaction_type: Union[Unset, PartTransactionModelTransactionType] = UNSET
    type: Union[Unset, "PartTransactionModelType"] = UNSET
    unit_cost: Union[Unset, float] = UNSET
    unit_measurement: Union[Unset, "PartTransactionModelUnitMeasurement"] = UNSET
    updated_by: Union[Unset, str] = UNSET
    work_order_task_code: Union[Unset, str] = UNSET
    work_order_task_code_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_name = self.account_name
        account_number = self.account_number
        comments = self.comments
        cost_total = self.cost_total
        hard_reservation: Union[Unset, str] = UNSET
        if not isinstance(self.hard_reservation, Unset):
            hard_reservation = self.hard_reservation.value

        id = self.id
        location_id = self.location_id
        part_bin = self.part_bin
        part_brand = self.part_brand
        part_description = self.part_description
        part_id = self.part_id
        part_location = self.part_location
        part_number = self.part_number
        quantity = self.quantity
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        res_to_part_location = self.res_to_part_location
        reservation_number = self.reservation_number
        reservation_status = self.reservation_status
        service_provider_code = self.service_provider_code
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        taxable: Union[Unset, str] = UNSET
        if not isinstance(self.taxable, Unset):
            taxable = self.taxable.value

        transaction_cost = self.transaction_cost
        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        unit_cost = self.unit_cost
        unit_measurement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit_measurement, Unset):
            unit_measurement = self.unit_measurement.to_dict()

        updated_by = self.updated_by
        work_order_task_code = self.work_order_task_code
        work_order_task_code_index = self.work_order_task_code_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if comments is not UNSET:
            field_dict["comments"] = comments
        if cost_total is not UNSET:
            field_dict["costTotal"] = cost_total
        if hard_reservation is not UNSET:
            field_dict["hardReservation"] = hard_reservation
        if id is not UNSET:
            field_dict["id"] = id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if part_bin is not UNSET:
            field_dict["partBin"] = part_bin
        if part_brand is not UNSET:
            field_dict["partBrand"] = part_brand
        if part_description is not UNSET:
            field_dict["partDescription"] = part_description
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_location is not UNSET:
            field_dict["partLocation"] = part_location
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if res_to_part_location is not UNSET:
            field_dict["resToPartLocation"] = res_to_part_location
        if reservation_number is not UNSET:
            field_dict["reservationNumber"] = reservation_number
        if reservation_status is not UNSET:
            field_dict["reservationStatus"] = reservation_status
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if status is not UNSET:
            field_dict["status"] = status
        if taxable is not UNSET:
            field_dict["taxable"] = taxable
        if transaction_cost is not UNSET:
            field_dict["transactionCost"] = transaction_cost
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if type is not UNSET:
            field_dict["type"] = type
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if unit_measurement is not UNSET:
            field_dict["unitMeasurement"] = unit_measurement
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if work_order_task_code is not UNSET:
            field_dict["workOrderTaskCode"] = work_order_task_code
        if work_order_task_code_index is not UNSET:
            field_dict["workOrderTaskCodeIndex"] = work_order_task_code_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.part_transaction_model_status import PartTransactionModelStatus
        from ..models.part_transaction_model_type import PartTransactionModelType
        from ..models.part_transaction_model_unit_measurement import PartTransactionModelUnitMeasurement
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        account_name = d.pop("accountName", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        comments = d.pop("comments", UNSET)

        cost_total = d.pop("costTotal", UNSET)

        _hard_reservation = d.pop("hardReservation", UNSET)
        hard_reservation: Union[Unset, PartTransactionModelHardReservation]
        if isinstance(_hard_reservation, Unset):
            hard_reservation = UNSET
        else:
            hard_reservation = PartTransactionModelHardReservation(_hard_reservation)

        id = d.pop("id", UNSET)

        location_id = d.pop("locationId", UNSET)

        part_bin = d.pop("partBin", UNSET)

        part_brand = d.pop("partBrand", UNSET)

        part_description = d.pop("partDescription", UNSET)

        part_id = d.pop("partId", UNSET)

        part_location = d.pop("partLocation", UNSET)

        part_number = d.pop("partNumber", UNSET)

        quantity = d.pop("quantity", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        res_to_part_location = d.pop("resToPartLocation", UNSET)

        reservation_number = d.pop("reservationNumber", UNSET)

        reservation_status = d.pop("reservationStatus", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PartTransactionModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PartTransactionModelStatus.from_dict(_status)

        _taxable = d.pop("taxable", UNSET)
        taxable: Union[Unset, PartTransactionModelTaxable]
        if isinstance(_taxable, Unset):
            taxable = UNSET
        else:
            taxable = PartTransactionModelTaxable(_taxable)

        transaction_cost = d.pop("transactionCost", UNSET)

        _transaction_date = d.pop("transactionDate", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        _transaction_type = d.pop("transactionType", UNSET)
        transaction_type: Union[Unset, PartTransactionModelTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = PartTransactionModelTransactionType(_transaction_type)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PartTransactionModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PartTransactionModelType.from_dict(_type)

        unit_cost = d.pop("unitCost", UNSET)

        _unit_measurement = d.pop("unitMeasurement", UNSET)
        unit_measurement: Union[Unset, PartTransactionModelUnitMeasurement]
        if isinstance(_unit_measurement, Unset):
            unit_measurement = UNSET
        else:
            unit_measurement = PartTransactionModelUnitMeasurement.from_dict(_unit_measurement)

        updated_by = d.pop("updatedBy", UNSET)

        work_order_task_code = d.pop("workOrderTaskCode", UNSET)

        work_order_task_code_index = d.pop("workOrderTaskCodeIndex", UNSET)

        part_transaction_model = cls(
            account_name=account_name,
            account_number=account_number,
            comments=comments,
            cost_total=cost_total,
            hard_reservation=hard_reservation,
            id=id,
            location_id=location_id,
            part_bin=part_bin,
            part_brand=part_brand,
            part_description=part_description,
            part_id=part_id,
            part_location=part_location,
            part_number=part_number,
            quantity=quantity,
            record_id=record_id,
            res_to_part_location=res_to_part_location,
            reservation_number=reservation_number,
            reservation_status=reservation_status,
            service_provider_code=service_provider_code,
            status=status,
            taxable=taxable,
            transaction_cost=transaction_cost,
            transaction_date=transaction_date,
            transaction_type=transaction_type,
            type=type,
            unit_cost=unit_cost,
            unit_measurement=unit_measurement,
            updated_by=updated_by,
            work_order_task_code=work_order_task_code,
            work_order_task_code_index=work_order_task_code_index,
        )

        part_transaction_model.additional_properties = d
        return part_transaction_model

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
