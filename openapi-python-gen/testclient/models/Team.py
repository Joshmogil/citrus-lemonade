from typing import *

from pydantic import BaseModel, Field

from .User import User


class Team(BaseModel):
    """
    Team model

    """

    id: int = Field(alias="id")

    name: str = Field(alias="name")

    description: str = Field(alias="description")

    is_active: Optional[bool] = Field(alias="is_active", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    users: Optional[List[User]] = Field(alias="users", default=None)

    captain: Optional[User] = Field(alias="captain", default=None)
