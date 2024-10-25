import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invoice_model_printed import InvoiceModelPrinted
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_item_model import FeeItemModel
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="InvoiceModel")


@_attrs_define
class InvoiceModel:
    """
    Attributes:
        amount (Union[Unset, float]): The invoice fee amount.
        audit_status (Union[Unset, str]): The audit status of the invoice fee item.
        balance (Union[Unset, float]): The amount due.
        due_date (Union[Unset, datetime.datetime]): The invoice due date.
        fees (Union[Unset, List['FeeItemModel']]):
        id (Union[Unset, int]): The unique id of the invoice.
        inv_batch_date (Union[Unset, datetime.datetime]): The invoice batch date.
        inv_comment (Union[Unset, str]): A comment related to the invoice.
        inv_status (Union[Unset, str]): The invoice status.
        invoice_date (Union[Unset, datetime.datetime]): The invoice date.
        invoice_number (Union[Unset, str]): The invoice number string.
        printed (Union[Unset, InvoiceModelPrinted]): Indicates whether or not the invoice is printed.
        record_id (Union[Unset, RecordIdModel]):
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        udf1 (Union[Unset, str]): Invoice user defined field 1.
        udf2 (Union[Unset, str]): Invoice user defined field 2.
        udf3 (Union[Unset, str]): Invoice user defined field 3.
        udf4 (Union[Unset, str]): Invoice user defined field 4.
    """

    amount: Union[Unset, float] = UNSET
    audit_status: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    fees: Union[Unset, List["FeeItemModel"]] = UNSET
    id: Union[Unset, int] = UNSET
    inv_batch_date: Union[Unset, datetime.datetime] = UNSET
    inv_comment: Union[Unset, str] = UNSET
    inv_status: Union[Unset, str] = UNSET
    invoice_date: Union[Unset, datetime.datetime] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    printed: Union[Unset, InvoiceModelPrinted] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    udf1: Union[Unset, str] = UNSET
    udf2: Union[Unset, str] = UNSET
    udf3: Union[Unset, str] = UNSET
    udf4: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        audit_status = self.audit_status
        balance = self.balance
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        fees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()

                fees.append(fees_item)

        id = self.id
        inv_batch_date: Union[Unset, str] = UNSET
        if not isinstance(self.inv_batch_date, Unset):
            inv_batch_date = self.inv_batch_date.isoformat()

        inv_comment = self.inv_comment
        inv_status = self.inv_status
        invoice_date: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_date, Unset):
            invoice_date = self.invoice_date.isoformat()

        invoice_number = self.invoice_number
        printed: Union[Unset, str] = UNSET
        if not isinstance(self.printed, Unset):
            printed = self.printed.value

        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        service_provider_code = self.service_provider_code
        udf1 = self.udf1
        udf2 = self.udf2
        udf3 = self.udf3
        udf4 = self.udf4

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if audit_status is not UNSET:
            field_dict["auditStatus"] = audit_status
        if balance is not UNSET:
            field_dict["balance"] = balance
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if fees is not UNSET:
            field_dict["fees"] = fees
        if id is not UNSET:
            field_dict["id"] = id
        if inv_batch_date is not UNSET:
            field_dict["invBatchDate"] = inv_batch_date
        if inv_comment is not UNSET:
            field_dict["invComment"] = inv_comment
        if inv_status is not UNSET:
            field_dict["invStatus"] = inv_status
        if invoice_date is not UNSET:
            field_dict["invoiceDate"] = invoice_date
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if printed is not UNSET:
            field_dict["printed"] = printed
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if udf1 is not UNSET:
            field_dict["udf1"] = udf1
        if udf2 is not UNSET:
            field_dict["udf2"] = udf2
        if udf3 is not UNSET:
            field_dict["udf3"] = udf3
        if udf4 is not UNSET:
            field_dict["udf4"] = udf4

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_item_model import FeeItemModel
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        audit_status = d.pop("auditStatus", UNSET)

        balance = d.pop("balance", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = FeeItemModel.from_dict(fees_item_data)

            fees.append(fees_item)

        id = d.pop("id", UNSET)

        _inv_batch_date = d.pop("invBatchDate", UNSET)
        inv_batch_date: Union[Unset, datetime.datetime]
        if isinstance(_inv_batch_date, Unset):
            inv_batch_date = UNSET
        else:
            inv_batch_date = isoparse(_inv_batch_date)

        inv_comment = d.pop("invComment", UNSET)

        inv_status = d.pop("invStatus", UNSET)

        _invoice_date = d.pop("invoiceDate", UNSET)
        invoice_date: Union[Unset, datetime.datetime]
        if isinstance(_invoice_date, Unset):
            invoice_date = UNSET
        else:
            invoice_date = isoparse(_invoice_date)

        invoice_number = d.pop("invoiceNumber", UNSET)

        _printed = d.pop("printed", UNSET)
        printed: Union[Unset, InvoiceModelPrinted]
        if isinstance(_printed, Unset):
            printed = UNSET
        else:
            printed = InvoiceModelPrinted(_printed)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        udf1 = d.pop("udf1", UNSET)

        udf2 = d.pop("udf2", UNSET)

        udf3 = d.pop("udf3", UNSET)

        udf4 = d.pop("udf4", UNSET)

        invoice_model = cls(
            amount=amount,
            audit_status=audit_status,
            balance=balance,
            due_date=due_date,
            fees=fees,
            id=id,
            inv_batch_date=inv_batch_date,
            inv_comment=inv_comment,
            inv_status=inv_status,
            invoice_date=invoice_date,
            invoice_number=invoice_number,
            printed=printed,
            record_id=record_id,
            service_provider_code=service_provider_code,
            udf1=udf1,
            udf2=udf2,
            udf3=udf3,
            udf4=udf4,
        )

        invoice_model.additional_properties = d
        return invoice_model

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
