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
        rep_post_id: Optional[str] = None,
        test: bool = False,
    ) -> str:
        self.validate_parameter(text, 1, 280, "text")
        params = cast(
            PostRequest,
            {
                "text": text,
            },
        )
        if rep_user_id is not None:
            self.validate_parameter(rep_user_id, 40, 40, "rep_user_id")
            params["in_reply_to_user_id"] = rep_user_id
        if rep_post_id is not None:
            self.validate_parameter(rep_post_id, 36, 36, "rep_post_id")
            params["in_reply_to_text_id"] = rep_post_id
        res = requests.post(
            url=self.get_endpoint("/text_test" if test else "/text"),
            data=dumps(params),
            headers={"Authorization": "HelloWorld"},
        )
        self.validate_response(res)
        res_id = res.json()
        # self.__set_own_id(res_id)
        if "id" in res_id:
            return str(res_id["id"])
        else:
            raise ValueError("'id' is missing in response.")
