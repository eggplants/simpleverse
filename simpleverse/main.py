import argparse
import shlex
from base64 import b64encode
from imghdr import what
from json import dumps
from typing import Any, List, Optional

from prompt_toolkit.shortcuts import prompt

from .create_like import CreateLike
from .create_user import CreateUser
from .get_image import GetImageInfo
from .get_like import GetLikeInfo
from .get_post import GetPostInfo
from .get_user import GetUserInfo
from .submit_image import SubmitImage
from .submit_post import SubmitPost


def pprint_json(json_obj: Any) -> None:
    print(dumps(json_obj, sort_keys=True, indent=4, ensure_ascii=False))


def func_create_like(ns: argparse.Namespace) -> None:
    c = CreateLike()
    print(c.create_like(ns.post_id, ns.like_count))


def func_create_user(ns: argparse.Namespace) -> None:
    c = CreateUser()
    print(c.create_user(ns.name, ns.description))


def func_update_user(ns: argparse.Namespace) -> None:
    c = CreateUser()
    print(c.update_user(ns.name, ns.description))


def func_get_like(ns: argparse.Namespace) -> None:
    g = GetLikeInfo()
    if ns.post_id is None:
        pprint_json(g.get_like_all())
    else:
        pprint_json(g.get_like(ns.post_id))


def func_get_image(ns: argparse.Namespace) -> None:
    g = GetImageInfo()
    if ns.image_id is None:
        pprint_json(g.get_image_all())
    else:
        pprint_json(g.get_image(ns.image_id))


def func_get_post(ns: argparse.Namespace) -> None:
    g = GetPostInfo()
    if ns.post_id is None:
        pprint_json(g.get_post_all())
    else:
        pprint_json(g.get_post(ns.post_id))


def func_get_user(ns: argparse.Namespace) -> None:
    g = GetUserInfo()
    if ns.user_id is None:
        pprint_json(g.get_user_all())
    else:
        pprint_json(g.get_user(ns.user_id))


def func_submit_post(ns: argparse.Namespace) -> None:
    s = SubmitPost()
    print(s.submit_post(ns.text, rep_user_id=ns.user_id, rep_post_id=ns.post_id))


def func_submit_image(ns: argparse.Namespace) -> None:
    s = SubmitImage()
    body = repr(b64encode(open(ns.image, "rb").read()))
    img_type = what(ns.image)
    if img_type is None:
        raise OSError("Is not given file a sort of an image?")
    d = "data:image/" + img_type + ";base64," + body
    print(s.submit_image(d, ns.post_id))


def func_repl(ns: argparse.Namespace) -> None:
    while True:
        print("[cl,cu,uu,gl,gi,gp,gu,sp,si,exit,q]")
        try:
            inputs = "simv " + prompt("simv> ")
        except KeyboardInterrupt:
            print("bye.")
            exit(0)
        cmd_args = shlex.split(inputs, comments=False, posix=True)
        repl(cmd_args)


def repl(cmd_args: List[str]) -> None:
    if cmd_args in (["simv", "exit"], ["simv", "q"]):
        print("bye.")
        exit(1)
    try:
        args = parse(cmd_args[1:])
        args.func(args)
    except KeyboardInterrupt:
        print("bye.")
        exit(0)
    except SystemExit:
        # print(cmd_args)
        pass


def parse(test_args: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="simv",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Simple command for sending requests to versatileapi",
    )

    parser.set_defaults(func=lambda _: parser.print_usage())

    subparsers = parser.add_subparsers()

    create_like_parser = subparsers.add_parser("create_like", aliases=["cl"], help="")
    create_like_parser.add_argument(
        "-p",
        "--post_id",
        metavar="POSTID",
        type=str,
        help="id of a specific post",
        required=True,
    )
    create_like_parser.add_argument(
        "-n",
        "--like_count",
        metavar="POSITIVE",
        type=int,
        help="count of like you want to submit",
        required=True,
    )
    create_like_parser.set_defaults(func=func_create_like)

    create_user_parser = subparsers.add_parser("create_user", aliases=["cu"], help="")
    create_user_parser.add_argument(
        "-n", "--name", metavar="NAME", type=str, default="", help="your name"
    )
    create_user_parser.add_argument(
        "-d",
        "--description",
        metavar="DESCRIPTION",
        type=str,
        default="",
        help="self introduce",
    )
    create_user_parser.set_defaults(func=func_create_user)

    update_user_parser = subparsers.add_parser("update_user", aliases=["uu"], help="")
    update_user_parser.add_argument(
        "-n", "--name", metavar="NAME", type=str, default="", help="your name"
    )
    update_user_parser.add_argument(
        "-d",
        "--description",
        metavar="DESCRIPTION",
        type=str,
        default="",
        help="self introduce",
    )
    update_user_parser.set_defaults(func=func_update_user)

    get_like_parser = subparsers.add_parser("get_like", aliases=["gl"], help="")
    get_like_parser.add_argument(
        "-p", "--post_id", metavar="POSTID", type=str, help="id of a specific post"
    )
    get_like_parser.set_defaults(func=func_get_post)

    get_image_parser = subparsers.add_parser("get_image", aliases=["gi"], help="")
    get_image_parser.add_argument(
        "-i", "--image_id", metavar="IMAGEID", type=str, help="id of a specific image"
    )
    get_image_parser.set_defaults(func=func_get_image)

    get_post_parser = subparsers.add_parser("get_post", aliases=["gp"], help="")
    get_post_parser.add_argument(
        "-p", "--post_id", metavar="POSTID", type=str, help="id of a specific post"
    )
    get_post_parser.set_defaults(func=func_get_post)

    get_user_parser = subparsers.add_parser("get_user", aliases=["gu"], help="")
    get_user_parser.add_argument(
        "-u", "--user_id", metavar="USERID", type=str, help="id of a specific user"
    )
    get_user_parser.set_defaults(func=func_get_user)

    submit_post_parser = subparsers.add_parser("submit_post", aliases=["sp"], help="")
    submit_post_parser.add_argument("text", metavar="TEXT", type=str, help="post text")
    submit_post_parser.add_argument(
        "-u",
        "--user_id",
        metavar="USERID",
        type=str,
        help="id of a specific user you reply to",
    )
    submit_post_parser.add_argument(
        "-p",
        "--post_id",
        metavar="POSTID",
        type=str,
        help="id of a specific post you reply to",
    )
    submit_post_parser.set_defaults(func=func_submit_post)

    submit_image_parser = subparsers.add_parser("submit_image", aliases=["si"], help="")
    submit_image_parser.add_argument(
        "file", metavar="IMAGE", type=str, help="post image"
    )
    submit_image_parser.add_argument(
        "-p",
        "--post_id",
        metavar="POSTID",
        type=str,
        help="id of a specific post you reply to",
    )
    submit_image_parser.set_defaults(func=func_submit_image)

    repl_parser = subparsers.add_parser("repl", aliases=["rl"], help="")
    repl_parser.set_defaults(func=func_repl)

    if test_args is not None:
        return parser.parse_args(test_args)
    else:
        return parser.parse_args()


def main() -> None:
    args = parse()
    args.func(args)


if __name__ == "__main__":
    main()
