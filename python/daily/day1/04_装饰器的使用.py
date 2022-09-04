# coding: utf8
""" 
@File: 04_装饰器的使用.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 3:07
"""

import time


def func():
    start = time.time()
    n = 0
    for i in range(10000000):
        n += i
    print(n)
    end = time.time()
    print(f'{end - start}s')


if __name__ == '__main__':
    func()
