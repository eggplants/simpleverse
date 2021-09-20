from typing import Optional, TypedDict


class CreateUserRequest(TypedDict):
    name: str
    description: str


class UserInfo(TypedDict):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    _user_id: Optional[str]
    _created_at: Optional[str]
    _updated_at: Optional[str]


class PostRequest(TypedDict):
    text: str
    in_reply_to_user_id: Optional[str]
    in_reply_to_text_id: Optional[str]


class LikeRequest(TypedDict):
    text: str
    like_count: int


class PostInfo(TypedDict):
    id: Optional[str]
    text: Optional[str]
    in_reply_to_user_id: Optional[str]
    in_reply_to_text_id: Optional[str]
    _user_id: Optional[str]
    _created_at: Optional[str]
    _updated_at: Optional[str]


class LikeInfo(TypedDict):
    id: str
    _updated_at: str
    like_count: int


class ImageInfo(TypedDict):
    id: str
    _created_at: str
    _updated_at: str
    _user_id: str
    base64: str
    bind_text_id: str


class ImageRequest(TypedDict):
    base64: str
    bind_text_id: str
