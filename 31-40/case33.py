# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 21:24:50
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 21:27:25

# 按逗号分隔列表


def run():

    l = [1, 2, 3, 4, 5, 6, 7, 8]
    print(l)

    for i in range(len(l)):
        if i == len(l)-1:
            print(l[i])
        else:
            print(l[i], end=", ")


if __name__ == "__main__":
    run()
