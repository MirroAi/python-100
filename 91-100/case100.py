# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 18:36:16
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 18:45:40

# 列表转换为字典


def run():

    l = ['a', 'b', 'c', 'd', 'e', 'f']
    d = dict()
    for i in range(len(l)):
        d[l[i]] = i
    print(d)


if __name__ == '__main__':
    run()
