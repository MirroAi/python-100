# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 16:55:01
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 17:03:15

# 求0到7能组成的奇数个数，每个数字只能使用一次


def run():

    count = 0
    for i in range(1, 9):  # 最多可组成8位数
        if i == 1:
            count += 4
        elif i == 2:
            count += 7*4
        else:
            count += 7*(8**(i-2))*4

    print("能组成 %d 个奇数" % count)


if __name__ == "__main__":
    run()
