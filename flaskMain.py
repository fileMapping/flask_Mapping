import functools
import random
import uuid
from types import FunctionType
from typing import List
import string

import rich
from flask import Flask, Response
from fileMapping import File
from fileMapping.core import decorators


from . import config, funos

aliasRouting = True
appRegistrationWrapper = decorators.tagAppRegistration(config.__name__)


class CustomResponse(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 移除 Server 头
        del self.headers['Server']


def main(fileMapping: File):
    global aliasRouting
    # 全局变量设置

    from . import config

    flask_config = fileMapping.plugInRunData.pluginConfig
    if config.__name__ in flask_config:
        # 判断fileMapping有没有给配置
        config = flask_config[config.__name__]
        rich.print(config)

    # 注册蓝图
    app = Flask(**{
        "import_name": config.name,
        "template_folder": config.flask["template_folder"],
        "static_folder": config.flask["static_folder"]
    })
    if config.removeServerHeader:
        # 移除 Server 头
        app.response_class = CustomResponse
    app.app_context()
    # 创建应用上下文

    appRegistrationWrapper("flaskApp")(app)
    # 向fileMapping注册flaskApp

    aliasRouting = config.aliasRouting
    # 全局变量设置
    appRegistrationWrapper()(funos.nameLegitimacyChecks)
    # 向fileMapping注册nameLegitimacyChecks
    appRunParameters = {
        # flask.run() 运行参数
        "host": config.flask["host"],
        "port": config.flask["port"]
    }
    appRegistrationWrapper("appRun")(appRun(app, **appRunParameters))


def appRun(app: Flask, **kwargs):
    """
    启动flask应用
    """
    def wrapper():
        return app.run(**kwargs)

    return wrapper


@appRegistrationWrapper()
class RoutingRegistration:
    uuid = []
    aliasRouting: bool = aliasRouting
    # -> config.aliasRouting
    def __init__(self, app: Flask, alias: str='', methods: List[str]=None):
        if methods is None:
            methods = ["GET", "POST"]

        self.app = app
        self.alias = alias
        self.methods = methods
        self.characterSpace = []

    def randomlyGenerated(self) -> str:
        # 随机生成字符
        while True:
            _ = ''.join(random.sample(string.ascii_letters,10))
            if _ in self.characterSpace:
                continue

            self.characterSpace.append(_)
            return _


    def wrapper(self, path: str, **kwargs) -> FunctionType:
        """
        注册路由
        :param path: 当为空时, 默认使用 func.__name__
        :param kwargs: app.route 的参数
        :return:
        """
        def decorator(func: FunctionType):
            if self.aliasRouting:
                # 别名路由
                func.__name__ = self.randomlyGenerated()
            return self.app.route(f"{self.alias}/{path}", methods=self.methods, **kwargs)(func)
            # 注册路由

        return decorator

