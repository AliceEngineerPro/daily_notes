# coding: utf8
""" 
@File: 07_可调用对象(类装饰器).py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 22:35
"""


def function():
    print(1)


# 使用 callable 来判断是否可调用
print(callable(function))


class Personal:
    
    # 如果在类中实现了 __call__ 函数, 那么这个类的实例化对象就变成了可调用对象
    def __call__(self, *args, **kwargs):
        print('调用 __call__')
        pass


if __name__ == '__main__':
    # 实例化对象
    tom = Personal()
    # 调用对象
    tom()
