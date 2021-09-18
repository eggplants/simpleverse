from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import UserInfo as UserInfo
from typing import List

class GetUserInfo(BaseVerseRequests):
    def get_user_all(self) -> List[UserInfo]: ...
    def get_user(self, id_: str) -> UserInfo: ...
