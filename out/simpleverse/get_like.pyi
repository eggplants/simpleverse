from typing import List, Optional

from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import LikeInfo as LikeInfo

class GetLikeInfo(BaseVerseRequests):
    def get_like_all(self) -> List[LikeInfo]: ...
    def get_like(self, post_id: str) -> LikeInfo: ...
    def get_like_OData(
        self,
        filter_: Optional[str] = ...,
        order_by: Optional[str] = ...,
        limit: Optional[int] = ...,
        skip: Optional[int] = ...,
    ) -> List[LikeInfo]: ...
