# coding: utf8
""" 
@File: CSVMerge.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/30 23:28
"""

import pandas
import pathlib
import glob
import os


def csv_marge_main():
    areas_list: list = ['chenghua', 'gaoxin7', 'jinniu', 'qingyang', 'jinjiang', 'tianfuxinqu', 'wuhou', ]
    areas_dict: dict = {}
    for area in areas_list:
        areas_dict.update([(f'{area}', None)])
    csv_work_dir = pathlib.Path(r'D:\downloads\20220928')
    csv_files = csv_work_dir.glob(r'**/*.csv')
    # chenghua_numbers = gaoxin7_numbers = jinniu_numbers = qingyang_numbers = jinjiang_numbers = 0
    chenghua_numbers: int = 0
    gaoxin7_numbers: int = 0
    jinniu_numbers: int = 0
    qingyang_numbers: int = 0
    jinjiang_numbers: int = 0
    tianfuxinqu_numbers: int = 0
    wuhou_numbers: int = 0
    for csv_file in csv_files:
        file_name, file_ext = os.path.splitext(csv_file)
        for area in areas_list:
            var = f'{area}_numbeers'
            exec (var + '=%i' % 0)
            if area in file_name:
                    read_file = pandas.read_csv(csv_file, sep=',', encoding='GB18030')
                    if area == 'chenghua':
                        chenghua_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', chenghua_numbers)])
                    elif area == 'gaoxin7':
                        gaoxin7_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', gaoxin7_numbers)])
                    elif area == 'jinniu':
                        jinniu_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', jinniu_numbers)])
                    elif area == 'qingyang':
                        qingyang_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', qingyang_numbers)])
                    elif area == 'jinjiang':
                        jinjiang_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', jinjiang_numbers)])
                    elif area == 'tianfuxinqu':
                        tianfuxinqu_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', tianfuxinqu_numbers)])
                    elif area == 'wuhou':
                        wuhou_numbers += len(read_file.index) + 1
                        areas_dict.update([(f'{area}', wuhou_numbers)])
                    else:
                        print(csv_file)
    print(areas_dict)


if __name__ == '__main__':
    csv_marge_main()
