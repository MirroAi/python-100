# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 20:55:55
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 21:00:00

# 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153


def run():
    l = []
    for i in range(100, 1000):
        a, b, c = int(str(i)[0]), int(str(i)[1]), int(str(i)[2])
        if i == (a**3 + b**3 + c**3):
            l.append(i)

    print(l)


if __name__ == '__main__':
    run()
