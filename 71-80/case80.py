# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-12 11:25:32
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-12 11:57:27

# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样
# 做的，问海滩上原来最少有多少个桃子？


def run():

    n = 1

    while True:

        flag = 1
        m = n/4 * 5 + 1
        if m != int(m):  # 判断每一次分配前的桃子数是否为整数
            flag = 0

        for i in range(4):
            m = m/4 * 5 + 1
            if m != int(m):  # 判断每一次分配前的桃子数是否为整数
                flag = 0

        if flag:
            print("原来至少有 %d 个桃子" % int(m))
            break
        else:
            n += 1


if __name__ == "__main__":
    run()
