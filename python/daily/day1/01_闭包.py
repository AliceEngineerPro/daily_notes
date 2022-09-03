# coding: utf8
"""
@File: 01_闭包.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/3 22:15
"""

# def show():
#     n =1
#     print(n)
#     
#     
# show()
# print(n)


def outer():
    n = 1
    
    def inner():
        print(n)
    
    # 返回内函数的引用(函数名称)
    return inner


def show():
    print('show', end='')


if __name__ == '__main__':
    print(outer())
