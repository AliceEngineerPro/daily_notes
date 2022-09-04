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


# 装饰器基本格式
def running_time(function):
    def run():
        start = time.time()
        function()
        end = time.time()
        print(f'运行时长: {round(end - start, 2)}s')
    return run

@running_time  # -->count = running_time(count)
def count():
    n = 0
    for i in range(10000000):
        n += i
    print(n)


if __name__ == '__main__':
    # func()
    count()
