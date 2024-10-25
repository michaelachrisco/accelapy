from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseToken")


@_attrs_define
class ResponseToken:
    """
    Attributes:
        access_token (Union[Unset, str]): The issued user access token.
        token_type (Union[Unset, str]): The type of the token issued. It contains the fixed value "bearer" for
            authorization_code grant type.
        expires_in (Union[Unset, str]): The lifetime in seconds of the access token. For example, the value "3600"
            denotes that the access token will expire in one hour from the time the response was generated.
        refresh_token (Union[Unset, str]): The refresh token that can be used to obtain a new access token.
        scope (Union[Unset, str]): The scope of the resources authenticated by the authorization server.
        state (Union[Unset, str]): The exact value received from the client.
    """

    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    expires_in: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        token_type = self.token_type
        expires_in = self.expires_in
        refresh_token = self.refresh_token
        scope = self.scope
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        scope = d.pop("scope", UNSET)

        state = d.pop("state", UNSET)

        response_token = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            refresh_token=refresh_token,
            scope=scope,
            state=state,
        )

        response_token.additional_properties = d
        return response_token

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
