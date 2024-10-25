from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_item_base_model_1_code import FeeItemBaseModel1Code
    from ..models.fee_item_base_model_1_payment_period import FeeItemBaseModel1PaymentPeriod
    from ..models.fee_item_base_model_1_schedule import FeeItemBaseModel1Schedule
    from ..models.fee_item_base_model_1_version import FeeItemBaseModel1Version


T = TypeVar("T", bound="FeeItemBaseModel1")


@_attrs_define
class FeeItemBaseModel1:
    """
    Attributes:
        code (Union[Unset, FeeItemBaseModel1Code]): The fee item code.
        id (Union[Unset, int]): The fee item system id assigned by the Civic Platform server.
        notes (Union[Unset, str]): A note entered against a fee item.
        payment_period (Union[Unset, FeeItemBaseModel1PaymentPeriod]): The time interval for processing invoices.
        quantity (Union[Unset, float]): The number of units for which the fee applies.
        schedule (Union[Unset, FeeItemBaseModel1Schedule]): Contains parameters that define the fee schedule. See [Get
            All Fee Schedules for Record Type](./api-
            settings.html#operation/v4.get.settings.records.types.id.fees.schedules).
        version (Union[Unset, FeeItemBaseModel1Version]): The fee item version.
    """

    code: Union[Unset, "FeeItemBaseModel1Code"] = UNSET
    id: Union[Unset, int] = UNSET
    notes: Union[Unset, str] = UNSET
    payment_period: Union[Unset, "FeeItemBaseModel1PaymentPeriod"] = UNSET
    quantity: Union[Unset, float] = UNSET
    schedule: Union[Unset, "FeeItemBaseModel1Schedule"] = UNSET
    version: Union[Unset, "FeeItemBaseModel1Version"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        id = self.id
        notes = self.notes
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
        if id is not UNSET:
            field_dict["id"] = id
        if notes is not UNSET:
            field_dict["notes"] = notes
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
        from ..models.fee_item_base_model_1_code import FeeItemBaseModel1Code
        from ..models.fee_item_base_model_1_payment_period import FeeItemBaseModel1PaymentPeriod
        from ..models.fee_item_base_model_1_schedule import FeeItemBaseModel1Schedule
        from ..models.fee_item_base_model_1_version import FeeItemBaseModel1Version

        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, FeeItemBaseModel1Code]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = FeeItemBaseModel1Code.from_dict(_code)

        id = d.pop("id", UNSET)

        notes = d.pop("notes", UNSET)

        _payment_period = d.pop("paymentPeriod", UNSET)
        payment_period: Union[Unset, FeeItemBaseModel1PaymentPeriod]
        if isinstance(_payment_period, Unset):
            payment_period = UNSET
        else:
            payment_period = FeeItemBaseModel1PaymentPeriod.from_dict(_payment_period)

        quantity = d.pop("quantity", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, FeeItemBaseModel1Schedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FeeItemBaseModel1Schedule.from_dict(_schedule)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FeeItemBaseModel1Version]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = FeeItemBaseModel1Version.from_dict(_version)

        fee_item_base_model_1 = cls(
            code=code,
            id=id,
            notes=notes,
            payment_period=payment_period,
            quantity=quantity,
            schedule=schedule,
            version=version,
        )

        fee_item_base_model_1.additional_properties = d
        return fee_item_base_model_1

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
