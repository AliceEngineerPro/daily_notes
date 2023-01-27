# coding: utf8
""" 
@File: dep.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/27 15:54
"""
import os
import paramiko
import shutil
import stat
import re
import sys
from git.repo import Repo
from git.remote import RemoteProgress
from time import sleep


class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print('\rupdate(%s, %s, %s, %s)'%(op_code, cur_count, max_count, message),end='')

class Linux():
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        self.t = None
        self.chan = None
        self.try_times = 3

    def connect(self):
        while True:
            try:
                self.t = paramiko.Transport(sock=(self.ip, 22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                print(u'连接%s成功' % self.ip)
                print(self.chan.recv(65535).decode('utf-8'))
                return
            except Exception:
                if self.try_times != 0:
                    print(u'连接%s失败，进行重试' % self.ip)
                    self.try_times -= 1
                else:
                    print(u'重试3次失败，结束程序')
                    exit(1)

    def send(self, cmd):
        cmd += '\r'
        p = re.compile(r':~\$|#')
        result = ''
        self.chan.send(cmd)
        while True:
            sleep(0.5)
            ret = self.chan.recv(65535)
            ret = ret.decode('utf-8')
            result += ret
            if p.search(ret):
                try:
                    print(result)
                except Exception as e:
                    print(e)
                return result

    def close(self):
        self.chan.close()
        self.t.close()


def readonly_handler(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def download(url, branch):
    repo_name = url.split('/')[-1].split('.')[0]
    repo_path = os.path.join(os.path.join(os.getcwd(),'projects'),repo_name)
    Repo.clone_from(url,to_path=repo_path,branch=branch,progress=Progress())
    print("\n{}已下载".format(repo_name))
    repository = Repo(repo_path)
    with open(os.path.join(os.getcwd(), '{}.tar'.format(repo_name)), 'wb') as fp:
        repository.archive(fp)
    print("{}已打包".format(repo_name))
    return '{}.tar'.format(repo_name)


def translate_byte(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(MB ** 2)
    TB = float(GB ** 2)
    if B < KB:
        return '{} {}'.format(B, 'bytes' if B > 1 else 'byte')
    elif KB < B < MB:
        return '{:.2f} KB'.format(B / KB)
    elif MB < B < GB:
        return '{:.2f} MB'.format(B / MB)
    elif GB < B < TB:
        return '{:.2f} GB'.format(B / GB)
    else:
        return '{:.2f} TB'.format(B / TB)


def call_back(curr=100, total=100):
    bar_length = 100
    percents = '\033[32;1m%s\033[0m' % round(float(curr) * 100 / float(total), 2)
    filled = int(bar_length * curr / float(total))
    bar = '\033[32;1m%s\033[0m' % '=' * filled + '-' * (bar_length - filled)
    print('\rtranslating: [{}] {}% already complete: {}, total: {}'.format(bar, percents, translate_byte(curr), translate_byte(total)), end='')


def upload_file(filename, ip, username, password):
    transport = paramiko.Transport((ip, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(filename, f'/home/{username}/{filename}',callback=call_back)
    transport.close()
    if os.path.exists(os.path.join(os.getcwd(), filename)):
        os.remove(os.path.join(os.getcwd(), filename))
    print("{}已上传".format(filename))


def download_log(url, ip, username, password):
    dir_name = url.split('/')[-1].split('.')[0]
    transport = paramiko.Transport((ip, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(f'/home/{username}/renren/{dir_name}/cmms.log', './cmms.log',callback=call_back)
    transport.close()
    print("\n日志已下载!")


def deploy(option, ip, username, password):
    dirs = os.listdir(os.path.join(os.getcwd(), 'projects'))
    host = Linux(ip, username, password)
    host.connect()
    res = host.send('sudo su')
    if res.endswith('for {}: '.format(username)):
        host.send(password)
    if option != '2':
        host.send(f'cd /home/{username}/')
        host.send(f'mkdir ./{dirs[-1]}/')
        host.send(f'tar -xvf {dirs[-1]}.tar -C ./{dirs[-1]}/')
        host.send(f'rm {dirs[-1]}.tar')
        host.send(f'cd /home/{username}/renren')
        host.send(f'rm -rf {dirs[-1]}/')
        host.send(f'mv ../{dirs[-1]}/ ./')
        host.send(f'cd {dirs[-1]}/')
        host.send('rm -rf .env.example')
        host.send('cp ../configs/.env.local ./')
        host.send('cp -r ../configs/node_modules/ ./')
        host.send('npm run build')
    if option != '1':
        host.send(f'cd /home/{username}/')
        host.send(f'mkdir ./{dirs[0]}/')
        host.send(f'tar -xvf {dirs[0]}.tar -C ./{dirs[0]}/')
        host.send(f'rm {dirs[0]}.tar')
        host.send(f'cd /home/{username}/renren')
        host.send('kill -9 $(lsof -i:4328 -t)')
        host.send(f'rm -rf {dirs[0]}/')
        host.send(f'mv ../{dirs[0]}/ ./')
        host.send(f'cd {dirs[0]}/')
        host.send('cp ../configs/application-dev.yml ./src/main/resources/')
        host.send('mvn package -Dmaven.test.skip=true')
        host.send('nohup java -jar ./target/cmms.jar > cmms.log 2>&1 &')
    host.close()


def clear_cwd():
    path = os.path.join(os.getcwd(), 'projects')
    dirs = os.listdir(path)
    for i in dirs:
        if os.path.exists(os.path.join(path,i)):
            shutil.rmtree(os.path.join(path,i), onerror=readonly_handler)
    if os.path.exists(path):
        os.rmdir(path)


def main():
    while True:
        option = input("\r1.部署前端\n2.部署后端\n3.部署全部\n4.下载后端日志\n5.退出\n请输入您要执行的操作：")
        if option == '4':
            os.system("cls")
            download_log(api_url, ip, username, password)
            sleep(1.5)
            os.system("cls")
        elif option not in ['1','2','3','5']:
            os.system("cls")
            print("输入有误，请重新输入！")
            sleep(0.7)
            os.system("cls")
        else:
            break
    if option == '5':
        sys.exit(0)
    if option != '2':
        filename = download(h5_url, h5_branch)
        upload_file(filename, ip, username, password)
    if option != '1':
        filename = download(api_url, api_branch)
        upload_file(filename, ip, username, password)
    deploy(option, ip, username, password)
    clear_cwd()
    print("部署完毕！")
    os.system('pause')


if __name__ == '__main__':
    h5_url = 'http://gitlab.galaiot.cn:10080/chenxiaoxiang/jeast-admin-h5.git'
    api_url = 'http://gitlab.galaiot.cn:10080/sushaohua/fast-project-api.git'
    h5_branch = 'master'
    api_branch = 'master'
    ip = '192.168.1.207'
    username = 'zkwh'
    password = 'zkwh216'
    main()
