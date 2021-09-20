from typing import List

import requests

from .base import BaseVerseRequests
from .schemas import LikeInfo


class GetLikeInfo(BaseVerseRequests):
    def get_like_all(self) -> List[LikeInfo]:
        res = requests.get(url=self.get_endpoint("/like/all"))
        self.validate_response(res)
        return res.json()

    def get_like(self, post_id: str) -> LikeInfo:
        self.validate_parameter(post_id, 36, 36, "text_id")
        res = requests.get(url=self.get_endpoint("/like/" + post_id))
        self.validate_response(res)
        return res.json()
