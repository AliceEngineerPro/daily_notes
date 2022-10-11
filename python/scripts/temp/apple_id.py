# coding: utf8
""" 
@File: apple_id.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/8 22:34
"""

import requests
import bs4
import urllib

path_url = 'https://apple.laogoubi.net/p/34a6d9b585a296820393270bf5b49f34'

response = requests.request(method='get', url=path_url)
soup = bs4.BeautifulSoup(response.content, 'html.parser')
