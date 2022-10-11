# coding: utf8
""" 
@File: mobile.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/11 14:27
"""

a = b = c = d = e = f = 0
init_m = f'137{a}{b}{c}{d}{e}{f}98'
for aa in range(10):
    for bb in range(10):
        for cc in range(10):
            for dd in range(10):
                for ee in range(10):
                    for ff in range(10):
                        init_m = f'137{aa}{bb}{cc}{dd}{ee}{ff}98'
                        # print(init_m)
                        with open(file='./m.txt', mode='a', encoding='utf-8') as m:
                            m.write(init_m)
                            m.write('\n')
                        # break
                    # break
                # break
            # break
        # break
    # break
m.close()
