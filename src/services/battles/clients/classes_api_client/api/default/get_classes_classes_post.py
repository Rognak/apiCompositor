from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.classes import Classes
from ...models.classes_filter import ClassesFilter
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ClassesFilter,
) -> Dict[str, Any]:
    url = "{}/classes/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, List[Classes]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Classes.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, List[Classes]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ClassesFilter,
) -> Response[Union[HTTPValidationError, List[Classes]]]:
    """Get Classes

    Args:
        json_body (ClassesFilter):  Example: {'countries': ['USA'], 'type': 'bb'}.

    Returns:
        Response[Union[HTTPValidationError, List[Classes]]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: ClassesFilter,
) -> Optional[Union[HTTPValidationError, List[Classes]]]:
    """Get Classes

    Args:
        json_body (ClassesFilter):  Example: {'countries': ['USA'], 'type': 'bb'}.

    Returns:
        Response[Union[HTTPValidationError, List[Classes]]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ClassesFilter,
) -> Response[Union[HTTPValidationError, List[Classes]]]:
    """Get Classes

    Args:
        json_body (ClassesFilter):  Example: {'countries': ['USA'], 'type': 'bb'}.

    Returns:
        Response[Union[HTTPValidationError, List[Classes]]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ClassesFilter,
) -> Optional[Union[HTTPValidationError, List[Classes]]]:
    """Get Classes

    Args:
        json_body (ClassesFilter):  Example: {'countries': ['USA'], 'type': 'bb'}.

    Returns:
        Response[Union[HTTPValidationError, List[Classes]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
