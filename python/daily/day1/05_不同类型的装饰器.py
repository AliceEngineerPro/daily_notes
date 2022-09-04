# coding: utf8
""" 
@File: 05_不同类型的装饰器.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 15:21
"""


# 无参数, 无返回值
def outer_1(func):
    def inner():
        print('装饰内容')
        func()

    return inner


@outer_1
def func_1():
    print(1)


# 有参数, 无返回值
def outer_2(func):
    def inner(msg):
        print('装饰内容')
        func(msg)

    return inner


@outer_2
def func_2(msg):
    print(msg)


# 无参数, 有返回值
def outer_3(func):
    def inner():
        print('装饰内容')
        return func()

    return inner


@outer_3
def func_3():
    return 3


# 有参数, 有返回值
def outer_4(func):
    def inner(msg):
        print('装饰内容')
        return func(msg)

    return inner


@outer_4
def func_4(msg):
    return msg


# 通用装饰器
def outer__(func):
    def inner(*args, **kwargs):
        print('装饰内容1')
        result = func(*args, **kwargs)
        print('装饰内容2')
        return result
    
    return inner


@outer__
def func__(name, msg):
    # print(name, msg)
    return name, msg


if __name__ == '__main__':
    # 无参数, 无返回值
    # func_1()
    # 有参数, 无返回值
    # func_2(msg=2)
    # 无参数, 有返回值
    # print(func_3())
    # 有参数, 有返回值
    # print(func_4(msg=4))
    # 通用
    print(func__(name=1, msg=2))
