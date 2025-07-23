# fileFlask


基于Flask的简单服务器

## 开发环境：
- Windows 10
- Python 3.8

### 第三方库

- fileMapping 0.4.0
- Flask 3.0.3


## 运行环境：
- Windows 7+
- Linux

### python
- python3.8+

### 第三方库
- fileMapping 0.4.0
- Flask


## 手册

### 公开函数

#### flaskApp

这个是 flask.Flask 的实例

你可以通过它来 ~~注册路由、设置配置、~~ 启动服务器

请不要用这个进行 `注册路由` 应该要使用 `RoutingRegistration`

#### RoutingRegistration

`RoutingRegistration`是一个类

一般用于 `注册路由` 可以更好的管理路由

#### appRun

这个函数用于启动服务器


#### nameLegitimacyChecks

这个函数用于检查文件名是否合法

