from typing import List, Optional

import requests

from .base import BaseVerseRequests
from .schemas import PostInfo


class GetPostInfo(BaseVerseRequests):
    def get_post_all(self) -> List[PostInfo]:
        res = requests.get(
            url=self.get_endpoint("/text/all")
        )
        self.validate_response(res)
        return res.json()

    def get_post(self, id_: str) -> PostInfo:
        res = requests.get(
            url=self.get_endpoint("/text/" + id_)
        )
        self.validate_response(res)
        return res.json()

    def get_post_OData(
        self,
        filter_: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[str] = None,
        skip: Optional[str] = None
    ) -> List[PostInfo]:
        params = {}
        if filter_ is not None:
            params["$filter"] = filter_
        if order_by is not None:
            params["$order_by"] = order_by
        if limit is not None:
            params["$limit"] = limit
        if skip is not None:
            params["$skip"] = skip
        res = requests.get(
            self.URL + '/text/all',
            params=params
        )
        self.validate_response(res)
        return res.json()
