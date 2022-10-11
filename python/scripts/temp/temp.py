# coding: utf8
""" 
@File: temp.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/11 15:48
"""

# import re
# import time
# import json
# import urllib
# import win32api, win32con
# import os
# from tkinter import *
# import requests
# import tkinter as tk
# 
# # 设置header 头
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
#     "Accepted-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "referer": "https://user.qzone.qq.com/"
# }
# 
# 
# def get_gtk():
#     p_skey = cookie['p_skey']
#     h = 5381
#     g_tk = None
#     for i in p_skey:
#         h += (h << 5) + ord(i)
#         g_tk = h & 2147483647
#     return g_tk
# 
# 
# def get_uin():
#     uin = cookie['ptui_loginuin']
#     return uin
# 
# 
# # 找出好友列表
# def get_friend():
#     url_friend = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?'
#     g_tk = get_gtk()
#     uin = get_uin()
#     data = {
#         'uin': uin,
#         'do': 1,
#         'g_tk': g_tk
#     }
#     data_encode = urllib.parse.urlencode(data)
#     url_friend += data_encode
#     res = requests.get(url_friend, headers=header, cookies=cookie)
#     friend_json = re.findall('\((.*)\)', res.text, re.S)[0]
#     # print(friend_json)
#     friend_dict = json.loads(friend_json)
#     friend_result_list = []
#     # 循环将好友的姓名qq号存入字典中
#     for friend in friend_dict['data']['items_list']:
#         friend_result_list.append([friend['name'], friend['uin']])
#     # 得到的好友字典是{name: qqNum}格式的
#     return friend_result_list
# 
# 
# def get_mobile(uin):
#     url_mobile = "接口?qq={}".format(uin)
# 
#     try:
#         mobile_code = requests.get(url_mobile, timeout=5).status_code
#         if mobile_code == 200 and requests.get(url_mobile).text != '404':
#             mobile = requests.get(url_mobile).text
#             if json.loads(mobile)['qq'] != None:
#                 return json.loads(mobile)['qq']
#         else:
#             return "未知"
#     except:
#         return "获取失败!"
# 
# 
# if __name__ == "__main__":
#     # 怕被滥用  设置了个时间限制 ###失策了  这个时间是电脑时间  很容易绕
#     if time.time() > 1612605600:
#         exit()
#     import cookie
# 
#     try:
#         with open('cookie_dict.txt', 'r') as f:
#             cookie = json.load(f)
#         if get_friend():
#             file = open('通讯录.txt', 'w', encoding='utf-8')
#             get_friend_result = get_friend()
#             get_friend_result_len = len(get_friend_result)
# 
#             window = tk.Tk()
#             window.title('正在获取')
#             window.geometry('630x150')
# 
#             # 设置下载进度条
#             tk.Label(window, text='获取进度:', ).place(x=50, y=60)
#             canvas = tk.Canvas(window, width=465, height=22, bg="white")
#             canvas.place(x=110, y=60)
#             fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
#             x = get_friend_result_len  # 未知变量，可更改
#             n = 465 / x  # 465是矩形填充满的次数
# 
#             for i in range(0, get_friend_result_len):
#                 mobile = get_mobile(get_friend_result[i][1])
#                 name = get_friend_result[i][0]
#                 # print("\r正在获取好友手机号：{}%".format((i)*100/get_friend_result_len), end="", flush=True)
#                 file.write(name + '-' + mobile)
#                 file.write('\n\n')
#                 # 进度条
#                 n = n + 465 / x
#                 canvas.coords(fill_line, (0, 0, n, 60))
#                 window.update()
# 
#             file.close()
#             os.remove('cookie_dict.txt')
#             win32api.MessageBox(0, "获取成功!", "提示", win32con.MB_OK)
#     except:
#         win32api.MessageBox(0, "QQ帐号或者QQ密码错误！请确保已经关闭网页QQ登录保护！\n                           若多次失败，请联系作者！", "提示",
#                             win32con.MB_OK)
#         os.remove('cookie_dict.txt')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import json
import easygui as g  # 安装easygui库

msg = "需要关闭网页QQ登录保护，酌情使用！"  # 填报提示信息
title = "获取QQ好友电话"  # 标题
# 偷下懒 密码就不做*号了
fieldNames = ["*QQ", "*QQ密码"]  # 内容和格式
fieldValues = []  # 拿个空列表装信息
fieldValues = g.multenterbox(msg, title, fieldNames)  # 把信息装进去
while True:
    if fieldValues == None:
        exit()
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ("【%s】为必填项   " % fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

if fieldValues:
    chromedriver = 'chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    driver.get('https://user.qzone.qq.com/')
    driver.switch_to.frame('login_frame')
    # 找到账号密码登陆的地方
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').send_keys(fieldValues[0])
    driver.find_element_by_id('p').send_keys(fieldValues[1])
    driver.find_element_by_id('login_button').click()
    # 保存本地的cookie
    sleep(1)
    cookies = driver.get_cookies()
    sleep(1)
    if cookies:
        cookie_dic = {}
        for cookie in cookies:
            if 'name' in cookie and 'value' in cookie:
                cookie_dic[cookie['name']] = cookie['value']
            with open('cookie_dict.txt', 'w') as f:
                json.dump(cookie_dic, f)
        # 关闭chromedriver命令窗口
        os.system("taskkill /f /im chromedriver.exe")
        os.system('taskkill /im chrome.exe /F')
