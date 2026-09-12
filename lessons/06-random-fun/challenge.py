# -*- coding: utf-8 -*-
# ============================================================
# 第 6 课 挑战题：画一片属于自己的星空 🌌
# 加一个月亮，再多画一些星星
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import turtle
import random

turtle.setup(800, 600)
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")       # 换成纯黑夜空

# ---------- 先画一个大月亮（右上角）----------
t.penup()
t.goto(255, 150)
t.pendown()
t.pencolor("lightyellow")
t.fillcolor("lightyellow")
t.begin_fill()
t.circle(55)
t.end_fill()

# ---------- 再画 100 颗随机星星 ----------
star_colors = ["white", "gold", "yellow", "lightblue", "lightcyan", "ivory", "silver"]

for i in range(100):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    size = random.randint(1, 8)
    t.penup()
    t.goto(x, y)
    t.dot(size, random.choice(star_colors))

print("你的星空画好了！")

turtle.done()

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 随机彩色多边形（结合第 5 课的循环）：
#    随机边数 + 随机颜色 + 随机位置，画 10 个不一样的多边形
#
# 2. 一颗流星：用一条斜线划过天空
#    （提示：penup 到起点，pendown，再 goto 到另一个点）
#
# 3. 换夜空颜色：把 bgcolor 改成 navy、darkslateblue、midnightblue 看看
#
# 4. 猜数字小游戏（预告第 8 课 if）：
#    random.randint(1, 10) 出一个数，再用 input 让玩家猜
#
# 5. 终极挑战：夜空 + 月亮 + 星星 + 一座小房子（复习第 4 课）
