from json import dumps
from typing import cast

import requests

from .base import BaseVerseRequests
from .schemas import LikeRequest


class CreateLike(BaseVerseRequests):
    def create_like(self, post_id: str, like_count: int) -> str:
        self.validate_parameter(post_id, 36, 36, "post_id")
        self.validate_parameter(like_count, 0, 1000, "like_count")
        params = cast(LikeRequest, {"like_count": like_count})
        res = requests.put(
            self.get_endpoint("/like/" + post_id),
            data=dumps(params),
            headers={
                "Authorization": "LOVE",
            },
        )
        self.validate_response(res)
        res_id: str = res.json()["id"]
        # self.__set_own_id(res_id)
        return res_id
