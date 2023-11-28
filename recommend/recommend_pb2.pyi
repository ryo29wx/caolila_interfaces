from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecommnedRequest(_message.Message):
    __slots__ = ["user_id", "page", "listsize", "token"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LISTSIZE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    page: int
    listsize: int
    token: str
    def __init__(self, user_id: _Optional[str] = ..., page: _Optional[int] = ..., listsize: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class RecommendResponseList(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _containers.RepeatedCompositeFieldContainer[RecommendResponse]
    def __init__(self, response: _Optional[_Iterable[_Union[RecommendResponse, _Mapping]]] = ...) -> None: ...

class RecommendResponse(_message.Message):
    __slots__ = ["user_id", "nick_name", "sex", "title", "company", "like", "image_url", "last_login"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    nick_name: str
    sex: int
    title: str
    company: str
    like: bool
    image_url: str
    last_login: str
    def __init__(self, user_id: _Optional[str] = ..., nick_name: _Optional[str] = ..., sex: _Optional[int] = ..., title: _Optional[str] = ..., company: _Optional[str] = ..., like: bool = ..., image_url: _Optional[str] = ..., last_login: _Optional[str] = ...) -> None: ...
