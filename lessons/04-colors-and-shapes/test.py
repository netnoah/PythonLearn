# -*- coding: utf-8 -*-
# ============================================================
# 第 4 课：给世界涂上颜色
# 学：颜色 pencolor / bgcolor、抬笔落笔 penup / pendown、
#     填充 begin_fill / end_fill
# 作品：先练习画彩色图形，再画一道彩虹和一座小房子
#
# 运行方法：命令行进入本文件夹，输入  python demo.py
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import turtle

turtle.setup(800, 600)   # 把画画窗口调大一点（宽 800、高 600）

t = turtle.Turtle()
t.speed(6)
# 先把"背景"刷成天空蓝
turtle.bgcolor("skyblue")

print("小海龟要给世界涂上颜色啦！")

# ============================================
# 今天的新本领：
#   t.pencolor("颜色")       换笔画（线）的颜色
#   t.penup() / t.pendown()  抬笔 / 落笔
#   t.begin_fill() / t.end_fill()  开始填充 / 结束填充
# ============================================

# ---------- 本领 1：换颜色，画一个红色的正方形 ----------
# t.pencolor("red")      # 把笔换成红色
# t.forward(30)         # 门宽 30
# t.left(90)
# t.forward(50)         # 门高 50
# t.left(90)
# t.forward(30)
# t.penup()
# t.forward(50)
# t.left(90)
# t.forward(30)         # 门宽 30
# t.left(90)
# t.forward(50)         # 门高 50
# t.left(90)
# t.pendown()
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(30)         # 门宽 30
# t.left(90)
# t.forward(50)         # 门高 50
# t.left(90)
# t.forward(30)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(150)
# t.fillcolor("gold")
# t.begin_fill()            # 开始装颜料
# t.forward(120)
# t.left(120)
# t.forward(120)
# t.left(120)
# # t.pensize(110)
# t.forward(120)
# t.left(120)
# t.end_fill()


# t.forward(150)
# t.pencolor("blue")
# t.begin_fill()  
# t.fillcolor("gold")              # 结束：三角形被涂满了！
# t.circle(50)
# t.end_fill()

a=12
b=150
c=b*2-a
t.pencolor("red")
t.pensize(a)
# t.setheading(90)
t.left(90)
t.circle(b,180)

t.pencolor("orange")
t.left(90)
t.penup()
t.forward(c)
t.pendown()
t.left(90)
t.circle(b-a,180)

t.pencolor("yellow")
t.left(90)
t.penup()
t.forward(c-a*2)
t.pendown()
t.left(90)
t.circle(b-a*2,180)


















# 画完了！让窗口不关闭
turtle.done()