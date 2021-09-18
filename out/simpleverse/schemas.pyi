from typing import Optional, TypedDict

class CreateUserRequest(TypedDict):
    name: str
    description: str

class UserInfo(TypedDict):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]

class PostRequest(TypedDict):
    text: str
    in_reply_to_user_id: Optional[str]
    in_reply_to_text_id: Optional[str]

class PostInfo(TypedDict):
    id: Optional[str]
    text: Optional[str]
    in_reply_to_user_id: Optional[str]
    in_reply_to_text_id: Optional[str]
