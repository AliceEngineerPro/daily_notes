# coding: utf8
""" 
@File: 09_装饰器传参.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/5 0:32
"""


def set_args(msg):
    def set_func(func):
        def param_func(*args, **kwargs):
            print(f'装饰内容 {msg}')
            func(*args, **kwargs)

        return param_func

    return set_func


@set_args('hello')
def function(msg_1):
    print(msg_1)


if __name__ == '__main__':
    function(msg_1=1)
