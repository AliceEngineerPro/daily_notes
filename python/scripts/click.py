# coding: utf8
""" 
@File: click.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/22 0:37
"""

import pyautogui
import time

if __name__ == '__main__':
    while 1:
        print('5秒后进行操作')
        time.sleep(10)
        pyautogui.click(700, 379)
        time.sleep(1)
        # pyautogui.click(738, 425)
        time.sleep(60*60)
