import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_item_model_1_code import FeeItemModel1Code
    from ..models.fee_item_model_1_payment_period import FeeItemModel1PaymentPeriod
    from ..models.fee_item_model_1_schedule import FeeItemModel1Schedule
    from ..models.fee_item_model_1_sub_group import FeeItemModel1SubGroup
    from ..models.fee_item_model_1_unit import FeeItemModel1Unit
    from ..models.fee_item_model_1_version import FeeItemModel1Version
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="FeeItemModel1")


@_attrs_define
class FeeItemModel1:
    """
    Attributes:
        account_code_1 (Union[Unset, str]): The code associated with the first fee
        account_code_1_allocation (Union[Unset, float]): Allocation proportion or amount of account code 1.
        account_code_2 (Union[Unset, str]): The code associated with the second fee
        account_code_2_allocation (Union[Unset, float]): Allocation proportion or amount of account code 2.
        account_code_3 (Union[Unset, str]): The code associated with the third fee
        account_code_3_allocation (Union[Unset, float]): Allocation proportion or amount of account code 3.
        amount (Union[Unset, float]): The amount of a payment transaction or account balance.
        audit_date (Union[Unset, datetime.datetime]): The date when the fee item was added or updated.
        apply_date (Union[Unset, datetime.datetime]): The date the fee is applied.
        balance_due (Union[Unset, float]): The amount due.
        code (Union[Unset, FeeItemModel1Code]): A code identifying an associated item
        display_order (Union[Unset, int]): The display order of the fee item.
        id (Union[Unset, int]): The fee system id.
        invoice_id (Union[Unset, int]): The invoice ID for the fee item.
        max_fee (Union[Unset, float]): The maximum fee item.
        min_fee (Union[Unset, float]): The minimum fee item.
        notes (Union[Unset, str]): Notes about the fee item.
        payment_period (Union[Unset, FeeItemModel1PaymentPeriod]): The time interval for processing invoices.
        priority (Union[Unset, int]): The priority level assigned to the fee item.
        quantity (Union[Unset, float]): The number of units for which the same fee applies.
        record_id (Union[Unset, RecordIdModel]):
        schedule (Union[Unset, FeeItemModel1Schedule]): The payment schedule name.
        status (Union[Unset, str]): The fee item status.
        sub_group (Union[Unset, FeeItemModel1SubGroup]): The subgroup the fee is associated with.
        udf1 (Union[Unset, str]): User defined field 1
        udf2 (Union[Unset, str]): User defined field 2
        udf3 (Union[Unset, str]): User defined field 3
        unit (Union[Unset, FeeItemModel1Unit]): The unit of measure used for the object.
        variable (Union[Unset, str]): The variable associated with the fee item.
        version (Union[Unset, FeeItemModel1Version]): The payment schedule version
    """

    account_code_1: Union[Unset, str] = UNSET
    account_code_1_allocation: Union[Unset, float] = UNSET
    account_code_2: Union[Unset, str] = UNSET
    account_code_2_allocation: Union[Unset, float] = UNSET
    account_code_3: Union[Unset, str] = UNSET
    account_code_3_allocation: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    audit_date: Union[Unset, datetime.datetime] = UNSET
    apply_date: Union[Unset, datetime.datetime] = UNSET
    balance_due: Union[Unset, float] = UNSET
    code: Union[Unset, "FeeItemModel1Code"] = UNSET
    display_order: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    invoice_id: Union[Unset, int] = UNSET
    max_fee: Union[Unset, float] = UNSET
    min_fee: Union[Unset, float] = UNSET
    notes: Union[Unset, str] = UNSET
    payment_period: Union[Unset, "FeeItemModel1PaymentPeriod"] = UNSET
    priority: Union[Unset, int] = UNSET
    quantity: Union[Unset, float] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    schedule: Union[Unset, "FeeItemModel1Schedule"] = UNSET
    status: Union[Unset, str] = UNSET
    sub_group: Union[Unset, "FeeItemModel1SubGroup"] = UNSET
    udf1: Union[Unset, str] = UNSET
    udf2: Union[Unset, str] = UNSET
    udf3: Union[Unset, str] = UNSET
    unit: Union[Unset, "FeeItemModel1Unit"] = UNSET
    variable: Union[Unset, str] = UNSET
    version: Union[Unset, "FeeItemModel1Version"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_code_1 = self.account_code_1
        account_code_1_allocation = self.account_code_1_allocation
        account_code_2 = self.account_code_2
        account_code_2_allocation = self.account_code_2_allocation
        account_code_3 = self.account_code_3
        account_code_3_allocation = self.account_code_3_allocation
        amount = self.amount
        audit_date: Union[Unset, str] = UNSET
        if not isinstance(self.audit_date, Unset):
            audit_date = self.audit_date.isoformat()

        apply_date: Union[Unset, str] = UNSET
        if not isinstance(self.apply_date, Unset):
            apply_date = self.apply_date.isoformat()

        balance_due = self.balance_due
        code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        display_order = self.display_order
        id = self.id
        invoice_id = self.invoice_id
        max_fee = self.max_fee
        min_fee = self.min_fee
        notes = self.notes
        payment_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_period, Unset):
            payment_period = self.payment_period.to_dict()

        priority = self.priority
        quantity = self.quantity
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        status = self.status
        sub_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_group, Unset):
            sub_group = self.sub_group.to_dict()

        udf1 = self.udf1
        udf2 = self.udf2
        udf3 = self.udf3
        unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.to_dict()

        variable = self.variable
        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_code_1 is not UNSET:
            field_dict["accountCode1"] = account_code_1
        if account_code_1_allocation is not UNSET:
            field_dict["accountCode1Allocation"] = account_code_1_allocation
        if account_code_2 is not UNSET:
            field_dict["accountCode2"] = account_code_2
        if account_code_2_allocation is not UNSET:
            field_dict["accountCode2Allocation"] = account_code_2_allocation
        if account_code_3 is not UNSET:
            field_dict["accountCode3"] = account_code_3
        if account_code_3_allocation is not UNSET:
            field_dict["accountCode3Allocation"] = account_code_3_allocation
        if amount is not UNSET:
            field_dict["amount"] = amount
        if audit_date is not UNSET:
            field_dict["auditDate"] = audit_date
        if apply_date is not UNSET:
            field_dict["applyDate"] = apply_date
        if balance_due is not UNSET:
            field_dict["balanceDue"] = balance_due
        if code is not UNSET:
            field_dict["code"] = code
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if max_fee is not UNSET:
            field_dict["maxFee"] = max_fee
        if min_fee is not UNSET:
            field_dict["minFee"] = min_fee
        if notes is not UNSET:
            field_dict["notes"] = notes
        if payment_period is not UNSET:
            field_dict["paymentPeriod"] = payment_period
        if priority is not UNSET:
            field_dict["priority"] = priority
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if status is not UNSET:
            field_dict["status"] = status
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if udf1 is not UNSET:
            field_dict["udf1"] = udf1
        if udf2 is not UNSET:
            field_dict["udf2"] = udf2
        if udf3 is not UNSET:
            field_dict["udf3"] = udf3
        if unit is not UNSET:
            field_dict["unit"] = unit
        if variable is not UNSET:
            field_dict["variable"] = variable
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_item_model_1_code import FeeItemModel1Code
        from ..models.fee_item_model_1_payment_period import FeeItemModel1PaymentPeriod
        from ..models.fee_item_model_1_schedule import FeeItemModel1Schedule
        from ..models.fee_item_model_1_sub_group import FeeItemModel1SubGroup
        from ..models.fee_item_model_1_unit import FeeItemModel1Unit
        from ..models.fee_item_model_1_version import FeeItemModel1Version
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        account_code_1 = d.pop("accountCode1", UNSET)

        account_code_1_allocation = d.pop("accountCode1Allocation", UNSET)

        account_code_2 = d.pop("accountCode2", UNSET)

        account_code_2_allocation = d.pop("accountCode2Allocation", UNSET)

        account_code_3 = d.pop("accountCode3", UNSET)

        account_code_3_allocation = d.pop("accountCode3Allocation", UNSET)

        amount = d.pop("amount", UNSET)

        _audit_date = d.pop("auditDate", UNSET)
        audit_date: Union[Unset, datetime.datetime]
        if isinstance(_audit_date, Unset):
            audit_date = UNSET
        else:
            audit_date = isoparse(_audit_date)

        _apply_date = d.pop("applyDate", UNSET)
        apply_date: Union[Unset, datetime.datetime]
        if isinstance(_apply_date, Unset):
            apply_date = UNSET
        else:
            apply_date = isoparse(_apply_date)

        balance_due = d.pop("balanceDue", UNSET)

        _code = d.pop("code", UNSET)
        code: Union[Unset, FeeItemModel1Code]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = FeeItemModel1Code.from_dict(_code)

        display_order = d.pop("displayOrder", UNSET)

        id = d.pop("id", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        max_fee = d.pop("maxFee", UNSET)

        min_fee = d.pop("minFee", UNSET)

        notes = d.pop("notes", UNSET)

        _payment_period = d.pop("paymentPeriod", UNSET)
        payment_period: Union[Unset, FeeItemModel1PaymentPeriod]
        if isinstance(_payment_period, Unset):
            payment_period = UNSET
        else:
            payment_period = FeeItemModel1PaymentPeriod.from_dict(_payment_period)

        priority = d.pop("priority", UNSET)

        quantity = d.pop("quantity", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, FeeItemModel1Schedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FeeItemModel1Schedule.from_dict(_schedule)

        status = d.pop("status", UNSET)

        _sub_group = d.pop("subGroup", UNSET)
        sub_group: Union[Unset, FeeItemModel1SubGroup]
        if isinstance(_sub_group, Unset):
            sub_group = UNSET
        else:
            sub_group = FeeItemModel1SubGroup.from_dict(_sub_group)

        udf1 = d.pop("udf1", UNSET)

        udf2 = d.pop("udf2", UNSET)

        udf3 = d.pop("udf3", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, FeeItemModel1Unit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = FeeItemModel1Unit.from_dict(_unit)

        variable = d.pop("variable", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FeeItemModel1Version]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = FeeItemModel1Version.from_dict(_version)

        fee_item_model_1 = cls(
            account_code_1=account_code_1,
            account_code_1_allocation=account_code_1_allocation,
            account_code_2=account_code_2,
            account_code_2_allocation=account_code_2_allocation,
            account_code_3=account_code_3,
            account_code_3_allocation=account_code_3_allocation,
            amount=amount,
            audit_date=audit_date,
            apply_date=apply_date,
            balance_due=balance_due,
            code=code,
            display_order=display_order,
            id=id,
            invoice_id=invoice_id,
            max_fee=max_fee,
            min_fee=min_fee,
            notes=notes,
            payment_period=payment_period,
            priority=priority,
            quantity=quantity,
            record_id=record_id,
            schedule=schedule,
            status=status,
            sub_group=sub_group,
            udf1=udf1,
            udf2=udf2,
            udf3=udf3,
            unit=unit,
            variable=variable,
            version=version,
        )

        fee_item_model_1.additional_properties = d
        return fee_item_model_1

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
