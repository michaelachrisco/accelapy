from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseAuthorize")


@_attrs_define
class ResponseAuthorize:
    """
    Attributes:
        code (Union[Unset, str]): The authorization code (for an authorization code flow request where
            response_type=code). The client app uses the authorization code to exchange for an access token.
        environment (Union[Unset, str]): The environment name that the user selected when signing into the app (for an
            authorization code flow request where response_type=code).

            For an implicit flow request where response_type=token, environment is returned as a parameter in the
            redirection URI using the "application/x-www-form-urlencoded" format.
        agency_name (Union[Unset, str]): The agency name that the user entered when signing into the app (for an
            authorization code flow request where response_type=code).

            For an implicit flow request where response_type=token, agency_name is returned as a parameter in the
            redirection URI using the "application/x-www-form-urlencoded" format.
        state (Union[Unset, str]): The exact value received from the client (for an authorization code flow request
            where response_type=code). Check this value against original state value sent in the request to verify and
            protect against CSRF.

            For an implicit flow request where response_type=token, state is returned as a parameter in the redirection URI
            using the "application/x-www-form-urlencoded" format.
        access_token (Union[Unset, str]): The issued user access token (for an implicit flow request where
            response_type=token). access_token is returned as a parameter in the redirection URI using the
            "application/x-www-form-urlencoded" format.
        token_type (Union[Unset, str]): The type of the token issued (for an implicit flow request where
            response_type=token). token_type is returned as a parameter in the redirection URI using the "application/x-www-
            form-urlencoded" format.
        expires_in (Union[Unset, str]): The lifetime in seconds of the access token (for an implicit flow request where
            response_type=token). For example, the value "3600" denotes that the access token will expire in one hour from
            the time the response was generated. expires_in is returned as a parameter in the redirection URI using the
            "application/x-www-form-urlencoded" format.
        scope (Union[Unset, str]): The scope of the resources authenticated by the authorization server (for an implicit
            flow request where response_type=token). scope is returned as a parameter in the redirection URI using the
            "application/x-www-form-urlencoded" format.
    """

    code: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    agency_name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    expires_in: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        environment = self.environment
        agency_name = self.agency_name
        state = self.state
        access_token = self.access_token
        token_type = self.token_type
        expires_in = self.expires_in
        scope = self.scope

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if environment is not UNSET:
            field_dict["environment"] = environment
        if agency_name is not UNSET:
            field_dict["agency_name"] = agency_name
        if state is not UNSET:
            field_dict["state"] = state
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        environment = d.pop("environment", UNSET)

        agency_name = d.pop("agency_name", UNSET)

        state = d.pop("state", UNSET)

        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        scope = d.pop("scope", UNSET)

        response_authorize = cls(
            code=code,
            environment=environment,
            agency_name=agency_name,
            state=state,
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            scope=scope,
        )

        response_authorize.additional_properties = d
        return response_authorize

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
