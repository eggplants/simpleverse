from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import ImageRequest as ImageRequest

class SubmitImage(BaseVerseRequests):
    def submit_image(self, image_data: str, post_id: str) -> str: ...
