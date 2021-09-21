# simpleverse

[![PyPI](https://img.shields.io/pypi/v/simpleverse?color=blue)](https://pypi.org/project/simpleverse) [![Maintainability](https://api.codeclimate.com/v1/badges/3dafcba23209bf5a4a04/maintainability)](https://codeclimate.com/github/eggplants/simpleverse/maintainability)

API wrapper for [versatileapi](https://versatileapi.herokuapp.com/api) in Python

## Install

```bash
pip install simpleverse
```

## CLI

<!-- markdownlint-disable MD033 -->

<details>
<summary>Workaround for simpleverse's CLI</summary>

```text
$ simv -h
usage: simv [-h]
            {create_like,cl,create_user,cu,update_user,uu,get_like,gl,get_image,gi,get_post,gp,get_user,gu,submit_post,sp,submit_image,si,repl,rl}
            ...

Simple command for sending requests to versatileapi

positional arguments:
  {create_like,cl,create_user,cu,update_user,uu,get_like,gl,get_image,gi,get_post,gp,get_user,gu,submit_post,sp,submit_image,si,repl,rl}
    create_like (cl)
    create_user (cu)
    update_user (uu)
    get_like (gl)
    get_image (gi)
    get_post (gp)
    get_user (gu)
    submit_post (sp)
    submit_image (si)
    repl (rl)

optional arguments:
  -h, --help            show this help message and exit
$ simv cu -n eggplants -d "https://github.com/eggplants/simpleverseを書きました。"
b6e4ae19fc2c59ce55c726de44a40dc825faa04d
$ simv gu -u b6e4ae19fc2c59ce55c726de44a40dc825faa04d
{
    'id': 'b6e4ae19fc2c59ce55c726de44a40dc825faa04d',
    '_created_at': '2021-09-19T04:35:11.765+00:00',
    '_updated_at': '2021-09-19T04:35:11.765+00:00',
    '_user_id': 'b6e4ae19fc2c59ce55c726de44a40dc825faa04d',
    'description': 'https://github.com/eggplants/simpleverseを書きました。',
    'name': 'eggplants'
}
$ simv sp "コレはテストです"
00210022-a452-4be7-a873-d369b1bf8d70
$ simv gp -p 00210022-a452-4be7-a873-d369b1bf8d70
{
    'id': '00210022-a452-4be7-a873-d369b1bf8d70',
    '_created_at': '2021-09-19T04:45:42.017+00:00',
    '_updated_at': '2021-09-19T04:45:42.017+00:00',
    '_user_id': 'b6e4ae19fc2c59ce55c726de44a40dc825faa04d',
    'text': 'コレはテストです'
}
$ simv uu -n eggplants -d "こんにちは。https://github.com/eggplants/simpleverseを書きました。"
b6e4ae19fc2c59ce55c726de44a40dc825faa04d
$ simv gu -u b6e4ae19fc2c59ce55c726de44a40dc825faa04d
{
    'id': 'b6e4ae19fc2c59ce55c726de44a40dc825faa04d',
    '_created_at': '2021-09-19T04:35:11.765+00:00',
    '_updated_at': '2021-09-19T04:46:53.659+00:00',
    '_user_id': 'b6e4ae19fc2c59ce55c726de44a40dc825faa04d',
    'description': 'こんにちは。https://github.com/eggplants/simpleverseを書きました。',
    'name': 'eggplants'
}
$ # All posts by a specific user
$ simv gp | jq '.[]|select(._user_id=="b6e4ae19fc2c59ce55c726de44a40dc825faa04d")'
{
  "_created_at": "2021-09-18T18:50:33.316+00:00",
  "_updated_at": "2021-09-18T18:50:33.316+00:00",
  "_user_id": "b6e4ae19fc2c59ce55c726de44a40dc825faa04d",
  "id": "12d7d6c5-1412-4299-9fe0-4e11c5261aab",
  "text": "test"
}
{
  "_created_at": "2021-09-19T04:10:35.054+00:00",
  "_updated_at": "2021-09-19T04:10:35.054+00:00",
  "_user_id": "b6e4ae19fc2c59ce55c726de44a40dc825faa04d",
  "id": "81dd0981-de48-47b6-bb81-2bc33579d0d1",
  "text": "hello woooooooold!"
}
{
  "_created_at": "2021-09-19T04:14:44.837+00:00",
  "_updated_at": "2021-09-19T04:14:44.837+00:00",
  "_user_id": "b6e4ae19fc2c59ce55c726de44a40dc825faa04d",
  "id": "b281751f-03a9-47b0-ace1-2dc1be620a2a",
  "text": "hello woooooooold!\n(this post submitted by https://git.io/JzmhD)"
}
{
  "_created_at": "2021-09-19T04:39:57.808+00:00",
  "_updated_at": "2021-09-19T04:39:57.808+00:00",
  "_user_id": "b6e4ae19fc2c59ce55c726de44a40dc825faa04d",
  "id": "d2f875a4-540e-4332-ae4e-5ac80d435449",
  "text": "a"
}
{
  "_created_at": "2021-09-19T04:45:42.017+00:00",
  "_updated_at": "2021-09-19T04:45:42.017+00:00",
  "_user_id": "b6e4ae19fc2c59ce55c726de44a40dc825faa04d",
  "id": "00210022-a452-4be7-a873-d369b1bf8d70",
  "text": "コレはテストです"
}
```

</details>

<!-- markdownlint-enable MD033 -->

## Library

<!-- markdownlint-disable MD033 -->

<details>
<summary>Classes and its methods of simpleverse</summary>

```python
from simpleverse import (
    CreateLike,
    CreateUser,
    GetImageInfo,
    GetLikeInfo,
    GetPostInfo,
    GetUserInfo,
    SubmitImage,
    SubmitPost,
)


class CreateLike(BaseVerseRequests):
    def create_like(self, post_id: str, like_count: int) -> str: ...

class CreateUser(BaseVerseRequests):
    def create_user(self, name: str, description: str) -> str: ...
    def update_user(self, name: str, description: str) -> str: ...

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

class GetUserInfo(BaseVerseRequests):
    def get_user_all(self) -> List[UserInfo]: ...
    def get_user(self, user_id: str) -> UserInfo: ...
    def get_user_OData(
        self,
        filter_: Optional[str] = ...,
        order_by: Optional[str] = ...,
        limit: Optional[int] = ...,
        skip: Optional[int] = ...,
    ) -> List[UserInfo]: ...

class SubmitImage(BaseVerseRequests):
    def submit_image(self, image_data: str, post_id: str) -> str: ...

class SubmitPost(BaseVerseRequests):
    def submit_post(
        self,
        text: str,
        rep_user_id: Optional[str] = ...,
        rep_post_id: Optional[str] = ...,
        test: bool = ...,
    ) -> str: ...
```

</details>

<!-- markdownlint-enable MD033 -->

## Links

### Docs

- [HawkClaws/versatileapi](https://github.com/HawkClaws/versatileapi)
  - API generator
- [エンジニア・プログラマにしか使えない SNS を作ってみた話](https://qiita.com/HawkClaws/items/599d7666f55e79ef7f56)
  - Author's article
- [Swagger](https://editor.swagger.io/?url=https://gist.githubusercontent.com/YusukeIwaki/ce8a7250fb7e5279267c495324de19f7/raw/292eb24fb381c9af49fc42c901794ec2d98d134a/openapi.yml)
  - Versatileapi's schema in Swagger

### WebUI Clients (deploying somewhare)

- [chamegashi/Engineer_SNS_Test_Site](https://chamegashi.github.io/Engineer_SNS_Test_Site/)
  - Repo: <https://github.com/chamegashi/Engineer_SNS_Test_Site>
- [dala00/engineer-sns-client](http://engineer-sns-client.vercel.app/)
  - Repo: <https://github.com/dala00/engineer-sns-client>
- [hir0o/sns-for-engineer](http://sns-for-engineer.vercel.app/)
  - Repo: <https://github.com/hir0o/sns-for-engineer>
- [lightwill/sns](https://lightwill.tokyo/dev/sns/)
  - Posts of spesific user: `https://lightwill.tokyo/dev/sns/?selectUserId={userid}`
- [nison/json-sns-viewer](https://sns-viewer.nison.jp/)
  - Repo: <https://github.com/nison-okrock/json-sns-viewer>
- [mehm8128/twitter-for-engineer](https://twitter-for-engineer-gs7w7u3rv-mehm8128.vercel.app/)
  - Repo: <https://github.com/mehm8128/twitter-for-engineer>
- [standard-software/programmer-only-sns](https://standard-software.github.io/programmer-only-sns/)
  - Repo: <https://github.com/standard-software/programmer-only-sns>
- [voidproc/engineer-sns-client](https://codesandbox.io/s/engineer-sns-client-l6n6j)
  - Repo: <https://github.com/voidproc/engineer-sns-client>
- [yosket/engineer-sns](https://sofeap.vercel.app/)
  - Repo: <https://github.com/yosket/engineer-sns>
  - Article: [『エンジニア・プログラマにしか使えない SNS を作ってみた話』のクライアントを作ってみた話](https://zenn.dev/yosket/articles/a4402ffa2a12e4)

### CUI Clients

- [daiji-tsutsui/Beelzebub](https://github.com/daiji-tsutsui/Beelzebub)
  - Ruby
- [elderica/esns](https://github.com/elderica/esns)
  - Racket
- [javaboy-github/only-programer-sns-client](https://github.com/javaboy-github/only-programer-sns-client)
  - Golang
- [nyanpyou106/versatileapisns_client](https://github.com/nyanpyou106/versatileapisns_client)
  - Python

## License

MIT
