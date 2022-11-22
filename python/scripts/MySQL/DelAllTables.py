# coding: utf-8

import pymysql
import logging
import json
from typing import Any 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s: %(message)s',
                    )


def connection() -> Any:
    """
    连接数据库
    :return:
    """
    connect = pymysql.Connection(
        host='10.31.101.2',
        port=13306,
        user='root',
        password='root',

    )

    cur = connect.cursor()

    return cur


def del_tables(database: str) -> str:
    """
    删除一个数据库中的所有表
    :return:
    """
    cur = connection()
    try:
        cur.execute(query=f"use {database} ;")
        cur.execute(query=f'show tables')
        tables = cur.fetchall()
        for table in tables:
            try:
                cur.execute(query=f'drop table {table[0]}')
            except Exception as error:
                cur.close()
                logging.exception(error)
                msg = {'status': False, 'message': f'{error}'}
                return json.dumps(msg)
    except Exception as error:
        logging.exception(error)
        msg = {'status': False, 'message': f'{error}'}
        return json.dumps(msg)
    cur.close()
    msg = {'status': True, 'message': f'From {database} delete all tables'}
    return json.dumps(msg)


def del_database(database: str) -> str:
    """
    删除数据库
    :param database:
    :return:
    """
    cur = connection()
    try:
        cur.execute(query=f'drop database {database}')
    except Exception as error:
        logging.exception(error)
        msg = {'status': False, 'message': f'{error}'}
        return json.dumps(msg)
    cur.close()
    msg = {'status': True, 'message': f'Delete {database} database successful'}
    return json.dumps(msg)


def create_database(database: str) -> str:
    """
    创建数据库
    :param database:
    :return:
    """
    cur = connection()
    try:
        cur.execute(query=f'create database {database} charset utf8mb4')
    except Exception as error:
        logging.exception(error)
        msg = {'status': False, 'message': f'{error}'}
        return json.dumps(msg)
    cur.close()
    msg = {'status': True, 'message': f'Create {database} database successful'}
    return json.dumps(msg)


if __name__ == '__main__':
    print(del_database(database='hm_day1'))
    print(create_database(database='hm_day1'))
    pass
