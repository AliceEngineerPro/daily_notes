# coding: utf8
"""
@File: AR2RadarUnzip.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/21 14:26
"""

import glob, os, re, bz2
from datetime import datetime


def unzip_bz2(path):
    file_list = glob.glob(pathname=r'{}\**\*'.format(path), recursive=True)
    for file in file_list:
        try:
            if os.path.isdir(file):
                raise Exception('目录: {}'.format(file))
            elif os.path.isfile(file):
                file_path = re.findall(r'.+\\', file)[0]
                file_name, file_ext = os.path.splitext(re.findall(r'[^\\]+', file)[-1])
                if file_ext == '.bz2':
                    new_name = '{}Z_RADR_I_{}_{}{}_{}.BIN'.format(
                        file_name.split('.')[0][:-5],
                        file_name.split('.')[0][-5:],
                        file_name.split('.')[1],
                        file_name.split('.')[2],
                        file_name.split('.')[3],
                    )
                    try:
                        with open(file='{}{}'.format(file_path, new_name), mode='wb') as file_new, bz2.BZ2File(filename=file, mode='rb') as file_unzip:
                            for data in iter(lambda: file_unzip.read(100 * 1024), b''):
                                file_new.write(data)
                        file_new.close()
                        file_unzip.close()
                        with open(file='access.txt', mode='a+', encoding='utf-8') as file_access:
                            file_access.write('{}\t{}解压完成\n'.format(datetime.now(), file))
                        file_access.close()
                        print('{}\t{}解压完成\n'.format(datetime.now(), file))
                    except Exception as error:
                        with open(file='error.txt', mode='a+', encoding='utf-8') as file_error:
                            file_error.write('{}\t{}\n'.format(datetime.now(), file))
                            file_error.write('{}\n'.format(error))
                            file_error.write('{}\n'.format('-' * 50))
                        file_error.close()
                        pass
        except Exception as error:
            with open(file='error.txt', mode='a+', encoding='utf-8') as file_error:
                file_error.write('{}\t{}\n'.format(datetime.now(), file))
                file_error.write('{}\n'.format(error))
                file_error.write('{}\n'.format('-' * 50))
            file_error.close()
            pass


if __name__ == '__main__':
    p = r'D:\develops\DefaultSpace\AliceProjects\analysis_radar\test_data\1'
    unzip_bz2(path=p)
