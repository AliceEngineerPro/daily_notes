# coding: utf8
""" 
@File: move_file.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/5 14:35
"""

import os
import pathlib
import shutil

path = pathlib.Path(r'D:\dev_project\data\folder')
new_path = r'D:\dev_project\data'
files_path = path.glob('**/*')
count_file = 0
for file in files_path:
    if os.path.isdir(file):
        pass
    elif os.path.isfile(file):
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            try:
                shutil.move(file, new_path)
                print(rf'移动文件 {file} 到 {new_path}')
                count_file += 1
            except Exception as error:
                print(error)
                break
print(f'移动文件数量: {count_file}')

