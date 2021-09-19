from simpleverse import CreateUser, GetPostInfo, GetUserInfo, SubmitPost

# import pytest

C = CreateUser()
P = GetPostInfo()
U = GetUserInfo()
S = SubmitPost()


def test_create_user() -> None:
    user_id = C.create_user(name="hello", description="hello")
    assert len(user_id) == 40


def test_update_user() -> None:
    user_id = C.update_user(name="hello", description="")
    assert len(user_id) == 40


def test_get_post_all() -> None:
    posts = P.get_post_all()
    assert len(posts) >= 3359


def test_get_post() -> None:
    post = P.get_post(id_="5672fc00-1cd6-4716-b14e-cac082814e81")
    assert post == {
        'id': '5672fc00-1cd6-4716-b14e-cac082814e81',
        '_created_at': '2021-07-16T04:33:28.924+00:00',
        '_updated_at': '2021-07-16T04:33:28.924+00:00',
        '_user_id': '3a1bdba464ccb76022e0d10f657a0effdc24782c',
        'text': 'はじめてのツイーヨ！'
    }


def test_get_user_all() -> None:
    users = U.get_user_all()
    assert len(users) >= 289


def test_get_user() -> None:
    user = U.get_user(id_="3a1bdba464ccb76022e0d10f657a0effdc24782c")
    assert user["_created_at"] == "2021-07-22T05:47:44.384+00:00"


def test_submit_post() -> None:
    post_id = S.submit_post(
        text=("hello woooooooold!\n"
              "(this post submitted by https://git.io/JzmhD)")
    )
    assert len(post_id) == 36
