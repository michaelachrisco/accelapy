from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v4_get_records_mine_expand import V4GetRecordsMineExpand
from ...models.v4_get_records_mine_expand_custom_forms import V4GetRecordsMineExpandCustomForms
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, None, str] = UNSET,
    opened_date_from: Union[Unset, None, str] = UNSET,
    opened_date_to: Union[Unset, None, str] = UNSET,
    custom_id: Union[Unset, None, str] = UNSET,
    module: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    assigned_date_from: Union[Unset, None, str] = UNSET,
    assigned_date_to: Union[Unset, None, str] = UNSET,
    completed_date_from: Union[Unset, None, str] = UNSET,
    completed_date_to: Union[Unset, None, str] = UNSET,
    status_date_from: Union[Unset, None, str] = UNSET,
    status_date_to: Union[Unset, None, str] = UNSET,
    update_date_from: Union[Unset, None, str] = UNSET,
    update_date_to: Union[Unset, None, str] = UNSET,
    completed_by_department: Union[Unset, None, str] = UNSET,
    completed_by_user: Union[Unset, None, str] = UNSET,
    closed_date_from: Union[Unset, None, str] = UNSET,
    closed_date_to: Union[Unset, None, str] = UNSET,
    closed_by_department: Union[Unset, None, str] = UNSET,
    closed_by_user: Union[Unset, None, str] = UNSET,
    record_class: Union[Unset, None, str] = UNSET,
    types: Union[Unset, None, str] = UNSET,
    modules: Union[Unset, None, str] = UNSET,
    status_types: Union[Unset, None, str] = UNSET,
    expand: Union[Unset, None, V4GetRecordsMineExpand] = UNSET,
    expand_custom_forms: Union[Unset, None, V4GetRecordsMineExpandCustomForms] = UNSET,
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

    params["assignedDateFrom"] = assigned_date_from

    params["assignedDateTo"] = assigned_date_to

    params["completedDateFrom"] = completed_date_from

    params["completedDateTo"] = completed_date_to

    params["statusDateFrom"] = status_date_from

    params["statusDateTo"] = status_date_to

    params["updateDateFrom"] = update_date_from

    params["updateDateTo"] = update_date_to

    params["completedByDepartment"] = completed_by_department

    params["completedByUser"] = completed_by_user

    params["closedDateFrom"] = closed_date_from

    params["closedDateTo"] = closed_date_to

    params["closedByDepartment"] = closed_by_department

    params["closedByUser"] = closed_by_user

    params["recordClass"] = record_class

    params["types"] = types

    params["modules"] = modules

    params["statusTypes"] = status_types

    json_expand: Union[Unset, None, str] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand.value if expand else None

    params["expand"] = json_expand

    json_expand_custom_forms: Union[Unset, None, str] = UNSET
    if not isinstance(expand_custom_forms, Unset):
        json_expand_custom_forms = expand_custom_forms.value if expand_custom_forms else None

    params["expandCustomForms"] = json_expand_custom_forms

    params["limit"] = limit

    params["offset"] = offset

    params["fields"] = fields

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v4/records/mine",
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
    assigned_date_from: Union[Unset, None, str] = UNSET,
    assigned_date_to: Union[Unset, None, str] = UNSET,
    completed_date_from: Union[Unset, None, str] = UNSET,
    completed_date_to: Union[Unset, None, str] = UNSET,
    status_date_from: Union[Unset, None, str] = UNSET,
    status_date_to: Union[Unset, None, str] = UNSET,
    update_date_from: Union[Unset, None, str] = UNSET,
    update_date_to: Union[Unset, None, str] = UNSET,
    completed_by_department: Union[Unset, None, str] = UNSET,
    completed_by_user: Union[Unset, None, str] = UNSET,
    closed_date_from: Union[Unset, None, str] = UNSET,
    closed_date_to: Union[Unset, None, str] = UNSET,
    closed_by_department: Union[Unset, None, str] = UNSET,
    closed_by_user: Union[Unset, None, str] = UNSET,
    record_class: Union[Unset, None, str] = UNSET,
    types: Union[Unset, None, str] = UNSET,
    modules: Union[Unset, None, str] = UNSET,
    status_types: Union[Unset, None, str] = UNSET,
    expand: Union[Unset, None, V4GetRecordsMineExpand] = UNSET,
    expand_custom_forms: Union[Unset, None, V4GetRecordsMineExpandCustomForms] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get My Records

     Gets records for the currently logged-in user.



    **API Endpoint**:  GET /v4/records/mine

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  No authorization required

    **Civic Platform version**: 7.3.2


    Args:
        type (Union[Unset, None, str]):
        opened_date_from (Union[Unset, None, str]):
        opened_date_to (Union[Unset, None, str]):
        custom_id (Union[Unset, None, str]):
        module (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        assigned_date_from (Union[Unset, None, str]):
        assigned_date_to (Union[Unset, None, str]):
        completed_date_from (Union[Unset, None, str]):
        completed_date_to (Union[Unset, None, str]):
        status_date_from (Union[Unset, None, str]):
        status_date_to (Union[Unset, None, str]):
        update_date_from (Union[Unset, None, str]):
        update_date_to (Union[Unset, None, str]):
        completed_by_department (Union[Unset, None, str]):
        completed_by_user (Union[Unset, None, str]):
        closed_date_from (Union[Unset, None, str]):
        closed_date_to (Union[Unset, None, str]):
        closed_by_department (Union[Unset, None, str]):
        closed_by_user (Union[Unset, None, str]):
        record_class (Union[Unset, None, str]):
        types (Union[Unset, None, str]):
        modules (Union[Unset, None, str]):
        status_types (Union[Unset, None, str]):
        expand (Union[Unset, None, V4GetRecordsMineExpand]):
        expand_custom_forms (Union[Unset, None, V4GetRecordsMineExpandCustomForms]):
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
        assigned_date_from=assigned_date_from,
        assigned_date_to=assigned_date_to,
        completed_date_from=completed_date_from,
        completed_date_to=completed_date_to,
        status_date_from=status_date_from,
        status_date_to=status_date_to,
        update_date_from=update_date_from,
        update_date_to=update_date_to,
        completed_by_department=completed_by_department,
        completed_by_user=completed_by_user,
        closed_date_from=closed_date_from,
        closed_date_to=closed_date_to,
        closed_by_department=closed_by_department,
        closed_by_user=closed_by_user,
        record_class=record_class,
        types=types,
        modules=modules,
        status_types=status_types,
        expand=expand,
        expand_custom_forms=expand_custom_forms,
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
    assigned_date_from: Union[Unset, None, str] = UNSET,
    assigned_date_to: Union[Unset, None, str] = UNSET,
    completed_date_from: Union[Unset, None, str] = UNSET,
    completed_date_to: Union[Unset, None, str] = UNSET,
    status_date_from: Union[Unset, None, str] = UNSET,
    status_date_to: Union[Unset, None, str] = UNSET,
    update_date_from: Union[Unset, None, str] = UNSET,
    update_date_to: Union[Unset, None, str] = UNSET,
    completed_by_department: Union[Unset, None, str] = UNSET,
    completed_by_user: Union[Unset, None, str] = UNSET,
    closed_date_from: Union[Unset, None, str] = UNSET,
    closed_date_to: Union[Unset, None, str] = UNSET,
    closed_by_department: Union[Unset, None, str] = UNSET,
    closed_by_user: Union[Unset, None, str] = UNSET,
    record_class: Union[Unset, None, str] = UNSET,
    types: Union[Unset, None, str] = UNSET,
    modules: Union[Unset, None, str] = UNSET,
    status_types: Union[Unset, None, str] = UNSET,
    expand: Union[Unset, None, V4GetRecordsMineExpand] = UNSET,
    expand_custom_forms: Union[Unset, None, V4GetRecordsMineExpandCustomForms] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get My Records

     Gets records for the currently logged-in user.



    **API Endpoint**:  GET /v4/records/mine

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  No authorization required

    **Civic Platform version**: 7.3.2


    Args:
        type (Union[Unset, None, str]):
        opened_date_from (Union[Unset, None, str]):
        opened_date_to (Union[Unset, None, str]):
        custom_id (Union[Unset, None, str]):
        module (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        assigned_date_from (Union[Unset, None, str]):
        assigned_date_to (Union[Unset, None, str]):
        completed_date_from (Union[Unset, None, str]):
        completed_date_to (Union[Unset, None, str]):
        status_date_from (Union[Unset, None, str]):
        status_date_to (Union[Unset, None, str]):
        update_date_from (Union[Unset, None, str]):
        update_date_to (Union[Unset, None, str]):
        completed_by_department (Union[Unset, None, str]):
        completed_by_user (Union[Unset, None, str]):
        closed_date_from (Union[Unset, None, str]):
        closed_date_to (Union[Unset, None, str]):
        closed_by_department (Union[Unset, None, str]):
        closed_by_user (Union[Unset, None, str]):
        record_class (Union[Unset, None, str]):
        types (Union[Unset, None, str]):
        modules (Union[Unset, None, str]):
        status_types (Union[Unset, None, str]):
        expand (Union[Unset, None, V4GetRecordsMineExpand]):
        expand_custom_forms (Union[Unset, None, V4GetRecordsMineExpandCustomForms]):
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
        assigned_date_from=assigned_date_from,
        assigned_date_to=assigned_date_to,
        completed_date_from=completed_date_from,
        completed_date_to=completed_date_to,
        status_date_from=status_date_from,
        status_date_to=status_date_to,
        update_date_from=update_date_from,
        update_date_to=update_date_to,
        completed_by_department=completed_by_department,
        completed_by_user=completed_by_user,
        closed_date_from=closed_date_from,
        closed_date_to=closed_date_to,
        closed_by_department=closed_by_department,
        closed_by_user=closed_by_user,
        record_class=record_class,
        types=types,
        modules=modules,
        status_types=status_types,
        expand=expand,
        expand_custom_forms=expand_custom_forms,
        limit=limit,
        offset=offset,
        fields=fields,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
