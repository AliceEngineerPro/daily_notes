# coding: utf8
""" 
@File: redis_cil.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/8 13:31
"""

import redis


def redis_connection():
    try:
        redis_connect = redis.Redis(
            host='10.31.101.2',
            port=6379,
            db=0,
            password=None,

        )
        return redis_connect
    except Exception as error:
        return error


if __name__ == '__main__':
    redis_conn = redis_connection()
    status = redis_conn.set(name='name', value='alice1')
    print(status)
    get_name = redis_conn.get(name='name')
    print(get_name)
    pass
