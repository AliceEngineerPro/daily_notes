# coding: utf8
""" 
@File: p_wrapper.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/5 16:48
"""

import time


class RunTime(object):
    
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.function(*args, **kwargs)
        run_time = time.time() - start_time
        print(f'运行时间: {run_time}')
        return result
        
        
