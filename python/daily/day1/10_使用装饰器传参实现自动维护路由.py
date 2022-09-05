# coding: utf8
""" 
@File: 10_使用装饰器传参实现自动维护路由.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/5 2:20
"""

route_dict = {}


def add_url(url):
    def function(func):
        def wrapper(*args, **kwargs):
            func()

        route_dict[url] = wrapper

        return wrapper

    return function


@add_url('index')
def index():
    print('首页')


@add_url('home')
def home():
    print('主页')


@add_url('mail')
def mail():
    print('邮箱')


def error():
    print('错误')


def request_url(url):
    # 默认指向错误页面
    func = error
    # 判断访问的url是否在路由表中
    if url in route_dict:
        func = route_dict[url]
    func()


if __name__ == '__main__':
    request_url('home')
