import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_item_model_code import FeeItemModelCode
    from ..models.fee_item_model_description import FeeItemModelDescription
    from ..models.fee_item_model_payment_period import FeeItemModelPaymentPeriod
    from ..models.fee_item_model_schedule import FeeItemModelSchedule
    from ..models.fee_item_model_sub_group import FeeItemModelSubGroup
    from ..models.fee_item_model_unit import FeeItemModelUnit
    from ..models.fee_item_model_version import FeeItemModelVersion
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="FeeItemModel")


@_attrs_define
class FeeItemModel:
    """
    Attributes:
        aca_required_flag (Union[Unset, str]): Indicates whether or not the fee schedule is required in order to make it
            accessible to citizens.
        account_code_1 (Union[Unset, str]): The code associated with the first fee
        account_code_1_allocation (Union[Unset, float]): Allocation proportion or amount of account code 1.
        account_code_2 (Union[Unset, str]): The code associated with the second fee
        account_code_2_allocation (Union[Unset, float]): Allocation proportion or amount of account code 2.
        account_code_3 (Union[Unset, str]): The code associated with the third fee
        account_code_3_allocation (Union[Unset, float]): Allocation proportion or amount of account code 3.
        allocated_fee_1 (Union[Unset, float]): The allocated fee for account code 1.
        allocated_fee_2 (Union[Unset, float]): The allocated fee for account code 2.
        allocated_fee_3 (Union[Unset, float]): The allocated fee for account code 3.
        amount (Union[Unset, float]): The amount of a payment transaction or account balance.
        apply_date (Union[Unset, datetime.datetime]): The date the fee is applied.
        auto_assess_flag (Union[Unset, str]): Indicates whether or not the fee item is automatically assessed.
        auto_invoice_flag (Union[Unset, str]): Indicates whether or not the fee item is automatically invoiced.
        balance_due (Union[Unset, float]): The amount due.
        calc_flag (Union[Unset, str]): Indicates whether or not the fee amount is based on fee calculation.
        calculated_flag (Union[Unset, str]): Indicates whether or not the fee amount is based on fee calculation.
        code (Union[Unset, FeeItemModelCode]): A code identifying an associated item
        description (Union[Unset, FeeItemModelDescription]): The fee description.
        display_order (Union[Unset, int]): The display order of the fee item.
        effect_date (Union[Unset, datetime.datetime]): Fee item effective date.
        expire_date (Union[Unset, datetime.datetime]): The date when the item expires
        fee_allocation_type (Union[Unset, str]): The fee allocation type to each account code.
        fee_notes (Union[Unset, str]): Notes about the fee.
        id (Union[Unset, int]): The fee system id.
        invoice_id (Union[Unset, int]): The invoice ID for the fee item.
        max_fee (Union[Unset, float]): The maximum fee item.
        min_fee (Union[Unset, float]): The minimum fee item.
        payment_period (Union[Unset, FeeItemModelPaymentPeriod]): The time interval for processing invoices.
        priority (Union[Unset, int]): The priority level assigned to the fee item.
        quantity (Union[Unset, float]): The number of units for which the same fee applies.
        record_id (Union[Unset, RecordIdModel]):
        schedule (Union[Unset, FeeItemModelSchedule]): The payment schedule name.
        status (Union[Unset, str]): The fee item status.
        sub_group (Union[Unset, FeeItemModelSubGroup]): The subgroup the fee is associated with.
        udf1 (Union[Unset, str]): User defined field 1
        udf2 (Union[Unset, str]): User defined field 2
        udf3 (Union[Unset, str]): User defined field 3
        unit (Union[Unset, FeeItemModelUnit]): The unit of measure used for the object.
        variable (Union[Unset, str]): The variable associated with the fee item.
        version (Union[Unset, FeeItemModelVersion]): The payment schedule version
    """

    aca_required_flag: Union[Unset, str] = UNSET
    account_code_1: Union[Unset, str] = UNSET
    account_code_1_allocation: Union[Unset, float] = UNSET
    account_code_2: Union[Unset, str] = UNSET
    account_code_2_allocation: Union[Unset, float] = UNSET
    account_code_3: Union[Unset, str] = UNSET
    account_code_3_allocation: Union[Unset, float] = UNSET
    allocated_fee_1: Union[Unset, float] = UNSET
    allocated_fee_2: Union[Unset, float] = UNSET
    allocated_fee_3: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    apply_date: Union[Unset, datetime.datetime] = UNSET
    auto_assess_flag: Union[Unset, str] = UNSET
    auto_invoice_flag: Union[Unset, str] = UNSET
    balance_due: Union[Unset, float] = UNSET
    calc_flag: Union[Unset, str] = UNSET
    calculated_flag: Union[Unset, str] = UNSET
    code: Union[Unset, "FeeItemModelCode"] = UNSET
    description: Union[Unset, "FeeItemModelDescription"] = UNSET
    display_order: Union[Unset, int] = UNSET
    effect_date: Union[Unset, datetime.datetime] = UNSET
    expire_date: Union[Unset, datetime.datetime] = UNSET
    fee_allocation_type: Union[Unset, str] = UNSET
    fee_notes: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    invoice_id: Union[Unset, int] = UNSET
    max_fee: Union[Unset, float] = UNSET
    min_fee: Union[Unset, float] = UNSET
    payment_period: Union[Unset, "FeeItemModelPaymentPeriod"] = UNSET
    priority: Union[Unset, int] = UNSET
    quantity: Union[Unset, float] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    schedule: Union[Unset, "FeeItemModelSchedule"] = UNSET
    status: Union[Unset, str] = UNSET
    sub_group: Union[Unset, "FeeItemModelSubGroup"] = UNSET
    udf1: Union[Unset, str] = UNSET
    udf2: Union[Unset, str] = UNSET
    udf3: Union[Unset, str] = UNSET
    unit: Union[Unset, "FeeItemModelUnit"] = UNSET
    variable: Union[Unset, str] = UNSET
    version: Union[Unset, "FeeItemModelVersion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aca_required_flag = self.aca_required_flag
        account_code_1 = self.account_code_1
        account_code_1_allocation = self.account_code_1_allocation
        account_code_2 = self.account_code_2
        account_code_2_allocation = self.account_code_2_allocation
        account_code_3 = self.account_code_3
        account_code_3_allocation = self.account_code_3_allocation
        allocated_fee_1 = self.allocated_fee_1
        allocated_fee_2 = self.allocated_fee_2
        allocated_fee_3 = self.allocated_fee_3
        amount = self.amount
        apply_date: Union[Unset, str] = UNSET
        if not isinstance(self.apply_date, Unset):
            apply_date = self.apply_date.isoformat()

        auto_assess_flag = self.auto_assess_flag
        auto_invoice_flag = self.auto_invoice_flag
        balance_due = self.balance_due
        calc_flag = self.calc_flag
        calculated_flag = self.calculated_flag
        code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        display_order = self.display_order
        effect_date: Union[Unset, str] = UNSET
        if not isinstance(self.effect_date, Unset):
            effect_date = self.effect_date.isoformat()

        expire_date: Union[Unset, str] = UNSET
        if not isinstance(self.expire_date, Unset):
            expire_date = self.expire_date.isoformat()

        fee_allocation_type = self.fee_allocation_type
        fee_notes = self.fee_notes
        id = self.id
        invoice_id = self.invoice_id
        max_fee = self.max_fee
        min_fee = self.min_fee
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
        if aca_required_flag is not UNSET:
            field_dict["acaRequiredFlag"] = aca_required_flag
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
        if allocated_fee_1 is not UNSET:
            field_dict["allocatedFee1"] = allocated_fee_1
        if allocated_fee_2 is not UNSET:
            field_dict["allocatedFee2"] = allocated_fee_2
        if allocated_fee_3 is not UNSET:
            field_dict["allocatedFee3"] = allocated_fee_3
        if amount is not UNSET:
            field_dict["amount"] = amount
        if apply_date is not UNSET:
            field_dict["applyDate"] = apply_date
        if auto_assess_flag is not UNSET:
            field_dict["autoAssessFlag"] = auto_assess_flag
        if auto_invoice_flag is not UNSET:
            field_dict["autoInvoiceFlag"] = auto_invoice_flag
        if balance_due is not UNSET:
            field_dict["balanceDue"] = balance_due
        if calc_flag is not UNSET:
            field_dict["calcFlag"] = calc_flag
        if calculated_flag is not UNSET:
            field_dict["calculatedFlag"] = calculated_flag
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if effect_date is not UNSET:
            field_dict["effectDate"] = effect_date
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date
        if fee_allocation_type is not UNSET:
            field_dict["feeAllocationType"] = fee_allocation_type
        if fee_notes is not UNSET:
            field_dict["feeNotes"] = fee_notes
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if max_fee is not UNSET:
            field_dict["maxFee"] = max_fee
        if min_fee is not UNSET:
            field_dict["minFee"] = min_fee
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
        from ..models.fee_item_model_code import FeeItemModelCode
        from ..models.fee_item_model_description import FeeItemModelDescription
        from ..models.fee_item_model_payment_period import FeeItemModelPaymentPeriod
        from ..models.fee_item_model_schedule import FeeItemModelSchedule
        from ..models.fee_item_model_sub_group import FeeItemModelSubGroup
        from ..models.fee_item_model_unit import FeeItemModelUnit
        from ..models.fee_item_model_version import FeeItemModelVersion
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        aca_required_flag = d.pop("acaRequiredFlag", UNSET)

        account_code_1 = d.pop("accountCode1", UNSET)

        account_code_1_allocation = d.pop("accountCode1Allocation", UNSET)

        account_code_2 = d.pop("accountCode2", UNSET)

        account_code_2_allocation = d.pop("accountCode2Allocation", UNSET)

        account_code_3 = d.pop("accountCode3", UNSET)

        account_code_3_allocation = d.pop("accountCode3Allocation", UNSET)

        allocated_fee_1 = d.pop("allocatedFee1", UNSET)

        allocated_fee_2 = d.pop("allocatedFee2", UNSET)

        allocated_fee_3 = d.pop("allocatedFee3", UNSET)

        amount = d.pop("amount", UNSET)

        _apply_date = d.pop("applyDate", UNSET)
        apply_date: Union[Unset, datetime.datetime]
        if isinstance(_apply_date, Unset):
            apply_date = UNSET
        else:
            apply_date = isoparse(_apply_date)

        auto_assess_flag = d.pop("autoAssessFlag", UNSET)

        auto_invoice_flag = d.pop("autoInvoiceFlag", UNSET)

        balance_due = d.pop("balanceDue", UNSET)

        calc_flag = d.pop("calcFlag", UNSET)

        calculated_flag = d.pop("calculatedFlag", UNSET)

        _code = d.pop("code", UNSET)
        code: Union[Unset, FeeItemModelCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = FeeItemModelCode.from_dict(_code)

        _description = d.pop("description", UNSET)
        description: Union[Unset, FeeItemModelDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = FeeItemModelDescription.from_dict(_description)

        display_order = d.pop("displayOrder", UNSET)

        _effect_date = d.pop("effectDate", UNSET)
        effect_date: Union[Unset, datetime.datetime]
        if isinstance(_effect_date, Unset):
            effect_date = UNSET
        else:
            effect_date = isoparse(_effect_date)

        _expire_date = d.pop("expireDate", UNSET)
        expire_date: Union[Unset, datetime.datetime]
        if isinstance(_expire_date, Unset):
            expire_date = UNSET
        else:
            expire_date = isoparse(_expire_date)

        fee_allocation_type = d.pop("feeAllocationType", UNSET)

        fee_notes = d.pop("feeNotes", UNSET)

        id = d.pop("id", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        max_fee = d.pop("maxFee", UNSET)

        min_fee = d.pop("minFee", UNSET)

        _payment_period = d.pop("paymentPeriod", UNSET)
        payment_period: Union[Unset, FeeItemModelPaymentPeriod]
        if isinstance(_payment_period, Unset):
            payment_period = UNSET
        else:
            payment_period = FeeItemModelPaymentPeriod.from_dict(_payment_period)

        priority = d.pop("priority", UNSET)

        quantity = d.pop("quantity", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, FeeItemModelSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FeeItemModelSchedule.from_dict(_schedule)

        status = d.pop("status", UNSET)

        _sub_group = d.pop("subGroup", UNSET)
        sub_group: Union[Unset, FeeItemModelSubGroup]
        if isinstance(_sub_group, Unset):
            sub_group = UNSET
        else:
            sub_group = FeeItemModelSubGroup.from_dict(_sub_group)

        udf1 = d.pop("udf1", UNSET)

        udf2 = d.pop("udf2", UNSET)

        udf3 = d.pop("udf3", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, FeeItemModelUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = FeeItemModelUnit.from_dict(_unit)

        variable = d.pop("variable", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FeeItemModelVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = FeeItemModelVersion.from_dict(_version)

        fee_item_model = cls(
            aca_required_flag=aca_required_flag,
            account_code_1=account_code_1,
            account_code_1_allocation=account_code_1_allocation,
            account_code_2=account_code_2,
            account_code_2_allocation=account_code_2_allocation,
            account_code_3=account_code_3,
            account_code_3_allocation=account_code_3_allocation,
            allocated_fee_1=allocated_fee_1,
            allocated_fee_2=allocated_fee_2,
            allocated_fee_3=allocated_fee_3,
            amount=amount,
            apply_date=apply_date,
            auto_assess_flag=auto_assess_flag,
            auto_invoice_flag=auto_invoice_flag,
            balance_due=balance_due,
            calc_flag=calc_flag,
            calculated_flag=calculated_flag,
            code=code,
            description=description,
            display_order=display_order,
            effect_date=effect_date,
            expire_date=expire_date,
            fee_allocation_type=fee_allocation_type,
            fee_notes=fee_notes,
            id=id,
            invoice_id=invoice_id,
            max_fee=max_fee,
            min_fee=min_fee,
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

        fee_item_model.additional_properties = d
        return fee_item_model

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
