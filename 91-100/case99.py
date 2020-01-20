# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 18:27:42
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 18:34:50

# 有两个磁盘文件A.txt和B.txt，各存放了一行字母，要求把这两个文件中的信息合并按字母顺序排列，输出到新文件C.txt中


def run():

    with open("A.txt", "r") as f:
        text1 = f.read()
    with open("B.txt", "r") as f:
        text2 = f.read()
    print("A.txt中内容为：%s\nB.txt中内容为：%s" % (text1, text2))
    text3 = ""
    for i in sorted(text1+text2):
        text3 += i
    with open("C.txt", "w") as f:
        f.write(text3)
    with open("C.txt", "r") as f:
        print("C.txt中内容为：%s" % f.read())


if __name__ == "__main__":
    run()
