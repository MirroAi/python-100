# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 21:50:37
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 21:56:02

# 列表排序及连接


def run():

    l1 = []
    for i in input("请输入数组1，如1,2,3,4：").split(","):
        l1.append(int(i))

    l2 = []
    for i in input("请输入数组2：").split(","):
        l2.append(int(i))

    print("数组1排序后为", sorted(l1))
    print("数组2排序后为", sorted(l2))
    print("数组1、数组2连接后为", l1+l2)


if __name__ == "__main__":
    run()
