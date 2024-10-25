from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trust_account_model_is_primary import TrustAccountModelIsPrimary
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_id_model import RecordIdModel
    from ..models.trust_account_model_associations import TrustAccountModelAssociations
    from ..models.trust_account_model_overdraft import TrustAccountModelOverdraft
    from ..models.trust_account_model_status import TrustAccountModelStatus


T = TypeVar("T", bound="TrustAccountModel")


@_attrs_define
class TrustAccountModel:
    """
    Attributes:
        account (Union[Unset, str]): The account ID number for the trust account.
        associations (Union[Unset, TrustAccountModelAssociations]): The trust account associations.
        balance (Union[Unset, float]): The balance of the trust account in dollars.
        description (Union[Unset, str]): The description of the trust account.
        id (Union[Unset, int]): The trust account system id assigned by the Civic Platform server.
        is_primary (Union[Unset, TrustAccountModelIsPrimary]): Indicates whether or not to designate the trust account
            as the primary source.
        ledger_account (Union[Unset, str]): The ledger account of the trust account.
        overdraft (Union[Unset, TrustAccountModelOverdraft]): Indicates whether or not the trust account can use the
            overdraft option.
        overdraft_limit (Union[Unset, float]): The overdraft limit amount, in dollars, for the trust account.
        record_id (Union[Unset, RecordIdModel]):
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        status (Union[Unset, TrustAccountModelStatus]): The status of the trust account.
        threshold_amount (Union[Unset, float]): The minimum amount required in a trust account.
    """

    account: Union[Unset, str] = UNSET
    associations: Union[Unset, "TrustAccountModelAssociations"] = UNSET
    balance: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_primary: Union[Unset, TrustAccountModelIsPrimary] = UNSET
    ledger_account: Union[Unset, str] = UNSET
    overdraft: Union[Unset, "TrustAccountModelOverdraft"] = UNSET
    overdraft_limit: Union[Unset, float] = UNSET
    record_id: Union[Unset, "RecordIdModel"] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    status: Union[Unset, "TrustAccountModelStatus"] = UNSET
    threshold_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account
        associations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.associations, Unset):
            associations = self.associations.to_dict()

        balance = self.balance
        description = self.description
        id = self.id
        is_primary: Union[Unset, str] = UNSET
        if not isinstance(self.is_primary, Unset):
            is_primary = self.is_primary.value

        ledger_account = self.ledger_account
        overdraft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.overdraft, Unset):
            overdraft = self.overdraft.to_dict()

        overdraft_limit = self.overdraft_limit
        record_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = self.record_id.to_dict()

        service_provider_code = self.service_provider_code
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        threshold_amount = self.threshold_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if associations is not UNSET:
            field_dict["associations"] = associations
        if balance is not UNSET:
            field_dict["balance"] = balance
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if ledger_account is not UNSET:
            field_dict["ledgerAccount"] = ledger_account
        if overdraft is not UNSET:
            field_dict["overdraft"] = overdraft
        if overdraft_limit is not UNSET:
            field_dict["overdraftLimit"] = overdraft_limit
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if status is not UNSET:
            field_dict["status"] = status
        if threshold_amount is not UNSET:
            field_dict["thresholdAmount"] = threshold_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_id_model import RecordIdModel
        from ..models.trust_account_model_associations import TrustAccountModelAssociations
        from ..models.trust_account_model_overdraft import TrustAccountModelOverdraft
        from ..models.trust_account_model_status import TrustAccountModelStatus

        d = src_dict.copy()
        account = d.pop("account", UNSET)

        _associations = d.pop("associations", UNSET)
        associations: Union[Unset, TrustAccountModelAssociations]
        if isinstance(_associations, Unset):
            associations = UNSET
        else:
            associations = TrustAccountModelAssociations.from_dict(_associations)

        balance = d.pop("balance", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _is_primary = d.pop("isPrimary", UNSET)
        is_primary: Union[Unset, TrustAccountModelIsPrimary]
        if isinstance(_is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = TrustAccountModelIsPrimary(_is_primary)

        ledger_account = d.pop("ledgerAccount", UNSET)

        _overdraft = d.pop("overdraft", UNSET)
        overdraft: Union[Unset, TrustAccountModelOverdraft]
        if isinstance(_overdraft, Unset):
            overdraft = UNSET
        else:
            overdraft = TrustAccountModelOverdraft.from_dict(_overdraft)

        overdraft_limit = d.pop("overdraftLimit", UNSET)

        _record_id = d.pop("recordId", UNSET)
        record_id: Union[Unset, RecordIdModel]
        if isinstance(_record_id, Unset):
            record_id = UNSET
        else:
            record_id = RecordIdModel.from_dict(_record_id)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, TrustAccountModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TrustAccountModelStatus.from_dict(_status)

        threshold_amount = d.pop("thresholdAmount", UNSET)

        trust_account_model = cls(
            account=account,
            associations=associations,
            balance=balance,
            description=description,
            id=id,
            is_primary=is_primary,
            ledger_account=ledger_account,
            overdraft=overdraft,
            overdraft_limit=overdraft_limit,
            record_id=record_id,
            service_provider_code=service_provider_code,
            status=status,
            threshold_amount=threshold_amount,
        )

        trust_account_model.additional_properties = d
        return trust_account_model

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
