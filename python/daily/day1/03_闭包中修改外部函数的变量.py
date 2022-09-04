# coding: utf8
""" 
@File: 03_闭包中修改外部函数的变量.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 2:50
"""


def outer():
    n = 1

    def inner():
        # nonlocal关键字来声明变量为外部函数变量
        nonlocal n
        n = 10
        print(n)

    return inner


if __name__ == '__main__':
    outer()()
