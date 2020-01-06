# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-06 20:26:19
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-06 20:34:01

# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上再想吃时，见只剩下一个桃子了。求第一天共摘了多少。


def run():
    x = 1
    for i in range(9):
        x = (x+1)*2

    print("第一天共摘了%d个桃子" % x)


if __name__ == "__main__":
    run()
