from json import dumps

import requests

from .base import BaseVerseRequests


class CreateUser(BaseVerseRequests):
    def create_user(self, name: str, description: str) -> str:
        if len(name) > 300 or len(description) > 300:
            raise ValueError(
                f"name = {len(name)}, "
                f"description = {len(description)}"
            )
        res = requests.post(
            url=self.get_endpoint("/user/create_user"),
            data=dumps({
                "name": name,
                "description": description
            })
        )
        self.validate_response(res)
        res_id = res.json()["id"]
        # self.__set_own_id(res_id)
        return res_id

    def update_user(self, name: str, description: str) -> str:
        if len(name) > 300 or len(description) > 300:
            raise ValueError(
                f"name = {len(name)}, "
                f"description = {len(description)}"
            )
        res = requests.put(
            url=self.get_endpoint("/user/create_user"),
            data=dumps({
                "name": name,
                "description": description
            })
        )
        self.validate_response(res)
        res_id = res.json()["id"]
        # self.__set_own_id(res_id)
        return res_id
