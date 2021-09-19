import argparse

from .create_user import CreateUser
from .get_post import GetPostInfo
from .get_user import GetUserInfo
from .submit_post import SubmitPost


def func_create_user(ns: argparse.Namespace) -> None:
    c = CreateUser()
    print(c.create_user(ns.name, ns.description))


def func_update_user(ns: argparse.Namespace) -> None:
    c = CreateUser()
    print(c.update_user(ns.name, ns.description))


def func_get_post(ns: argparse.Namespace) -> None:
    g = GetPostInfo()
    if ns.post_id is None:
        print(g.get_post_all())
    else:
        print(g.get_post(ns.post_id))


def func_get_user(ns: argparse.Namespace) -> None:
    g = GetUserInfo()
    if ns.user_id is None:
        print(g.get_user_all())
    else:
        print(g.get_user(ns.user_id))


def func_submit_post(ns: argparse.Namespace) -> None:
    s = SubmitPost()
    print(
        s.submit_post(
            ns.text,
            rep_user_id=ns.user_id,
            rep_post_id=ns.post_id
        )
    )


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='simv',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Simple command for sending requests to versatileapi')

    parser.set_defaults(func=lambda _: parser.print_usage())

    subparsers = parser.add_subparsers()

    create_user_parser = subparsers.add_parser(
        "create_user", aliases=["cu"],
        help=""
    )
    create_user_parser.add_argument(
        "-n", "--name", metavar="NAME", type=str,
        default="", help="your name"
    )
    create_user_parser.add_argument(
        "-d", "--description", metavar="DESCRIPTION", type=str,
        default="", help="self introduce"
    )
    create_user_parser.set_defaults(func=func_create_user)

    update_user_parser = subparsers.add_parser(
        "update_user", aliases=["uu"],
        help=""
    )
    update_user_parser.add_argument(
        "-n", "--name", metavar="NAME", type=str,
        default="", help="your name"
    )
    update_user_parser.add_argument(
        "-d", "--description", metavar="DESCRIPTION", type=str,
        default="", help="self introduce"
    )
    update_user_parser.set_defaults(func=func_update_user)

    get_post_parser = subparsers.add_parser(
        "get_post", aliases=["gp"],
        help=""
    )
    get_post_parser.add_argument(
        "-p", "--post_id", metavar="POSTID", type=str,
        help="id of a specific post"
    )
    get_post_parser.set_defaults(func=func_get_post)

    get_user_parser = subparsers.add_parser(
        "get_user", aliases=["gu"],
        help=""
    )
    get_user_parser.add_argument(
        "-u", "--user_id", metavar="USERID", type=str,
        help="id of a specific user"
    )
    get_user_parser.set_defaults(func=func_get_user)

    submit_post_parser = subparsers.add_parser(
        "submit_post", aliases=["sp"],
        help=""
    )
    submit_post_parser.add_argument(
        "text", metavar="TEXT", type=str,
        help="post text"
    )
    submit_post_parser.add_argument(
        "-u", "--user_id", metavar="USERID", type=str,
        help="id of a specific user you reply to"
    )
    submit_post_parser.add_argument(
        "-p", "--post_id", metavar="POSTID", type=str,
        help="id of a specific post you reply to"
    )
    submit_post_parser.set_defaults(func=func_submit_post)

    return parser.parse_args()


def main() -> None:
    args = parse()
    args.func(args)


if __name__ == "__main__":
    main()
