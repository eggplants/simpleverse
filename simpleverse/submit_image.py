from json import dumps
from typing import Optional, cast

import requests

from .base import BaseVerseRequests
from .schemas import ImageRequest


class SubmitImage(BaseVerseRequests):
    def submit_image(self, image_data: str, post_id: str) -> str:
        self.validate_parameter(image_data, 1, 100000, "image_data")
        self.validate_parameter(post_id, 36, 36, "post_id")
        params = cast(ImageRequest, {"base64": image_data, "bind_text_id": post_id})
        res = requests.post(
            url=self.get_endpoint("/image"),
            data=dumps(params),
            headers={"Authorization": "evolution"},
        )
        self.validate_response(res)
        res_id = res.json()["id"]
        # self.__set_own_id(res_id)
        return res_id
