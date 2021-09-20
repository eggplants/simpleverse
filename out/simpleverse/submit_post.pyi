from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import PostRequest as PostRequest
from typing import Optional

class SubmitPost(BaseVerseRequests):
    def submit_post(self, text: str, rep_user_id: Optional[str] = ..., rep_post_id: Optional[str] = ...) -> str: ...
