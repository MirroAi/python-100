# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 16:41:06
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 17:35:03


# 求100以内的素数

def run():

    l = []

    for i in range(2, 100+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            l.append(i)

    print(l)


if __name__ == '__main__':
    run()
