from typing import List, Optional

from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import UserInfo as UserInfo

class GetUserInfo(BaseVerseRequests):
    def get_user_all(self) -> List[UserInfo]: ...
    def get_user(self, user_id: str) -> UserInfo: ...
    def get_user_OData(
        self,
        filter_: Optional[str] = ...,
        order_by: Optional[str] = ...,
        limit: Optional[int] = ...,
        skip: Optional[int] = ...,
    ) -> List[UserInfo]: ...
