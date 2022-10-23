# coding: utf8
"""
@File: connect_mysql.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/21 16:50
"""

import pymysql
from typing import Any
import json


class ConnectMySQLDataBase(object):
    """连接数据"""

    def __init__(self):
        self.host = 'connect.server.alicehome.ltd'
        self.port = 52001
        self.user = 'root'
        self.password = 'root'
        self.database = 'tb_test_basic'

    def init_connect(self) -> Any:
        """
        连接数据库
        :return: 
        """
        try:
            connect = pymysql.Connection(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connect.cursor()
        except Exception as error:
            return error
        
    def create_database(self) -> json:
        cur = self.init_connect()
        sql_query_001 = "create table movie(id int primary key auto_increment,directors varchar(255),rate varchar(255), title varchar(255),casts varchar(255),cover varchar(255),detailLink varchar(255),year varchar(255),types varchar(255),country varchar(255),lang varchar(255),time varchar(255),moveiTime varchar(255),comment_len varchar(255),strts varchar(255),summary varchar(2555),comments text,imgList varchar(2555),movieurl varchar(255)) "
        try:
            cur.execute(query=sql_query_001)
        except Exception as error:
            return error
        cur.close()
        return json.dumps({'code': 200, 'msg': 'successes', 'data': '创建成功'})


if __name__ == '__main__':
    print(ConnectMySQLDataBase().create_database())
    pass


