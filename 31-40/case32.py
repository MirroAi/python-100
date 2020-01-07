# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 21:20:56
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 21:23:33

# 按相反的顺序输出列表的值


def run():

    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("逆序输出为：")
    for i in s[::-1]:
        print(i, end=" ")


if __name__ == "__main__":
    run()
