from typing import List, Optional

import requests

from .base import BaseVerseRequests
from .schemas import ImageInfo


class GetImageInfo(BaseVerseRequests):
    def get_image_all(self) -> List[ImageInfo]:
        res = requests.get(url=self.get_endpoint("/image/all"))
        self.validate_response(res)
        return res.json()

    def get_image(self, image_id: str) -> ImageInfo:
        self.validate_parameter(image_id, 36, 36, "image_id")
        res = requests.get(url=self.get_endpoint("/image/" + image_id))
        self.validate_response(res)
        return res.json()

    def get_image_OData(
        self,
        filter_: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[ImageInfo]:
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
        res = requests.get(self.URL + "/image/all", params=params)
        self.validate_response(res)
        return res.json()
