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
from tqdm import tqdm

if __name__ == '__main__':
    while 1:
        dir = r'Z:\runnet\networkRadarHistory\CR'
        lists = os.listdir(dir)
        lists.sort(key=lambda x: os.path.getmtime(dir + '\\' + x))
        file_new = lists[-1]
        name = file_new.split('.')[0]
        Y = name[:4]
        M = name[4:6]
        D = name[6:8]
        H = name[8:10]
        m = name[10:]
        print('10秒后进行操作...')
        time.sleep(10)
        # 操作
        pyautogui.click(24, 634)
        time.sleep(0.1)
        # 分析
        pyautogui.click(71, 684)
        time.sleep(0.1)
        # 年
        pyautogui.doubleClick(183, 761)
        pyautogui.typewrite('{}'.format(Y))
        # 月
        pyautogui.doubleClick(248, 765)
        pyautogui.typewrite('{}'.format(M))
        # 日
        pyautogui.doubleClick(283, 765)
        pyautogui.typewrite('{}'.format(D))
        # 时
        pyautogui.doubleClick(196, 783)
        pyautogui.typewrite('{}'.format(H))
        # 分
        pyautogui.doubleClick(241, 788)
        pyautogui.typewrite('{}'.format(m))
        # 秒
        pyautogui.doubleClick(283, 787)
        pyautogui.typewrite('00')
        # 运行
        pyautogui.click(206, 826)
        for _ in tqdm(range(1, 3601)):
            time.sleep(1)
