# coding: utf8
""" 
@File: 08_类装饰器.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 23:58
"""


class Wrapper:
    
    def __int__(self, func):
        self.func= func
    
    def __call__(self, *args, **kwargs):
        print('类装饰器')
        self.func()
        
        
@Wrapper
def function():
    print('name')
