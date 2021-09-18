# from os.path import expanduser, join

import requests
from requests.exceptions import RequestException


class BaseVerseRequests(object):
    URL = "https://versatileapi.herokuapp.com/api"
    # CONF_PATH = join(expanduser('~'), ".verse_id")

    # def __init__(self):
    #     print(end="", file=open(self.CONF_PATH, 'a'))
    #     self.__get_own_id()

    # def __get_own_id(self):
    #     i = open(self.CONF_PATH, 'r').readline().rstrip()
    #     if i != "":
    #         self.id = i
    #     else:
    #         self.id = None

    # def __set_own_id(self, id: str) -> None:
    #     if type(id) is str and id != "":
    #         print(id, end="", file=open(self.CONF_PATH, 'w'))
    #         self.id = id
    #     else:
    #         raise ValueError(id)

    def get_endpoint(self, endpoint: str) -> str:
        return self.URL + endpoint

    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_response(res: requests.Response) -> None:
        if not res.ok:
            raise RequestException(
                f"{res.status_code}: {res.text}"
            )
