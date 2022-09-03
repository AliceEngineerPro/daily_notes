# coding: utf8
""" 
@File: 02_闭包的使用.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/4 0:03
"""


class Personal(object):
    
    
    def __init__(self, name: str):
        self.name = name
        
        
    def say(self, msg: str):
        print(f'{self.name}: {msg}')
        
        
def personal_outer(name):
    
    def personal_inner(msg):
        print(f'{name}: {msg}')
        
    return personal_inner


if __name__ == '__main__':
    a = Personal(name='a')
    b = Personal(name='b')
    a.say(msg='hello')
    b.say(msg='world')
    
    aa = personal_outer(name='aa')
    bb = personal_outer(name='bb')
    aa(msg='hello')
    bb(msg='world')





