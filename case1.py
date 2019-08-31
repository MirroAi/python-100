# -*- coding: utf-8 -*-

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

def case1():
    '''使用数字，每种语言都可以用'''
    l = []  

    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                # print('a =', a, 'b =', b, 'c =', c)
                if (a != b) & (b != c) & (a != c):
                # if a != b and b != c and a != c:
                    x = a*100 + b*10 + c
                    l.append(x)
                    # print(x)  

    print('总共能组成%d个符合条件的三位数'%len(l), '分别是：')
    for i in l:
        print(i)

def case2():
    '''使用字符串特性'''
    l = []

    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                if a != b and b != c and a != c:
                    l.append(str(a) + str(b) + str(c))

    print('总共能组成%d个符合条件的三位数'%len(l), '分别是：')
    for i in l:
        print(i)

def run():
    case1()
    case2()


if __name__ == '__main__':
    run()