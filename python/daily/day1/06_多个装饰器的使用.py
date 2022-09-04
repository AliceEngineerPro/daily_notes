# coding: utf8
""" 
@File: 06_多个装饰器的使用.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 21:43
"""


def wrapper_dev(function):
    def wrapper(*args, **kwargs):
        return f'<dev>{function(*args, **kwargs)}</dev>'

    return wrapper


def wrapper_p(function):
    def wrapper(*args, **kwargs):
        return f'<p>{function(*args, **kwargs)}</p>'

    return wrapper


@wrapper_dev
@wrapper_p
def func():
    return '多装饰器'


if __name__ == '__main__':
    print(func())
