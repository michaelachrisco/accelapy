from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v4_get_records_record_id_payments_payment_status import V4GetRecordsRecordIdPaymentsPaymentStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    record_id: str,
    *,
    payment_status: Union[Unset, None, V4GetRecordsRecordIdPaymentsPaymentStatus] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    params: Dict[str, Any] = {}
    json_payment_status: Union[Unset, None, str] = UNSET
    if not isinstance(payment_status, Unset):
        json_payment_status = payment_status.value if payment_status else None

    params["paymentStatus"] = json_payment_status

    params["fields"] = fields

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v4/records/{recordId}/payments".format(
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
    payment_status: Union[Unset, None, V4GetRecordsRecordIdPaymentsPaymentStatus] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    """Get All Payments for Record

     Gets information about the payments for the specified record.



    **API Endpoint**:  GET /v4/records/{recordId}/payments

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  Access token

    **Civic Platform version**: 9.0.0


    Args:
        record_id (str):
        payment_status (Union[Unset, None, V4GetRecordsRecordIdPaymentsPaymentStatus]):
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
        payment_status=payment_status,
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
    payment_status: Union[Unset, None, V4GetRecordsRecordIdPaymentsPaymentStatus] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    """Get All Payments for Record

     Gets information about the payments for the specified record.



    **API Endpoint**:  GET /v4/records/{recordId}/payments

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  Access token

    **Civic Platform version**: 9.0.0


    Args:
        record_id (str):
        payment_status (Union[Unset, None, V4GetRecordsRecordIdPaymentsPaymentStatus]):
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
        payment_status=payment_status,
        fields=fields,
        lang=lang,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
