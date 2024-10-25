from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    record_id: str,
    *,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/v4/records/{recordId}/finalize".format(
            recordId=record_id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
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
    record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    """Finalize Record

     Creates the finalized record in the database. Use this method after calling Create Partial Record to
    submit the completed record. See [Creating Records](https://developer.accela.com/docs/construct-api-
    records.html#construct-api-records__creatingRecords) for more information about calling Finalize
    Record in tandem with Create Partial Record.

     The Create Partial Record API triggers the business rules engine event ApplicationSubmitAfter.

     Note: The Finalize Record API does not include custom forms and custom tables in the request body.
    To add or update custom forms and custom tables, use the [Update Record Custom Forms](./api-
    records.html#operation/v4.put.records.recordId.customForms) and [Update Record Custom Tables](./api-
    records.html#operation/v4.put.records.recordId.customForms) between the Create Partial Record and
    Finalize Record requests.



    **API Endpoint**:  POST /v4/records/{recordId}/finalize

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  Access token

    **Civic Platform version**: 7.3.2


    Args:
        record_id (str):
        fields (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        fields=fields,
        lang=lang,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    """Finalize Record

     Creates the finalized record in the database. Use this method after calling Create Partial Record to
    submit the completed record. See [Creating Records](https://developer.accela.com/docs/construct-api-
    records.html#construct-api-records__creatingRecords) for more information about calling Finalize
    Record in tandem with Create Partial Record.

     The Create Partial Record API triggers the business rules engine event ApplicationSubmitAfter.

     Note: The Finalize Record API does not include custom forms and custom tables in the request body.
    To add or update custom forms and custom tables, use the [Update Record Custom Forms](./api-
    records.html#operation/v4.put.records.recordId.customForms) and [Update Record Custom Tables](./api-
    records.html#operation/v4.put.records.recordId.customForms) between the Create Partial Record and
    Finalize Record requests.



    **API Endpoint**:  POST /v4/records/{recordId}/finalize

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  Access token

    **Civic Platform version**: 7.3.2


    Args:
        record_id (str):
        fields (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        fields=fields,
        lang=lang,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
