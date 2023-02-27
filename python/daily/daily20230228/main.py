# coding: utf8
""" 
@File: main.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/28 1:02
"""

import os
import sys
import subprocess

# subprocess
def subprocess_run():
    py = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    py.stdin.write(b'print(1) \n')
    out, err = py.communicate()
    print(out, type(out))
    s_out = bytes.decode(out)
    print(s_out, type(s_out))
    print(err, type(err))
    
    
if __name__ == '__main__':
    subprocess_run()



