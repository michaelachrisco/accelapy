from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_model import IdentifierModel


T = TypeVar("T", bound="OwnerAddressModel")


@_attrs_define
class OwnerAddressModel:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        address_line_3 (Union[Unset, str]):
        city (Union[Unset, str]):
        country (Union[Unset, IdentifierModel]):
        postal_code (Union[Unset, str]):
        state (Union[Unset, IdentifierModel]):
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, "IdentifierModel"] = UNSET
    postal_code: Union[Unset, str] = UNSET
    state: Union[Unset, "IdentifierModel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line_1 = self.address_line_1
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        city = self.city
        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        postal_code = self.postal_code
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_model import IdentifierModel

        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, IdentifierModel]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = IdentifierModel.from_dict(_country)

        postal_code = d.pop("postalCode", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, IdentifierModel]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = IdentifierModel.from_dict(_state)

        owner_address_model = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            city=city,
            country=country,
            postal_code=postal_code,
            state=state,
        )

        owner_address_model.additional_properties = d
        return owner_address_model

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
