from typing import *

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User model

    """

    id: int = Field(alias="id")

    username: str = Field(alias="username")

    email: str = Field(alias="email")

    password: str = Field(alias="password")

    is_active: Optional[bool] = Field(alias="is_active", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)
