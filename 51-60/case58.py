# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 21:37:34
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 21:39:12

# 画图，画方形

import turtle


def run():

    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.goto(50, -50)
    turtle.goto(50, 50)
    turtle.goto(-50, 50)
    turtle.goto(-50, -50)

    turtle.mainloop()


if __name__ == '__main__':
    run()
