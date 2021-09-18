from json import dumps
from typing import Optional, cast

import requests

from .base import BaseVerseRequests
from .schemas import PostRequest


class SubmitPost(BaseVerseRequests):
    def submit_post(
        self,
        text: str,
        rep_user_id: Optional[str] = None,
        rep_post_id: Optional[str] = None
    ) -> str:
        if not(281 > len(text) > 0):
            raise ValueError(
                f"text = {len(text)}"
            )
        params = cast(
            PostRequest,
            {
                "text": text,
            }
        )
        if rep_user_id is not None:
            params['in_reply_to_user_id'] = rep_user_id
        if rep_post_id is not None:
            params['in_reply_to_text_id'] = rep_post_id
        res = requests.post(
            url=self.get_endpoint("/text"),
            data=dumps(params),
            headers={"Authorization": "HelloWorld"}
        )
        self.validate_response(res)
        res_id = res.json()["id"]
        # self.__set_own_id(res_id)
        return res_id
