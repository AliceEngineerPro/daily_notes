# coding: utf8
"""
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/21 15:57
"""

import requests
import json
from lxml import etree
import time
import fake_useragent


class MoviesDouban(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        self.proxies = {
            'http': 'http://127.0.0.1:56789',
            'https': 'http://127.0.0.1:56789'
        }

    def get_hot_movies(self):
        # url_list: list = []
        for number in range(0, 351, 50):
            request_url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start={number}'
            # request_url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=5&page_start=193'
            response = requests.get(url=request_url, headers=self.headers, proxies=self.proxies)
            response_dict = json.loads(response.content.decode())
            for data in response_dict.get('subjects'):
                # url_list.append(data['url'])
                detailed_hot_movie_response = requests.request(
                    method='GET',
                    url=data['url'],
                    # url='https://movie.douban.com/subject/35608160/',
                    headers=self.headers,
                )
                parse_html = etree.HTML(detailed_hot_movie_response.content.decode())
                detailed_hot_movie_name = parse_html.xpath('//span[@property="v:itemreviewed"]/text()')
                detailed_hot_movie_director = parse_html.xpath('//span[@class="attrs"]/a[@rel="v:directedBy"]/text()')
                # print(url_hot_movie)
                # print(detailed_hot_movie_name, detailed_hot_movie_director)
                print(data['url'])
                print(f'电影: {detailed_hot_movie_name[0]} 导演是: {detailed_hot_movie_director[0]}')
                time.sleep(1)
                
                # for data_key, data_value in data.items():
                    # if data_key == 'url':
                    #     init_num += 1
                    #     url_list.append(data_value)
        # return url_list
        # return init_num

    @classmethod
    def detailed_hot_movies(cls):
        print(cls().get_hot_movies())
        for url_hot_movie in cls().get_hot_movies():
            detailed_hot_movie_response = requests.request(
                method='GET',
                url=url_hot_movie,
                # url='https://movie.douban.com/subject/35608160/',
                headers=cls().headers,
            )
            parse_html = etree.HTML(detailed_hot_movie_response.content.decode())
            detailed_hot_movie_name = parse_html.xpath('//span[@property="v:itemreviewed"]/text()')
            detailed_hot_movie_director = parse_html.xpath('//span[@class="attrs"]/a[@rel="v:directedBy"]/text()')
            # print(url_hot_movie)
            print(detailed_hot_movie_name, detailed_hot_movie_director)
            print(f'电影: {detailed_hot_movie_name[0]} 导演是: {detailed_hot_movie_director[0]}')



class FakeUserAgentTest(object):
    
    def __index__(self):
        # fake_useragent.UserAgent.update()
        pass
    
    @ staticmethod
    def get_random_user_agent():
        for _ in range(101):
            print(fake_useragent.UserAgent().random)
