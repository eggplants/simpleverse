from typing import List, Optional

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

    def get_like_OData(
        self,
        filter_: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[LikeInfo]:
        params = {}
        if filter_ is not None:
            params["$filter"] = filter_
        if order_by is not None:
            params["$order_by"] = order_by
        if limit is not None:
            assert limit > 0, "limit should be positive int"
            params["$limit"] = str(limit)
        if skip is not None:
            assert skip > 0, "skip should be positive int"
            params["$skip"] = str(skip)
        res = requests.get(self.URL + "/like/all", params=params)
        self.validate_response(res)
        return res.json()
