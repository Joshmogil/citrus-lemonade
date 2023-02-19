import os
from typing import Optional, Union


class APIConfig:
    base_path: str = "http://localhost:8080"
    verify: Union[bool, str] = True

    @staticmethod
    def get_access_token() -> Optional[str]:
        try:
            return os.environ["access_token"]
        except KeyError:
            return None

    @staticmethod
    def set_access_token(value: str):
        raise Exception(
            "This client was generated with an environment variable for the access token. Please set the environment variable 'access_token' to the access token."
        )


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code} {message}")

    def __str__(self):
        return f"{self.status_code} {self.message}"
