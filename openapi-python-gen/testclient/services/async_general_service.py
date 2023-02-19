import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def root__get() -> RootResponse:
    base_path = APIConfig.base_path
    path = f"/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return RootResponse(**response.json()) if response.json() is not None else RootResponse()


async def get_users_users_get() -> List[User]:
    base_path = APIConfig.base_path
    path = f"/users"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return [User(**item) for item in response.json()]


async def create_user_users_post(
    data: User,
) -> User:
    base_path = APIConfig.base_path
    path = f"/users"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "post", httpx.URL(path), headers=headers, params=query_params, json=json.dumps(data.dict())
        )

    if response.status_code != 201:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return User(**response.json()) if response.json() is not None else User()


async def get_user_users__user_id__get(
    user_id: int,
) -> User:
    base_path = APIConfig.base_path
    path = f"/users/{user_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return User(**response.json()) if response.json() is not None else User()


async def delete_user_users__user_id__delete(
    user_id: int,
) -> None:
    base_path = APIConfig.base_path
    path = f"/users/{user_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 204:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return response.json()


async def update_user_users__user_id__patch(
    user_id: int,
    data: User,
) -> User:
    base_path = APIConfig.base_path
    path = f"/users/{user_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "patch", httpx.URL(path), headers=headers, params=query_params, json=json.dumps(data.dict())
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return User(**response.json()) if response.json() is not None else User()


async def get_teams_teams_get() -> List[Team]:
    base_path = APIConfig.base_path
    path = f"/teams"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return [Team(**item) for item in response.json()]


async def create_team_teams_post(
    data: Team,
) -> Team:
    base_path = APIConfig.base_path
    path = f"/teams"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "post", httpx.URL(path), headers=headers, params=query_params, json=json.dumps(data.dict())
        )

    if response.status_code != 201:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return Team(**response.json()) if response.json() is not None else Team()


async def get_team_teams__team_id__get(
    team_id: int,
) -> Team:
    base_path = APIConfig.base_path
    path = f"/teams/{team_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return Team(**response.json()) if response.json() is not None else Team()


async def delete_team_teams__team_id__delete(
    team_id: int,
) -> None:
    base_path = APIConfig.base_path
    path = f"/teams/{team_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 204:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return response.json()


async def update_team_teams__team_id__patch(
    team_id: int,
    data: Team,
) -> Team:
    base_path = APIConfig.base_path
    path = f"/teams/{team_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { APIConfig.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=APIConfig.verify) as client:
        response = await client.request(
            "patch", httpx.URL(path), headers=headers, params=query_params, json=json.dumps(data.dict())
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")
    return Team(**response.json()) if response.json() is not None else Team()
