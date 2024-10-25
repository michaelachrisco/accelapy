from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseTokeninfo")


@_attrs_define
class ResponseTokeninfo:
    """
    Attributes:
        app_id (Union[Unset, str]): The app ID value from [Construct Developer Portal](https://developer.accela.com).
            This value is passed in your access token request.
        user_id (Union[Unset, str]): The logged in user's unique id.
        agency_name (Union[Unset, str]): The agency name defined in the Accela Administrator Portal. The agency name is
            passed by client request or chosen by the end-user during access token request flow.
        scopes (Union[Unset, List[str]]):
        expires_in (Union[Unset, int]): The lifetime in seconds of the access token.
        state (Union[Unset, str]): The exact value received from the client.
    """

    app_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    agency_name: Union[Unset, str] = UNSET
    scopes: Union[Unset, List[str]] = UNSET
    expires_in: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_id = self.app_id
        user_id = self.user_id
        agency_name = self.agency_name
        scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        expires_in = self.expires_in
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if agency_name is not UNSET:
            field_dict["agencyName"] = agency_name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        user_id = d.pop("userId", UNSET)

        agency_name = d.pop("agencyName", UNSET)

        scopes = cast(List[str], d.pop("scopes", UNSET))

        expires_in = d.pop("expiresIn", UNSET)

        state = d.pop("state", UNSET)

        response_tokeninfo = cls(
            app_id=app_id,
            user_id=user_id,
            agency_name=agency_name,
            scopes=scopes,
            expires_in=expires_in,
            state=state,
        )

        response_tokeninfo.additional_properties = d
        return response_tokeninfo

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
