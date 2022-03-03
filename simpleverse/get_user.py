from typing import List, Optional, cast

import requests

from .base import BaseVerseRequests
from .schemas import UserInfo


class GetUserInfo(BaseVerseRequests):
    def get_user_all(self) -> List[UserInfo]:
        res = requests.get(url=self.get_endpoint("/user/all"))
        self.validate_response(res)
        res_user = res.json()
        if type(res_user) is list:
            return cast(List[UserInfo], res_user)
        else:
            raise ValueError("response is empty.")

    def get_user(self, user_id: str) -> UserInfo:
        self.validate_parameter(user_id, 40, 40, "user_id")
        res = requests.get(url=self.get_endpoint("/user/" + user_id))
        self.validate_response(res)
        res_user = res.json()
        if type(res_user) is dict:
            return cast(UserInfo, res_user)
        else:
            raise ValueError("response is empty.")

    def get_user_OData(
        self,
        filter_: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> List[UserInfo]:
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
        res = requests.get(self.URL + "/user/all", params=params)
        self.validate_response(res)
        res_user = res.json()
        if type(res_user) is list:
            return cast(List[UserInfo], res_user)
        else:
            raise ValueError("response is empty.")
