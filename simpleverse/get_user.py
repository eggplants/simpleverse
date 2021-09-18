from typing import List

import requests

from .base import BaseVerseRequests
from .schemas import UserInfo


class GetUserInfo(BaseVerseRequests):
    def get_user_all(self) -> List[UserInfo]:
        res = requests.get(
            url=self.get_endpoint("/user/all")
        )
        self.validate_response(res)
        return res.json()

    def get_user(self, id_: str) -> UserInfo:
        res = requests.get(
            url=self.get_endpoint("/user/" + id_)
        )
        self.validate_response(res)
        return res.json()
