# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-02 22:26:22
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-02 22:39:17

# 输入三个整数x,y,z，请把这三个数由小到大输出

def function(x, y, z):

    if x>y:
        x, y = y, x  # x存放较小数
    if x>z:
        x, z = z, x  # x存放最小数
    if y>z:
        y, z = z, y

    return x, y, z

def run():

    x, y, z = input("请输入三个整数x,y,z：（使用,隔开）\n").split(",") 
    print("有小到大排序如下：")
    l = function(int(x), int(y), int(z))
    for i in l:
        print(i, end="  ")


if __name__ == '__main__':
    run()