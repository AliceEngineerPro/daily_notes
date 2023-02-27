# coding: utf8
""" 
@File: conn_mysql.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/28 10:21
"""

import pymysql


def conn_mysql(host, username, password, port=3306):
    conn = pymysql.connect(
        host=host,
        user=username,
        password=password,
        port=port
    )
    cur = conn.cursor()
    cur.execute("""select now();""")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    conn.cursor()


class DefaultClass:

    def __init__(self, a, b=None):
        self.a = a
        self.b = {} if b is None else b

    def get_v(self):
        print(self.a)
        print(self.b)


if __name__ == '__main__':
    DefaultClass(a=1).get_v()

    try:
        conn_mysql(
            host='10.0.1.13',
            username='root',
            password='root1',
            port=13306
        )
    except Exception:
        print('---')




