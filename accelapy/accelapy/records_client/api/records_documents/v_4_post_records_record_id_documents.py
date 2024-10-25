from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v4_post_records_record_id_documents_multipart_data import V4PostRecordsRecordIdDocumentsMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    record_id: str,
    *,
    multipart_data: V4PostRecordsRecordIdDocumentsMultipartData,
    group: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    params: Dict[str, Any] = {}
    params["group"] = group

    params["category"] = category

    params["userId"] = user_id

    params["password"] = password

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/v4/records/{recordId}/documents".format(
            recordId=record_id,
        ),
        "files": multipart_multipart_data,
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
    multipart_data: V4PostRecordsRecordIdDocumentsMultipartData,
    group: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    r"""Create Record Documents

     Creates one or more document attachments for the specified record. To specify the documents to be
    attached, use the HTTP header \"Content-Type:multipart/form-data\" and form-data for
    \"uploadedFile\" and \"fileInfo\". Note that the \"fileInfo\" is a string containing an array of
    file attributes. Use \"fileInfo\" to specify one or more documents to be attached. See the example
    for details.



    **API Endpoint**:  POST /v4/records/{recordId}/documents

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  Access token

    **Civic Platform version**: 7.3.2


    Args:
        record_id (str):
        group (Union[Unset, None, str]):
        category (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):
        authorization (str):
        multipart_data (V4PostRecordsRecordIdDocumentsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        multipart_data=multipart_data,
        group=group,
        category=category,
        user_id=user_id,
        password=password,
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
    multipart_data: V4PostRecordsRecordIdDocumentsMultipartData,
    group: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
    lang: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    r"""Create Record Documents

     Creates one or more document attachments for the specified record. To specify the documents to be
    attached, use the HTTP header \"Content-Type:multipart/form-data\" and form-data for
    \"uploadedFile\" and \"fileInfo\". Note that the \"fileInfo\" is a string containing an array of
    file attributes. Use \"fileInfo\" to specify one or more documents to be attached. See the example
    for details.



    **API Endpoint**:  POST /v4/records/{recordId}/documents

    **Scope**:  records

    **App Type**:  All

    **Authorization Type**:  Access token

    **Civic Platform version**: 7.3.2


    Args:
        record_id (str):
        group (Union[Unset, None, str]):
        category (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):
        authorization (str):
        multipart_data (V4PostRecordsRecordIdDocumentsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        multipart_data=multipart_data,
        group=group,
        category=category,
        user_id=user_id,
        password=password,
        lang=lang,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
