from typing import List

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
