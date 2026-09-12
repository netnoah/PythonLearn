# -*- coding: utf-8 -*-
# ============================================================
# 第 5 课 挑战题：用循环重画彩虹 🌈
# 第 4 课画彩虹写了 6 遍很像的代码，现在一个循环搞定！
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import turtle

turtle.setup(800, 600)
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("skyblue")

print("挑战：用循环重画彩虹！")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.pensize(12)

# 一圈一圈画：半径从 130 开始，每圈小 14
for i in range(6):
    r = 130 - i * 14          # 第 i 圈的半径
    t.penup()
    t.goto(-r, 0)
    t.pendown()
    t.setheading(90)
    t.pencolor(colors[i])     # 第 i 圈用第 i 种颜色
    t.circle(-r, 180)

turtle.done()

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 画正十边形、正十二边形：
#    只改 demo.py 里的 sides 一个数字就行
#
# 2. 六角星 / 八角星：
#    把画星的 144 这个数字改成别的，看看会变成什么样
#
# 3. 旋转的花朵：
#    每画一个小正方形，就把整个海龟转 20 度，转一圈
#    （提示：外面套一个大循环 range(18)，里面再套画正方形的小循环）
#
# 4. 螺旋变形：
#    把 right(91) 改成 89、100、120……看看形状怎么变
#
# 5. 终极挑战：把"循环彩虹"和"螺旋"组合成一幅自己的画
