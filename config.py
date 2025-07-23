


__name__ = "fileFlask"
# 插件名字
# 不要修改这个名字


name: str = 'Flask'
# 这个是运行环境的名字
# 例如： app = Flask(name)
# 一般没有用
# 这个名字可以随便取 但是不为 None 字符串


removeServerHeader: bool = True
# 移除 Server 头

aliasRouting: bool = True
# 是否开启路由别名功能(函数)
"""
有多个函数注册时
如果函数名相同 则会覆盖之前的函数/可能导致错误报错

例如：
```python
@app.route('/url1')
def index(): ...

@app.route('/url2')
def index(): ...
```

"""

flask = {
    # 默认config
    "host": "127.0.0.1",
    # 默认host 如果要开放外网，请修改为0.0.0.0
    "port": 7000,
    "debug": False,
    # 是否开启debug模式 一般开发环境下开启
    "template_folder": "static",
    # 静态文件目录 一般是 js css img 的目录
    "static_folder": "templates"
    # 模板文件目录 一般是 html 文件的目录
}

