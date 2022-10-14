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

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='git_push.py',
                    filemode='a')


def auto_push():
    try:
        dirfile = os.path.abspath(r'D:\dev_projects\github\testing_auto_push')
        logging.info(msg=dirfile)
        with open(file=os.path.join(dirfile, 'auto_commit.log'), mode='a', encoding='utf-8') as file:
            file.write(str(datetime.now()))
            file.write('\n')
        file.close()
        repo = Repo(path=dirfile)
        g = repo.git
        g.add("--all")
        g.commit("-m auto commit")
        g.push()
        logging.info(msg=f'')
    except Exception as error:
        logging.error(msg=error)
    
    
if __name__ == '__main__':
    print(os.path.abspath(r'D:\dev_projects\github\testing_auto_push'))
    auto_push()

