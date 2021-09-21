import argparse
from typing import Any

from simpleverse import CreateLike as CreateLike
from simpleverse import CreateUser as CreateUser
from simpleverse import GetImageInfo as GetImageInfo
from simpleverse import GetLikeInfo as GetLikeInfo
from simpleverse import GetPostInfo as GetPostInfo
from simpleverse import GetUserInfo as GetUserInfo
from simpleverse import SubmitImage as SubmitImage
from simpleverse import SubmitPost as SubmitPost

def pprint_json(json_obj: Any) -> None: ...
def func_create_like(ns: argparse.Namespace) -> None: ...
def func_create_user(ns: argparse.Namespace) -> None: ...
def func_update_user(ns: argparse.Namespace) -> None: ...
def func_get_like(ns: argparse.Namespace) -> None: ...
def func_get_image(ns: argparse.Namespace) -> None: ...
def func_get_post(ns: argparse.Namespace) -> None: ...
def func_get_user(ns: argparse.Namespace) -> None: ...
def func_submit_post(ns: argparse.Namespace) -> None: ...
def func_submit_image(ns: argparse.Namespace) -> None: ...
def parse() -> argparse.Namespace: ...
def main() -> None: ...
