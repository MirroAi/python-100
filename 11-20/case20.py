# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 22:20:23
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 22:34:12

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？


def function(times):
    l = []
    for i in range(times):
        l.append(100 / 2**(i))

    return l


def run():
    t = int(input("请输入想要获取第几次的数值："))
    l = function(t)
    s = 0.0
    for i in range(len(l)):
        if i == 0:
            s += l[i]
            print("它在第 %d 次落地时，共经过 %f 米" % (i+1, s))
        else:
            s += l[i] * 2
            print("它在第 %d 次落地时，共经过 %f 米；第 %d 次反弹高度为 %f 米" % (i+1, s, i, l[i]))


if __name__ == "__main__":
    run()
