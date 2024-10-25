import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_id_model import RecordIdModel


T = TypeVar("T", bound="PaymentModel")


@_attrs_define
class PaymentModel:
    """
    Attributes:
        amount (Union[Unset, float]): The amount of a payment transaction or account balance.
        amount_not_allocated (Union[Unset, float]): The payment amount which has not been allocated.
        cashier_id (Union[Unset, str]): The unique ID associated with the cashier.
        id (Union[Unset, int]): The payment system id assigned by the Civic Platform server.
        payment_date (Union[Unset, datetime.datetime]): The date a payment was entered into the system.
        payment_method (Union[Unset, str]): Describes the method of payment, for example; credit card, cash, debit card,
            and so forth.
        payment_status (Union[Unset, str]): Indicates whether or not a payment has been made in full.
        receipt_id (Union[Unset, int]): The unique ID generated for the recipient.
        record_id (Union[Unset, RecordIdModel]):
        transaction_code (Union[Unset, str]): An industry standard code that identifies the type of transaction.
        transaction_id (Union[Unset, int]): A unique number, assigned by the system, that indentifies the transaction.
    """

    amount: Union[Unset, float] = UNSET
    amount_not_allocated: Union[Unset, float] = UNSET
    cashier_id: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    payment_date: Union[Unset, datetime.datetime] = UNSET
    payment_method: Union[Unset, str] = UNSET
    payment_status: Union[Unset, str] = UNSET
    receipt_id: Union[Unset, int] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    transaction_code: Union[Unset, str] = UNSET
    transaction_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        amount_not_allocated = self.amount_not_allocated
        cashier_id = self.cashier_id
        id = self.id
        payment_date: Union[Unset, str] = UNSET
        if not isinstance(self.payment_date, Unset):
            payment_date = self.payment_date.isoformat()

        payment_method = self.payment_method
        payment_status = self.payment_status
        receipt_id = self.receipt_id
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        transaction_code = self.transaction_code
        transaction_id = self.transaction_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_not_allocated is not UNSET:
            field_dict["amountNotAllocated"] = amount_not_allocated
        if cashier_id is not UNSET:
            field_dict["cashierId"] = cashier_id
        if id is not UNSET:
            field_dict["id"] = id
        if payment_date is not UNSET:
            field_dict["paymentDate"] = payment_date
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if receipt_id is not UNSET:
            field_dict["receiptId"] = receipt_id
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if transaction_code is not UNSET:
            field_dict["transactionCode"] = transaction_code
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_id_model import RecordIdModel

        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        amount_not_allocated = d.pop("amountNotAllocated", UNSET)

        cashier_id = d.pop("cashierId", UNSET)

        id = d.pop("id", UNSET)

        _payment_date = d.pop("paymentDate", UNSET)
        payment_date: Union[Unset, datetime.datetime]
        if isinstance(_payment_date, Unset):
            payment_date = UNSET
        else:
            payment_date = isoparse(_payment_date)

        payment_method = d.pop("paymentMethod", UNSET)

        payment_status = d.pop("paymentStatus", UNSET)

        receipt_id = d.pop("receiptId", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        transaction_code = d.pop("transactionCode", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        payment_model = cls(
            amount=amount,
            amount_not_allocated=amount_not_allocated,
            cashier_id=cashier_id,
            id=id,
            payment_date=payment_date,
            payment_method=payment_method,
            payment_status=payment_status,
            receipt_id=receipt_id,
            record_id=record_id,
            transaction_code=transaction_code,
            transaction_id=transaction_id,
        )

        payment_model.additional_properties = d
        return payment_model

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
