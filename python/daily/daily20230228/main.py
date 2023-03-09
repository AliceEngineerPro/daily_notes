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


def subprocess_run():
    s = subprocess.run('python --version')
    print(s.returncode)


if __name__ == '__main__':
    subprocess_run()
