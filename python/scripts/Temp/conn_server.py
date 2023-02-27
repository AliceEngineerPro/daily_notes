# coding: utf8
""" 
@File: conn_server.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/27 21:21
"""

import paramiko
from typing import Any


class ConnectServer:

    def __init__(self, hostname, username, password, port=22):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.conn: Any = None
        self.conn_session: Any = None

    def send_message(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password
            )
            self.conn = ssh.get_transport().open_session()
            if self.conn.active:
                # self.conn.exec_command(command='df -h')
                self.conn.exec_command(command='ls -all')
                print(self.conn.recv(1024).decode('utf-8'))
            ssh.close()
        except Exception as error:
            print(error)
        
        
def main():
    ssh_server = ConnectServer(
        hostname='10.31.102.2',
        username='alice',
        password='alice'
    )
    ssh_server.send_message()
    
    
if __name__ == '__main__':
    main()
