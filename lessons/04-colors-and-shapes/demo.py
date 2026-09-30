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
s = turtle.Turtle()
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
t.pencolor("red")      # 把笔换成红色
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# ---------- 本领 2：抬笔！走到旁边，不留线 ----------
t.penup()              # 抬笔：下面怎么走都不留线
t.forward(150)         # 走到右边一点
t.pendown()            # 落笔：又能画画了

t.pencolor("blue")     # 换成蓝色，再画一个正方形
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# ---------- 本领 3：填充！给三角形装满颜色 ----------
t.penup()
t.forward(150)         # 再挪到旁边，别和正方形重叠
t.pendown()

t.pencolor("darkorange")  # 边框用深橙色
t.fillcolor("gold")       # 里面涂金黄色

t.begin_fill()            # 开始装颜料
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.end_fill()              # 结束：三角形被涂满了！

print("练习完成！擦掉，画一个大作品：彩虹 + 小房子")

# ---------- 擦掉练习，开始画大作 ----------
t.clear()             # 把刚才的画都擦掉（背景色还在）

# ============ 大作 1：彩虹 ============
# 彩虹是一圈一圈的半圆，从外圈的红色画到内圈的紫色
# t.circle(半径, 180) 会画"半个圆"；半径越小，半圆越小
t.pensize(12)         # 笔变粗，彩虹更好看

# 最外圈 · 红
t.penup()
t.goto(-130, 0)
t.pendown()
t.setheading(90)      # 让海龟朝上，才能画出"拱桥"形状
t.pencolor("red")
t.circle(-130, 180)

# 第二圈 · 橙
t.penup()
t.goto(-116, 0)
t.pendown()
t.setheading(90)
t.pencolor("orange")
t.circle(-116, 180)

# 第三圈 · 黄
t.penup()
t.goto(-102, 0)
t.pendown()
t.setheading(90)
t.pencolor("yellow")
t.circle(-102, 180)

# 第四圈 · 绿
t.penup()
t.goto(-88, 0)
t.pendown()
t.setheading(90)
t.pencolor("green")
t.circle(-88, 180)

# 第五圈 · 蓝
t.penup()
t.goto(-74, 0)
t.pendown()
t.setheading(90)
t.pencolor("blue")
t.circle(-74, 180)

# 最内圈 · 紫
t.penup()
t.goto(-60, 0)
t.pendown()
t.setheading(90)
t.pencolor("purple")
t.circle(-60, 180)

# ============ 大作 2：小房子（在彩虹下面）============
t.pensize(3)          # 笔变回细一点，画房子更精致

# 墙壁：一个淡黄色的正方形，填满颜色
t.penup()
t.goto(-60, -170)     # 房子的左下角
t.pendown()
t.pencolor("sandybrown")
t.fillcolor("wheat")
t.begin_fill()
t.forward(120)        # 底边
t.left(90)
t.forward(90)         # 右边
t.left(90)
t.forward(120)        # 顶边
t.left(90)
t.forward(90)         # 左边
t.left(90)
t.end_fill()

# 屋顶：一个红色的三角形，盖在墙上面
t.penup()
t.goto(-70, -80)      # 屋顶比墙宽一点，从墙的左上角再往左一点开始
t.pendown()
t.pencolor("firebrick")
t.fillcolor("red")
t.begin_fill()
t.forward(140)        # 屋顶底边
t.left(120)
t.forward(140)        # 左边斜边
t.left(120)
t.forward(140)        # 右边斜边
t.left(120)
t.end_fill()

# 门：一个棕色的小长方形
t.penup()
t.goto(-15, -170)     # 门在墙的中间靠下
t.pendown()
t.pencolor("saddlebrown")
t.fillcolor("saddlebrown")
t.begin_fill()
t.forward(30)         # 门宽 30
t.left(90)
t.forward(50)         # 门高 50
t.left(90)
t.forward(30)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

# 画完了！让窗口不关闭
turtle.done()
