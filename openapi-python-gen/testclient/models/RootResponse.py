from typing import *

from pydantic import BaseModel, Field


class RootResponse(BaseModel):
    """
    RootResponse model

    """

    message: str = Field(alias="message")
