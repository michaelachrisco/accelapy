from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, None, str] = UNSET,
    opened_date_from: Union[Unset, None, str] = UNSET,
    opened_date_to: Union[Unset, None, str] = UNSET,
    custom_id: Union[Unset, None, str] = UNSET,
    module: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    assigned_to_department: Union[Unset, None, str] = UNSET,
    assigned_user: Union[Unset, None, str] = UNSET,
    assigned_date_from: Union[Unset, None, str] = UNSET,
    assigned_date_to: Union[Unset, None, str] = UNSET,
    completed_date_from: Union[Unset, None, str] = UNSET,
    completed_date_to: Union[Unset, None, str] = UNSET,
    status_date_from: Union[Unset, None, str] = UNSET,
    status_date_to: Union[Unset, None, str] = UNSET,
    completed_by_department: Union[Unset, None, str] = UNSET,
    completed_by_user: Union[Unset, None, str] = UNSET,
    closed_date_from: Union[Unset, None, str] = UNSET,
    closed_date_to: Union[Unset, None, str] = UNSET,
    closed_by_department: Union[Unset, None, str] = UNSET,
    closed_by_user: Union[Unset, None, str] = UNSET,
    record_class: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["type"] = type

    params["openedDateFrom"] = opened_date_from

    params["openedDateTo"] = opened_date_to

    params["customId"] = custom_id

    params["module"] = module

    params["status"] = status

    params["assignedToDepartment"] = assigned_to_department

    params["assignedUser"] = assigned_user

    params["assignedDateFrom"] = assigned_date_from

    params["assignedDateTo"] = assigned_date_to

    params["completedDateFrom"] = completed_date_from

    params["completedDateTo"] = completed_date_to

    params["statusDateFrom"] = status_date_from

    params["statusDateTo"] = status_date_to

    params["completedByDepartment"] = completed_by_department

    params["completedByUser"] = completed_by_user

    params["closedDateFrom"] = closed_date_from

    params["closedDateTo"] = closed_date_to

    params["closedByDepartment"] = closed_by_department

    params["closedByUser"] = closed_by_user

    params["recordClass"] = record_class

    params["limit"] = limit

    params["offset"] = offset

    params["fields"] = fields

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v4/records",
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
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, str] = UNSET,
    opened_date_from: Union[Unset, None, str] = UNSET,
    opened_date_to: Union[Unset, None, str] = UNSET,
    custom_id: Union[Unset, None, str] = UNSET,
    module: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    assigned_to_department: Union[Unset, None, str] = UNSET,
    assigned_user: Union[Unset, None, str] = UNSET,
    assigned_date_from: Union[Unset, None, str] = UNSET,
    assigned_date_to: Union[Unset, None, str] = UNSET,
    completed_date_from: Union[Unset, None, str] = UNSET,
    completed_date_to: Union[Unset, None, str] = UNSET,
    status_date_from: Union[Unset, None, str] = UNSET,
    status_date_to: Union[Unset, None, str] = UNSET,
    completed_by_department: Union[Unset, None, str] = UNSET,
    completed_by_user: Union[Unset, None, str] = UNSET,
    closed_date_from: Union[Unset, None, str] = UNSET,
    closed_date_to: Union[Unset, None, str] = UNSET,
    closed_by_department: Union[Unset, None, str] = UNSET,
    closed_by_user: Union[Unset, None, str] = UNSET,
    record_class: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get All Records

     Gets record information, based on the specified query parameters.



    **API Endpoint**:  GET /v4/records

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  	No authorization required

    **Civic Platform version**: 7.3.2


    Args:
        type (Union[Unset, None, str]):
        opened_date_from (Union[Unset, None, str]):
        opened_date_to (Union[Unset, None, str]):
        custom_id (Union[Unset, None, str]):
        module (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        assigned_to_department (Union[Unset, None, str]):
        assigned_user (Union[Unset, None, str]):
        assigned_date_from (Union[Unset, None, str]):
        assigned_date_to (Union[Unset, None, str]):
        completed_date_from (Union[Unset, None, str]):
        completed_date_to (Union[Unset, None, str]):
        status_date_from (Union[Unset, None, str]):
        status_date_to (Union[Unset, None, str]):
        completed_by_department (Union[Unset, None, str]):
        completed_by_user (Union[Unset, None, str]):
        closed_date_from (Union[Unset, None, str]):
        closed_date_to (Union[Unset, None, str]):
        closed_by_department (Union[Unset, None, str]):
        closed_by_user (Union[Unset, None, str]):
        record_class (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        fields (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type=type,
        opened_date_from=opened_date_from,
        opened_date_to=opened_date_to,
        custom_id=custom_id,
        module=module,
        status=status,
        assigned_to_department=assigned_to_department,
        assigned_user=assigned_user,
        assigned_date_from=assigned_date_from,
        assigned_date_to=assigned_date_to,
        completed_date_from=completed_date_from,
        completed_date_to=completed_date_to,
        status_date_from=status_date_from,
        status_date_to=status_date_to,
        completed_by_department=completed_by_department,
        completed_by_user=completed_by_user,
        closed_date_from=closed_date_from,
        closed_date_to=closed_date_to,
        closed_by_department=closed_by_department,
        closed_by_user=closed_by_user,
        record_class=record_class,
        limit=limit,
        offset=offset,
        fields=fields,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, str] = UNSET,
    opened_date_from: Union[Unset, None, str] = UNSET,
    opened_date_to: Union[Unset, None, str] = UNSET,
    custom_id: Union[Unset, None, str] = UNSET,
    module: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    assigned_to_department: Union[Unset, None, str] = UNSET,
    assigned_user: Union[Unset, None, str] = UNSET,
    assigned_date_from: Union[Unset, None, str] = UNSET,
    assigned_date_to: Union[Unset, None, str] = UNSET,
    completed_date_from: Union[Unset, None, str] = UNSET,
    completed_date_to: Union[Unset, None, str] = UNSET,
    status_date_from: Union[Unset, None, str] = UNSET,
    status_date_to: Union[Unset, None, str] = UNSET,
    completed_by_department: Union[Unset, None, str] = UNSET,
    completed_by_user: Union[Unset, None, str] = UNSET,
    closed_date_from: Union[Unset, None, str] = UNSET,
    closed_date_to: Union[Unset, None, str] = UNSET,
    closed_by_department: Union[Unset, None, str] = UNSET,
    closed_by_user: Union[Unset, None, str] = UNSET,
    record_class: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get All Records

     Gets record information, based on the specified query parameters.



    **API Endpoint**:  GET /v4/records

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  	No authorization required

    **Civic Platform version**: 7.3.2


    Args:
        type (Union[Unset, None, str]):
        opened_date_from (Union[Unset, None, str]):
        opened_date_to (Union[Unset, None, str]):
        custom_id (Union[Unset, None, str]):
        module (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        assigned_to_department (Union[Unset, None, str]):
        assigned_user (Union[Unset, None, str]):
        assigned_date_from (Union[Unset, None, str]):
        assigned_date_to (Union[Unset, None, str]):
        completed_date_from (Union[Unset, None, str]):
        completed_date_to (Union[Unset, None, str]):
        status_date_from (Union[Unset, None, str]):
        status_date_to (Union[Unset, None, str]):
        completed_by_department (Union[Unset, None, str]):
        completed_by_user (Union[Unset, None, str]):
        closed_date_from (Union[Unset, None, str]):
        closed_date_to (Union[Unset, None, str]):
        closed_by_department (Union[Unset, None, str]):
        closed_by_user (Union[Unset, None, str]):
        record_class (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        fields (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type=type,
        opened_date_from=opened_date_from,
        opened_date_to=opened_date_to,
        custom_id=custom_id,
        module=module,
        status=status,
        assigned_to_department=assigned_to_department,
        assigned_user=assigned_user,
        assigned_date_from=assigned_date_from,
        assigned_date_to=assigned_date_to,
        completed_date_from=completed_date_from,
        completed_date_to=completed_date_to,
        status_date_from=status_date_from,
        status_date_to=status_date_to,
        completed_by_department=completed_by_department,
        completed_by_user=completed_by_user,
        closed_date_from=closed_date_from,
        closed_date_to=closed_date_to,
        closed_by_department=closed_by_department,
        closed_by_user=closed_by_user,
        record_class=record_class,
        limit=limit,
        offset=offset,
        fields=fields,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
