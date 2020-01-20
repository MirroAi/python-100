# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 18:18:47
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 18:21:24

# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止


def run():

    while True:
        text = input("请输入需要保存的字符，输入#则结束：")
        if text == "#":
            break
        else:
            with open("case97.txt", "a") as f:
                f.write(text)


if __name__ == "__main__":
    run()
