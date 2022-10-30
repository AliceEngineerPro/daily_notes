# coding: utf8
""" 
@File: git_push.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/14 18:34
"""

from git import Repo
import os
from datetime import datetime
import logging
import time
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
    datefmt='%a %d %b %Y %H:%M:%S',
)


def auto_push():
    try:
        repo_path = os.path.abspath(r'D:\dev_projects\github\testing_auto_push')
        auto_path = f'{repo_path}/AutoCommit'
        if not os.path.exists(auto_path):
            os.makedirs(auto_path)
        logging.info(msg=f'Local path ==>{repo_path}')
        data_date = f'{datetime.today().year}-{datetime.today().month}-{datetime.today().day}'
        data_time = f'{datetime.today().hour}:{datetime.today().minute}:{datetime.today().second}'
        with open(
                file=f'{auto_path}/{data_date}.py',
                mode='a',
                encoding='utf-8'
        ) as file:
            logging.info(file.name)
            file.write(f'print(f"AutoCommitDateTime: {time.asctime()}")')
            file.write('\n')
        file.close()
        repo = Repo(path=repo_path)
        g = repo.git
        g.add("--all")
        g.commit("-m auto commit")
        g.push()
        logging.info(msg=f'Submitted successfully.')
    except Exception as error:
        logging.error(msg=error)


if __name__ == '__main__':
    while True:
        # auto_push()
        # time_delay = random.randint(1,10)
        # print(time_delay)
        # time.sleep(time_delay)
        print('done')
        
        
