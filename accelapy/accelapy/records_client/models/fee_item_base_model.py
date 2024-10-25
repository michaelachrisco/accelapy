from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_item_base_model_code import FeeItemBaseModelCode
    from ..models.fee_item_base_model_payment_period import FeeItemBaseModelPaymentPeriod
    from ..models.fee_item_base_model_schedule import FeeItemBaseModelSchedule
    from ..models.fee_item_base_model_version import FeeItemBaseModelVersion


T = TypeVar("T", bound="FeeItemBaseModel")


@_attrs_define
class FeeItemBaseModel:
    """
    Attributes:
        code (Union[Unset, FeeItemBaseModelCode]): The fee item code.
        fee_notes (Union[Unset, str]): Notes about the fee.
        id (Union[Unset, int]): The fee item system id assigned by the Civic Platform server.
        payment_period (Union[Unset, FeeItemBaseModelPaymentPeriod]): The time interval for processing invoices.
        quantity (Union[Unset, float]): The number of units for which the same fee applies.
        schedule (Union[Unset, FeeItemBaseModelSchedule]): Contains parameters that define the fee schedule.
        version (Union[Unset, FeeItemBaseModelVersion]): The fee schedule version.
    """

    code: Union[Unset, "FeeItemBaseModelCode"] = UNSET
    fee_notes: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    payment_period: Union[Unset, "FeeItemBaseModelPaymentPeriod"] = UNSET
    quantity: Union[Unset, float] = UNSET
    schedule: Union[Unset, "FeeItemBaseModelSchedule"] = UNSET
    version: Union[Unset, "FeeItemBaseModelVersion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        fee_notes = self.fee_notes
        id = self.id
        payment_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_period, Unset):
            payment_period = self.payment_period.to_dict()

        quantity = self.quantity
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if fee_notes is not UNSET:
            field_dict["feeNotes"] = fee_notes
        if id is not UNSET:
            field_dict["id"] = id
        if payment_period is not UNSET:
            field_dict["paymentPeriod"] = payment_period
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_item_base_model_code import FeeItemBaseModelCode
        from ..models.fee_item_base_model_payment_period import FeeItemBaseModelPaymentPeriod
        from ..models.fee_item_base_model_schedule import FeeItemBaseModelSchedule
        from ..models.fee_item_base_model_version import FeeItemBaseModelVersion

        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, FeeItemBaseModelCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = FeeItemBaseModelCode.from_dict(_code)

        fee_notes = d.pop("feeNotes", UNSET)

        id = d.pop("id", UNSET)

        _payment_period = d.pop("paymentPeriod", UNSET)
        payment_period: Union[Unset, FeeItemBaseModelPaymentPeriod]
        if isinstance(_payment_period, Unset):
            payment_period = UNSET
        else:
            payment_period = FeeItemBaseModelPaymentPeriod.from_dict(_payment_period)

        quantity = d.pop("quantity", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, FeeItemBaseModelSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FeeItemBaseModelSchedule.from_dict(_schedule)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FeeItemBaseModelVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = FeeItemBaseModelVersion.from_dict(_version)

        fee_item_base_model = cls(
            code=code,
            fee_notes=fee_notes,
            id=id,
            payment_period=payment_period,
            quantity=quantity,
            schedule=schedule,
            version=version,
        )

        fee_item_base_model.additional_properties = d
        return fee_item_base_model

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
