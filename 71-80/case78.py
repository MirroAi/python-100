# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-12 11:15:27
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-12 11:20:38

# 找到年龄最大的人，并输出


def run():

    person_age = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    max_age = 0

    for k, v in person_age.items():
        if v > max_age:
            name, max_age = k, v

    print("年龄最大的人是%s，年龄为%d" % (name, max_age))


if __name__ == "__main__":
    run()
