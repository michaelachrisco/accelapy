from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    *,
    content_type: str,
    x_accela_appid: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Content-Type"] = content_type

    headers["x-accela-appid"] = x_accela_appid

    return {
        "method": "post",
        "url": "/oauth2/token",
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content_type: str,
    x_accela_appid: str,
) -> Response[Any]:
    """Get Access Token

     Gets an access token from the authentication server.



    This API is used for the following:

    - [Authorization Code Flow](../construct-authCodeFlow.html) - set the request parameter
    grant_type=authorization_code.

    - [Password Credential Login](../construct-passwordCredentialLogin.html) - set the request parameter
    grant_type=password.

    - Refreshing the token - set the request parameter grant_type=refresh_token. Access tokens have a
    limited lifetime and, in some cases, an application needs access to an API beyond the lifetime of a
    single access token. When this is the case, your application can obtain a new access token using the
    refresh token. Your app can refresh the token before it expires or when it expires, according your
    app requirements or workflow.



    **API Endpoint**:  POST /oauth2/token

    Args:
        content_type (str):
        x_accela_appid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
        x_accela_appid=x_accela_appid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content_type: str,
    x_accela_appid: str,
) -> Response[Any]:
    """Get Access Token

     Gets an access token from the authentication server.



    This API is used for the following:

    - [Authorization Code Flow](../construct-authCodeFlow.html) - set the request parameter
    grant_type=authorization_code.

    - [Password Credential Login](../construct-passwordCredentialLogin.html) - set the request parameter
    grant_type=password.

    - Refreshing the token - set the request parameter grant_type=refresh_token. Access tokens have a
    limited lifetime and, in some cases, an application needs access to an API beyond the lifetime of a
    single access token. When this is the case, your application can obtain a new access token using the
    refresh token. Your app can refresh the token before it expires or when it expires, according your
    app requirements or workflow.



    **API Endpoint**:  POST /oauth2/token

    Args:
        content_type (str):
        x_accela_appid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
        x_accela_appid=x_accela_appid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
