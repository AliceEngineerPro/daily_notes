# coding: utf8
""" 
@File: testing.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/5 16:52
"""

import p_wrapper


@p_wrapper.RunTime
def add_num():
    n = 0
    for index in range(0, 100):
        n += index
    return n


if __name__ == '__main__':
    print(add_num())
