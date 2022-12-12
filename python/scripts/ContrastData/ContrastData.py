# coding: utf8
"""
@File: ContrastData.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/22 14:50
"""

import os, datetime
from tqdm import tqdm

def compare(src_path, aim_path):
    if os.path.isdir(src_path) and os.path.isdir(aim_path):
        try:
            aim_file_name_list =[os.path.splitext(data)[0] for data in os.listdir(aim_path)]
            with tqdm(total=len(os.listdir(src_path))) as pbar:
                for src_file in os.listdir(src_path):
                    if src_file in aim_file_name_list:
                        pass
                    else:
                        with open(file='compare.txt', mode='a+', encoding='utf-8') as file_compare:
                            file_compare.write('{}\n'.format(src_file))
                            file_compare.close()
                    pbar.update(1)
        except Exception as error:
            with open(file='error.txt', mode='a+', encoding='utf-8') as file_error:
                file_error.write('{}\t{}\n'.format(datetime.datetime.now(), error))
                file_error.write('{}\n'.format('-' * 50))
                file_error.close()
            print(error)


if __name__ == '__main__':
    src_path = r'D:\develops\DefaultSpace\AliceProjects\analysis_radar\data\source'
    aim_path = r'D:\develops\DefaultSpace\AliceProjects\analysis_radar\data\images'
    compare(src_path=src_path, aim_path=aim_path)
