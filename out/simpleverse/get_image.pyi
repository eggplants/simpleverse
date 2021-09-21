from typing import List, Optional

from .base import BaseVerseRequests as BaseVerseRequests
from .schemas import ImageInfo as ImageInfo

class GetImageInfo(BaseVerseRequests):
    def get_image_all(self) -> List[ImageInfo]: ...
    def get_image(self, image_id: str) -> ImageInfo: ...
    def get_image_OData(
        self,
        filter_: Optional[str] = ...,
        order_by: Optional[str] = ...,
        limit: Optional[int] = ...,
        skip: Optional[int] = ...,
    ) -> List[ImageInfo]: ...
