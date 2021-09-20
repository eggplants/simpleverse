from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import LikeInfo as LikeInfo
from typing import List

class GetLikeInfo(BaseVerseRequests):
    def get_like_all(self) -> List[LikeInfo]: ...
    def get_like(self, post_id: str) -> LikeInfo: ...
