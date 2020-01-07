# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 20:52:10
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 21:19:53

# 请输入星期几的第一个字母来判断一下是星期几。如果第一个字母一样，则继续判断第二个字母


def run():

    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

    l = weekdays

    for i in range(3):
        t = input("请输入第%d个字母：" % (i+1))
        sel = []
        for j in l:
            if t.lower() == j[i].lower():
                sel.append(j)
        # print(sel)

        if len(sel) == 1:
            print("输入的是："+sel[0])
            break

        l = sel


if __name__ == "__main__":
    run()
