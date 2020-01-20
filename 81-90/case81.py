# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-12 11:58:43
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 16:46:24

# 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。


def run():

    x = 0
    y = 0

    for i in range(10, 100):
        if len(str(i * 809)) == 4 and len(str(i * 8)) == 2 and len(str(i * 9)) == 3 and 809 * i == 800*i + 9*i:
            x = i

    y = 809 * x

    print("??代表的两位数是 %d\n809 * ?? = %d" % (x, y))


if __name__ == "__main__":
    run()
