from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import LikeRequest as LikeRequest

class CreateLike(BaseVerseRequests):
    def create_like(self, post_id: str, like_count: int) -> str: ...
