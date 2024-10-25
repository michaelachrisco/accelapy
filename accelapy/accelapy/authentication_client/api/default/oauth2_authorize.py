from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/oauth2/authorize",
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
) -> Response[Any]:
    """Get Authorization Code

     Gets an authorization code (for authorization code flow) or access token (for implicit flow) from
    the authentication server.

    This API is used for the following:

    - [Authorization Code Flow](../construct-authCodeFlow.html) - set the request parameter
    response_type=code. If successful, the authorization code will be returned in the response body. Use
    the authorization code to get the access token from [Get Access Token](#operation/oauth2.token).

    - [Implicit Flow](../construct-implicitFlow.html) - set the request parameter response_type=token.
    If successful, the access token will be returned in the access_token parameter in the redirect URL.

    **Note**: You can invoke this API using the HTTP GET method. In which case, specify the described
    request body fields as request query parameters.



    **API Endpoint**:  POST /oauth2/authorize

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Get Authorization Code

     Gets an authorization code (for authorization code flow) or access token (for implicit flow) from
    the authentication server.

    This API is used for the following:

    - [Authorization Code Flow](../construct-authCodeFlow.html) - set the request parameter
    response_type=code. If successful, the authorization code will be returned in the response body. Use
    the authorization code to get the access token from [Get Access Token](#operation/oauth2.token).

    - [Implicit Flow](../construct-implicitFlow.html) - set the request parameter response_type=token.
    If successful, the access token will be returned in the access_token parameter in the redirect URL.

    **Note**: You can invoke this API using the HTTP GET method. In which case, specify the described
    request body fields as request query parameters.



    **API Endpoint**:  POST /oauth2/authorize

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
