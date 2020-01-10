# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 11:41:47
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 11:44:43

# 输入3个数a, b, c，按大小顺序输出


def run():

    a = int(input("请输入a："))
    b = int(input("请输入b："))
    c = int(input("请输入c："))

    l = [a, b, c]

    print("从小到大输出为：", sorted(l, reverse=False))


if __name__ == "__main__":
    run()
