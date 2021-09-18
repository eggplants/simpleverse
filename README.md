# simpleverse

[![PyPI](https://img.shields.io/pypi/v/simpleverse?color=blue)](https://pypi.org/project/simpleverse) [![Maintainability](https://api.codeclimate.com/v1/badges/3dafcba23209bf5a4a04/maintainability)](https://codeclimate.com/github/eggplants/simpleverse/maintainability)

API wrapper for [versatileapi](https://versatileapi.herokuapp.com/api) in Python

## Install

```bash
pip install simpleverse
```

## CLI

```bash
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
```

## TIPS

- [エンジニア・プログラマにしか使えない SNS を作ってみた話](https://qiita.com/HawkClaws/items/599d7666f55e79ef7f56)
- [Swagger](https://editor.swagger.io/?url=https://gist.githubusercontent.com/YusukeIwaki/ce8a7250fb7e5279267c495324de19f7/raw/292eb24fb381c9af49fc42c901794ec2d98d134a/openapi.yml)

## License

MIT
