# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-06 20:35:17
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-06 20:42:20

# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程找出三队赛手的名单


def run():

    l = ['x', 'y', 'z']

    for a in l:
        for b in l:
            for c in l:
                if a != b and b != c and a != c and a != 'x' and c != 'x' and c != 'z':
                    print('a-%s, b-%s, c-%s' % (a, b, c))


if __name__ == "__main__":
    run()
