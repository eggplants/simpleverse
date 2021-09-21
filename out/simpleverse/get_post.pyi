from typing import List, Optional

from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import PostInfo as PostInfo

class GetPostInfo(BaseVerseRequests):
    def get_post_all(self) -> List[PostInfo]: ...
    def get_post(self, post_id: str) -> PostInfo: ...
    def get_post_OData(
        self,
        filter_: Optional[str] = ...,
        order_by: Optional[str] = ...,
        limit: Optional[int] = ...,
        skip: Optional[int] = ...,
    ) -> List[PostInfo]: ...
