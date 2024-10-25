from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_token_grant_type import RequestTokenGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestToken")


@_attrs_define
class RequestToken:
    """
    Attributes:
        client_id (str): The app ID value from [Construct Developer Portal](https://developer.accela.com).
        client_secret (str): The app secret value from [Construct Developer Portal](https://developer.accela.com).
        grant_type (RequestTokenGrantType): Specifies whether the request is for an authorization code, password
            credential access token, or refresh token. Valid values:

            Values:

            authorization_code - Request to exchange the given authorization code with an access token. Used with
            [Authorization Code Flow](../construct-authCodeFlow.html).

            password - Request authentication via userid and password credential. See [Password Credential
            Login](../construct-passwordCredentialLogin.html).

            refresh_token - Request to refresh the token.

            **Note**: Make sure the grant_type value does not contain any space character.
        code (str): The authorization code obtained from the preceding [/oauth2/authorize](#operation/oauth2.authorize)
            request.

            **Note**: code is required only when calling this API with grant_type=authorization_code for [Authorization Code
            Flow](../construct-authCodeFlow.html).

            **Note**: The code should be URL-encoded, if you are using tools or libraries which will auto-encode the code,
            you need to pass the code under decoded.

            **Note**: The code can be used no more than one time, the client should apply the rule during exchange access
            token.
        redirect_uri (str): The URI that is used to redirect to the client with an access token.

            **Note**: redirect_uri is required only when calling this API with grant_type=authorization_code for
            [Authorization Code Flow](../construct-authCodeFlow.html).

            **Note**: The value of redirect_uri must match the redirect_uri used in the preceding
            [/oauth2/authorize](#operation/oauth2.authorize) request.
        username (str): For a **citizen app**, the user name is the Civic ID.
            For an **agency app**, the user name is the Civic Platform account.

            **Note**: username is required only when calling this API with grant_type=password for [Password Credential
            Login](../construct-passwordCredentialLogin.html).
        password (str): For a **citizen app**, the user name is the Civic ID password.
            For an **agency app**, the user name is the Civic Platform password.

            **Note**: username is required only when calling this API with grant_type=password for [Password Credential
            Login](../construct-passwordCredentialLogin.html).
        agency_name (str): The agency name defined in [Construct Administrator Portal](https://admin.accela.com). APIs
            such as [Get All Agencies](./api-agencies.html#operation/v4.get.agencies), [Get Agency](./api-
            agencies.html#operation/v4.get.agencies.name), and [Search Agencies](./api-
            search.html#operation/v4.post.search.agencies) return valid agency names.

            **Note**: agency_name is used only when calling this API with grant_type=password for [Password Credential
            Login](../construct-passwordCredentialLogin.html). For an **agency app**, agency_name is required.
            For a **citizen app**, agency_name is optional.
        environment (str): The Construct environment name, such as "PROD" and "TEST". The [Get All Agency
            Environments](./api-agencies.html#operation/v4.get.agencies.name.environments) API returns a list of configured
            environments available for a specific agency. The [Get Environment Status](./api-
            agencies.html#operation/v4.get.agencies.name.environments.env.status) checks connectivity with the
            Agency/Environment..

            **Note**: scope is required only when calling this API with grant_type=password for [Password Credential
            Login](../construct-passwordCredentialLogin.html).
        scope (Union[Unset, str]): The scope of the resources that the client requests. Enter a list of APIs scope names
            separated by spaces. Get the scope names from the [Accela API Reference](./api-index.html).

            **Note**: scope is required only when calling this API with grant_type=password for [Password Credential
            Login](../construct-passwordCredentialLogin.html).
        refresh_token (Union[Unset, str]): The refresh token value obtained in the prior access token API request.

            **Note**: refresh_token is required only when calling this API to refresh the token for both [Authorization Code
            Flow](../construct-authCodeFlow.html) and [Password Credential Login](../construct-
            passwordCredentialLogin.html).
        state (Union[Unset, str]): An opaque value that the client uses for maintaining the state between the request
            and callback. Enter a unique value. This can be used for [Cross-Site Request
            Forgery](http://en.wikipedia.org/wiki/Cross-site_request_forgery) (CSRF) protection.

            This parameter is not used when refreshing a token.

            **Note**: state is used and optional only when calling this API with grant_type=authorization_code for
            [Authorization Code Flow](../construct-authCodeFlow.html).
    """

    client_id: str
    client_secret: str
    grant_type: RequestTokenGrantType
    code: str
    redirect_uri: str
    username: str
    password: str
    agency_name: str
    environment: str
    scope: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        client_secret = self.client_secret
        grant_type = self.grant_type.value

        code = self.code
        redirect_uri = self.redirect_uri
        username = self.username
        password = self.password
        agency_name = self.agency_name
        environment = self.environment
        scope = self.scope
        refresh_token = self.refresh_token
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": redirect_uri,
                "username": username,
                "password": password,
                "agency_name": agency_name,
                "environment": environment,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        grant_type = RequestTokenGrantType(d.pop("grant_type"))

        code = d.pop("code")

        redirect_uri = d.pop("redirect_uri")

        username = d.pop("username")

        password = d.pop("password")

        agency_name = d.pop("agency_name")

        environment = d.pop("environment")

        scope = d.pop("scope", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        state = d.pop("state", UNSET)

        request_token = cls(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            username=username,
            password=password,
            agency_name=agency_name,
            environment=environment,
            scope=scope,
            refresh_token=refresh_token,
            state=state,
        )

        request_token.additional_properties = d
        return request_token

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
