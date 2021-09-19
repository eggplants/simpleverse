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
usage: simv [-h] {create_user,cu,update_user,uu,get_post,gp,get_user,gu,submit_post,sp} ...

Simple command for sending requests to versatileapi

positional arguments:
  {create_user,cu,update_user,uu,get_post,gp,get_user,gu,submit_post,sp}
    create_user (cu)
    update_user (uu)
    get_post (gp)
    get_user (gu)
    submit_post (sp)

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
from simpleverse import (CreateUser,
                         GetPostInfo,
                         GetUserInfo,
                         SubmitPost)


class CreateUser(BaseVerseRequests):
    def create_user(self, name: str, description: str) -> str: ...
    def update_user(self, name: str, description: str) -> str: ...


class GetPostInfo(BaseVerseRequests):
    def get_post_all(self) -> List[PostInfo]: ...
    def get_post(self, id_: str) -> PostInfo: ...
    def get_post_OData(
        self,
        filter_: Optional[str],
        order_by: Optional[str],
        limit: Optional[str],
        skip: Optional[str]
    ) -> List[PostInfo]: ...


class GetUserInfo(BaseVerseRequests):
    def get_user_all(self) -> List[UserInfo]: ...
    def get_user(self, id_: str) -> UserInfo: ...


class SubmitPost(BaseVerseRequests):
    def submit_post(
        self,
        text: str,
        rep_user_id: Optional[str],
        rep_post_id: Optional[str]
    ) -> str: ...
```

</details>

<!-- markdownlint-enable MD033 -->

## TIPS

- [エンジニア・プログラマにしか使えない SNS を作ってみた話](https://qiita.com/HawkClaws/items/599d7666f55e79ef7f56)
- [Swagger](https://editor.swagger.io/?url=https://gist.githubusercontent.com/YusukeIwaki/ce8a7250fb7e5279267c495324de19f7/raw/292eb24fb381c9af49fc42c901794ec2d98d134a/openapi.yml)
- [エンジニア・プログラマにしか使えないSNSのWebクライアント](https://lightwill.tokyo/dev/sns/?selectUserId=b6e4ae19fc2c59ce55c726de44a40dc825faa04d)
  - `https://lightwill.tokyo/dev/sns/?selectUserId={userid}`

## License

MIT
