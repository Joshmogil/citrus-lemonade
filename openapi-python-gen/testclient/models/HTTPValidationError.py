from typing import *

from pydantic import BaseModel, Field

from .ValidationError import ValidationError


class HTTPValidationError(BaseModel):
    """
    HTTPValidationError model

    """

    detail: Optional[List[ValidationError]] = Field(alias="detail", default=None)
