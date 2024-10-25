from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v4_get_records_ids_expand import V4GetRecordsIdsExpand
from ...models.v4_get_records_ids_expand_custom_forms import V4GetRecordsIdsExpandCustomForms
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ids: str,
    *,
    expand: Union[Unset, None, V4GetRecordsIdsExpand] = UNSET,
    expand_custom_forms: Union[Unset, None, V4GetRecordsIdsExpandCustomForms] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_expand: Union[Unset, None, str] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand.value if expand else None

    params["expand"] = json_expand

    json_expand_custom_forms: Union[Unset, None, str] = UNSET
    if not isinstance(expand_custom_forms, Unset):
        json_expand_custom_forms = expand_custom_forms.value if expand_custom_forms else None

    params["expandCustomForms"] = json_expand_custom_forms

    params["fields"] = fields

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v4/records/{ids}".format(
            ids=ids,
        ),
        "params": params,
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
    ids: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expand: Union[Unset, None, V4GetRecordsIdsExpand] = UNSET,
    expand_custom_forms: Union[Unset, None, V4GetRecordsIdsExpandCustomForms] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get Records

     Gets the requested record(s).



    **API Endpoint**:  GET /v4/records/{ids}

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  No authorization required

    **Civic Platform version**: 	7.3.2


    Args:
        ids (str):
        expand (Union[Unset, None, V4GetRecordsIdsExpand]):
        expand_custom_forms (Union[Unset, None, V4GetRecordsIdsExpandCustomForms]):
        fields (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ids=ids,
        expand=expand,
        expand_custom_forms=expand_custom_forms,
        fields=fields,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ids: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expand: Union[Unset, None, V4GetRecordsIdsExpand] = UNSET,
    expand_custom_forms: Union[Unset, None, V4GetRecordsIdsExpandCustomForms] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get Records

     Gets the requested record(s).



    **API Endpoint**:  GET /v4/records/{ids}

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  No authorization required

    **Civic Platform version**: 	7.3.2


    Args:
        ids (str):
        expand (Union[Unset, None, V4GetRecordsIdsExpand]):
        expand_custom_forms (Union[Unset, None, V4GetRecordsIdsExpandCustomForms]):
        fields (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ids=ids,
        expand=expand,
        expand_custom_forms=expand_custom_forms,
        fields=fields,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
