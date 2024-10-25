import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_expiration_model_expiration_status import RecordExpirationModelExpirationStatus


T = TypeVar("T", bound="RecordExpirationModel")


@_attrs_define
class RecordExpirationModel:
    """
    Attributes:
        expiration_date (Union[Unset, datetime.datetime]): The date when the condition expires.
        expiration_status (Union[Unset, RecordExpirationModelExpirationStatus]): Indicates whether the expiration is
            enabled or disabled. See [Get All Record Expiration Statuses](./api-
            settings.html#operation/v4.get.settings.records.expirationStatuses).
    """

    expiration_date: Union[Unset, datetime.datetime] = UNSET
    expiration_status: Union[Unset, "RecordExpirationModelExpirationStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        expiration_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expiration_status, Unset):
            expiration_status = self.expiration_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if expiration_status is not UNSET:
            field_dict["expirationStatus"] = expiration_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_expiration_model_expiration_status import RecordExpirationModelExpirationStatus

        d = src_dict.copy()
        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        _expiration_status = d.pop("expirationStatus", UNSET)
        expiration_status: Union[Unset, RecordExpirationModelExpirationStatus]
        if isinstance(_expiration_status, Unset):
            expiration_status = UNSET
        else:
            expiration_status = RecordExpirationModelExpirationStatus.from_dict(_expiration_status)

        record_expiration_model = cls(
            expiration_date=expiration_date,
            expiration_status=expiration_status,
        )

        record_expiration_model.additional_properties = d
        return record_expiration_model

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
