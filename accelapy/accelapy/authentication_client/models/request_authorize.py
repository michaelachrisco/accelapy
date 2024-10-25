from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_authorize_response_type import RequestAuthorizeResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestAuthorize")


@_attrs_define
class RequestAuthorize:
    """
    Attributes:
        response_type (RequestAuthorizeResponseType): Specifies whether the request is for an authorization code or
            access token.

            Valid values:

            *code* - Request for an authorization code. See [Authorization Code Flow](../construct-authCodeFlow.html).

            *token* - Request for an access token. See [Implicit Flow](../construct-implicitFlow.html).
        client_id (str): The app ID value from [Construct Developer Portal](https://developer.accela.com).
        redirect_uri (str): The URI that is used to redirect to the client with an authorization code. This must be a
            valid URL.

            **Note**: Special characters in the URL should be encoded.
        environment (str): The Construct environment name, such as "PROD" and "TEST". The [Get All Agency
            Environments](./api-agencies.html#operation/v4.get.agencies.name.environments) API returns a list of configured
            environments available for a specific agency. The [Get Environment Status](./api-
            agencies.html#operation/v4.get.agencies.name.environments.env.status) checks connectivity with the
            Agency/Environment.
        agency_name (str): The agency name defined in [Construct Administrator Portal](https://admin.accela.com). APIs
            such as [Get All Agencies](./api-agencies.html#operation/v4.get.agencies), [Get Agency](./api-
            agencies.html#operation/v4.get.agencies.name), and [Search Agencies](./api-
            search.html#operation/v4.post.search.agencies) return valid agency names.

            **Note**: For an **agency app**, agency is required.
            For a **citizen app** that use dynamic agency routing functionality, agency_name is optional.
        forcelogin (Union[Unset, bool]): Indicates whether or not Accela Auth server forces end-user login each time
            client requests access token.

            Valid values:

            *true*: Always force end-user login.

            *false*: Do not force end-user login. The sever determines if the current request needs login. This is the
            default behavior.
        scope (Union[Unset, str]): The scope of the resources that the client requests. Enter a list of APIs scope names
            separated by spaces. Get the scope names from the [Accela API Reference](./api-index.html).
        state (Union[Unset, str]): An opaque value that the client uses for maintaining the state between the request
            and callback. Enter a unique value. This can be used for [Cross-Site Request
            Forgery](http://en.wikipedia.org/wiki/Cross-site_request_forgery) (CSRF) protection.
    """

    response_type: RequestAuthorizeResponseType
    client_id: str
    redirect_uri: str
    environment: str
    agency_name: str
    forcelogin: Union[Unset, bool] = UNSET
    scope: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        response_type = self.response_type.value

        client_id = self.client_id
        redirect_uri = self.redirect_uri
        environment = self.environment
        agency_name = self.agency_name
        forcelogin = self.forcelogin
        scope = self.scope
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "environment": environment,
                "agency_name": agency_name,
            }
        )
        if forcelogin is not UNSET:
            field_dict["forcelogin"] = forcelogin
        if scope is not UNSET:
            field_dict["scope"] = scope
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        response_type = RequestAuthorizeResponseType(d.pop("response_type"))

        client_id = d.pop("client_id")

        redirect_uri = d.pop("redirect_uri")

        environment = d.pop("environment")

        agency_name = d.pop("agency_name")

        forcelogin = d.pop("forcelogin", UNSET)

        scope = d.pop("scope", UNSET)

        state = d.pop("state", UNSET)

        request_authorize = cls(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            environment=environment,
            agency_name=agency_name,
            forcelogin=forcelogin,
            scope=scope,
            state=state,
        )

        request_authorize.additional_properties = d
        return request_authorize

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
