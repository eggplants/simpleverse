from typing import List, Optional

import requests

from .base import BaseVerseRequests
from .schemas import PostInfo


class GetPostInfo(BaseVerseRequests):
    def get_post_all(self) -> List[PostInfo]:
        res = requests.get(url=self.get_endpoint("/text/all"))
        self.validate_response(res)
        return res.json()

    def get_post(self, post_id: str) -> PostInfo:
        self.validate_parameter(post_id, 36, 36, "post_id")
        res = requests.get(url=self.get_endpoint("/text/" + post_id))
        self.validate_response(res)
        return res.json()

    def get_post_OData(
        self,
        filter_: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[PostInfo]:
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
        res = requests.get(self.URL + "/text/all", params=params)
        self.validate_response(res)
        return res.json()
