from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import ImageInfo as ImageInfo
from typing import List

class GetImageInfo(BaseVerseRequests):
    def get_image_all(self) -> List[ImageInfo]: ...
    def get_image(self, image_id: str) -> ImageInfo: ...
