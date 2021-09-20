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

# import pytest

CL = CreateLike()
CU = CreateUser()
GI = GetImageInfo()
GL = GetLikeInfo()
GP = GetPostInfo()
GU = GetUserInfo()
SP = SubmitPost()
SI = SubmitImage()


def test_create_like() -> None:
    like_id = CL.create_like(
        post_id="b201405d-6504-4441-8bd5-52d3696ee122", like_count=0
    )
    assert like_id == "b201405d-6504-4441-8bd5-52d3696ee122"


def test_create_user() -> None:
    user_id = CU.create_user(name="hello", description="hello")
    assert len(user_id) == 40


def test_update_user() -> None:
    user_id = CU.update_user(name="hello", description="")
    assert len(user_id) == 40


def test_get_image_all() -> None:
    images = GI.get_image_all()
    assert len(images) >= 45


def test_get_image() -> None:
    post = GI.get_image(image_id="967fd59f-cb52-4c14-b3c7-1fc188c59d3e")
    assert post == {
        "id": "967fd59f-cb52-4c14-b3c7-1fc188c59d3e",
        "_created_at": "2021-07-24T03:05:24.701+00:00",
        "_updated_at": "2021-07-24T03:05:24.701+00:00",
        "_user_id": "d5b6d59a7a3193bc034329605028a4dd3e1345ad",
        "base64": "https://storage.nison.jp/v1/AUTH_storage/resources/yozora.mp4",
        "bind_text_id": "dcdfb64f-3c59-4ed3-81f2-ddd0a3d6df98",
    }


def test_get_post_all() -> None:
    posts = GP.get_post_all()
    assert len(posts) >= 3359


def test_get_post() -> None:
    post = GP.get_post(post_id="5672fc00-1cd6-4716-b14e-cac082814e81")
    assert post == {
        "id": "5672fc00-1cd6-4716-b14e-cac082814e81",
        "_created_at": "2021-07-16T04:33:28.924+00:00",
        "_updated_at": "2021-07-16T04:33:28.924+00:00",
        "_user_id": "3a1bdba464ccb76022e0d10f657a0effdc24782c",
        "text": "はじめてのツイーヨ！",
    }


def test_get_user_odata() -> None:
    posts = GP.get_post_OData(limit=20)
    assert len(posts) == 20


def test_get_user_all() -> None:
    users = GU.get_user_all()
    assert len(users) >= 289


def test_get_user() -> None:
    user = GU.get_user(user_id="3a1bdba464ccb76022e0d10f657a0effdc24782c")
    assert user["_created_at"] == "2021-07-22T05:47:44.384+00:00"


def test_submit_post() -> None:
    post_id = SP.submit_post(
        text=("hello woooooooold!\n" "(this post submitted by https://git.io/JzmhD)"),
        test=True,
    )
    assert len(post_id) == 36


def test_submit_image() -> None:
    post_id = SI.submit_image(
        image_data=(
            "data:image/png;base64,"
            "iVBORw0KGgoAAAANSUhEUgAAABIAAAAXCAMAAAAx3e/WAAAABG"
            "dBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAA"
            "dTAAAOpgAAA6mAAAF3CculE8AAABelBMVEX+/v7////x8fG4uL"
            "je3t79/f36+vrT09Pn5+fOzs7i4uLl5eX7+/va2trExMT//v7M"
            "zMzh4eHb29vPz8/KysrV1dXz8/P5+fj29vXu7+7v8fH29vb09P"
            "Td3d3j4uHBxMGwsrKcnJyTlpextrnZ2dnj4+O+vr6qqqrAwMDt"
            "7e3q6ury8vPZ2dfQzs/h4ujl5ea6vb7e4uLc3Nzw8PDv7+/Jyc"
            "mampq3t7fu7u7d3dvDwL3X1Nb49e7QzsrS2Nrs7Ozm5ub3+PjY"
            "19W8urKnqKfW19bg4eHj5uf19fXS0tLs7eva3N3h4uPg4OH39/"
            "fNzc3+/v3Ly8v9/v7Y2Njb29z+///p6eny8vLHx8fR0dHW2d3S"
            "09Lk5+fn5uXIy8vr7O3CwcHW1tbr6+v+/f3x8/P6+/v5+fn4+f"
            "n4+Pj8/Pzi4+P08/DR09Pm6evj5eXV1tXP0dLv8fPc3d3d3t7W"
            "19fo6Ojz8/LZ2djk5OTGxsbU1NTQ0NDf39+7u7u87OoyAAAAAW"
            "JLR0QB/wIt3gAAAAd0SU1FB+UJFBUjHOhzyJ0AAAF0SURBVBjT"
            "LZD9X9JgFMXvQZ5tsA0dbpRtmtmmoJUJM1epLE1jpeDrfCnNUh"
            "fYqxVFCf+7z5D7uT/dez/3nPMlQqIvCQYiEuimGEQplZYlRVAz"
            "Al+gnyANIKHJ2UFdNnK3bueG7lBCNy0LBEXA8Mjd0Xtj98l2xi"
            "fyBVBBnZx68PDR9OMZKpb0PtsFm30y5z199nx+YZGyZTCFv1U0"
            "/8XS8suV1Vck2xBYVxuV4PWbtfUqsVo59gTaQEqKTfDO6Zuyay"
            "nK1vYOTHM33ONWk7av7x+sHr59dyQevz+x+dmHCpD8eHp2Hgm5"
            "T1ZeJtRF1sD2xecvX799/3FZn/UIZRUNmEZg/LTVX7/LYkTwh8"
            "E4CMH1m035T/iXh5OKaP3rcon1/3t85GtN0W7GxBpE0RUHhDB1"
            "AM0BjBIfR4HCT918FW0H1Y4zYMIKugEaDG0ZQVbrFNDiWjesW3"
            "oQTmayaRheLyYxN4JUC+2CznrK3WZMqYkVrncNzF81w22hMc0A"
            "AAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDktMjBUMjE6MzU6Mj"
            "ArMDA6MDAQ3bg4AAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIxLTA5"
            "LTIwVDIxOjM1OjIwKzAwOjAwYYAAhAAAAABJRU5ErkJggg=="
        ),
        post_id="2bcf16b9-df35-4bcd-ae50-d865b95d629f",
    )
    assert len(post_id) == 36
