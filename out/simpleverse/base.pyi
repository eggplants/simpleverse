from sys import getsizeof as getsizeof
from typing import Union

import requests

class BaseVerseRequests:
    URL: str
    def get_endpoint(self, endpoint: str) -> str: ...
    def __init__(self) -> None: ...
    @staticmethod
    def validate_response(res: requests.Response) -> None: ...
    @staticmethod
    def validate_parameter(
        val: Union[int, str], min: int, max: int, name: str
    ) -> None: ...
