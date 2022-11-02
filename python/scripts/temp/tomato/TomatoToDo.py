# coding: utf8
"""
@File: TomatoToDo.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/2 21:41
"""

import pymysql
import time
import yaml
import os


class GetRunConfig(object):

    def __init__(self, yaml_filename, config_name):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.yaml_filename = yaml_filename
        self.config_name = config_name

    def __get_config(self) -> dict:
        yaml_filepath = os.path.join(self.base_dir, self.yaml_filename)
        with open(file=yaml_filepath, mode='r', encoding='utf-8') as yaml_config_file:
            config = yaml.load(stream=yaml_config_file, Loader=yaml.Loader)
            return config

    def get_config(self, keyword):
        config = self.__get_config()
        try:
            keyword_config: dict = config.get(self.config_name)
            return keyword_config.get(keyword)
        except Exception as error:
            print(error)


class ConnectMySQL(object):

    def __init__(self):
        self.host = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='mysql').get_config(keyword='host')
        self.port = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='mysql').get_config(keyword='port')
        self.user = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='mysql').get_config(keyword='user')
        self.password = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='mysql').get_config(keyword='password')
        self.database = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='mysql').get_config(keyword='database')
        self.charset = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='mysql').get_config(keyword='charset')

    def __connect(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset
            )

            return conn
        except Exception as error:
            print(error)

    def __execute(self, sql_msg):
        connect = self.__connect()
        cursor = connect.cursor()
        try:
            cursor.execute(query=sql_msg)
        except Exception as error:
            print(error)
            cursor.close()
            connect.close()
        cursor.close()
        connect.commit()
        connect.close()
        print(f'{time.strftime("%H:%M", time.localtime())}: 修改成功')

    def task_run(self, sql_msg):
        self.__execute(sql_msg=sql_msg)


def run_todo_1():
    traffic = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_1')['traffic']
    nodes_id = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_1')['nodes_id']
    sql_mysql = f"update nodes set nodes.traffic = '{traffic}' where nodes.id in {nodes_id} ;"
    ConnectMySQL().task_run(sql_msg=sql_mysql)
    # print(sql_mysql)


def run_todo_2():
    traffic = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_2')['traffic']
    nodes_id = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_2')['nodes_id']
    sql_mysql = f"update nodes set nodes.traffic = '{traffic}' where nodes.id in {nodes_id} ;"
    ConnectMySQL().task_run(sql_msg=sql_mysql)
    # print(sql_mysql)


def run_todo_3():
    traffic = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_3')['traffic']
    nodes_id = GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_3')['nodes_id']
    sql_mysql = f"update nodes set nodes.traffic = '{traffic}' where nodes.id in {nodes_id} ;"
    ConnectMySQL().task_run(sql_msg=sql_mysql)
    # print(sql_mysql)

if __name__ == '__main__':
    while True:
        time_now = time.strftime('%H:%M', time.localtime())
        if time_now == GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_1')['HMS']:
            run_todo_1()
        elif time_now == GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_2')['HMS']:
            run_todo_2()
        elif time_now == GetRunConfig(yaml_filename='TomatoToDoConfig.yaml', config_name='Timing').get_config(keyword='todo_3')['HMS']:
            run_todo_3()
        else:
            print('无更改')
        print('等待10秒在检测')
        time.sleep(10)
        
