# -*- coding: utf-8 -*-
# ============================================================
# 第 4 课 挑战题：画一个红绿灯 🚦
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import turtle

turtle.setup(600, 700)
t = turtle.Turtle()
t.speed(6)
turtle.bgcolor("skyblue")

print("挑战：画一个红绿灯！")

# ---------- 灯柱（一个灰色长方形，涂满）----------
t.penup()
t.goto(-30, -300)
t.pendown()
t.pencolor("gray")
t.fillcolor("gray")
t.begin_fill()
t.forward(60)     # 宽 60
t.left(90)
t.forward(100)    # 高 100
t.left(90)
t.forward(60)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

# ---------- 灯箱（一个深色大长方形）----------
t.penup()
t.goto(-70, -200)
t.pendown()
t.pencolor("black")
t.fillcolor("dimgray")
t.begin_fill()
t.forward(140)    # 宽 140
t.left(90)
t.forward(280)    # 高 280
t.left(90)
t.forward(140)
t.left(90)
t.forward(280)
t.left(90)
t.end_fill()

# ---------- 三个灯（三个圆，红黄绿）----------
# t.circle(半径) 会画一个整圆；配合填充就是一个"灯泡"

# 红灯（最上面）
t.penup()
t.goto(0, 40)      # 圆心位置
t.pendown()
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.circle(40)
t.end_fill()

# 黄灯（中间）
t.penup()
t.goto(0, -60)
t.pendown()
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# 绿灯（最下面）
t.penup()
t.goto(0, -160)
t.pendown()
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.circle(40)
t.end_fill()

turtle.done()

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 画一面彩色旗帜：一个长方形，边框一种颜色，里面另一种颜色
#
# 2. 画一朵彩色小花：
#    用 5~6 个填充的小圆围成一圈，每个圆颜色不一样
#    （提示：每画完一个圆，就转 360 ÷ 5 或 360 ÷ 6 度）
#
# 3. 给 demo.py 的小房子加一扇"窗户"：
#    一个小正方形，涂成浅蓝色，放在门的上方
#
# 4. 把红绿灯改成"躺着"的，或换一组你喜欢的颜色
#
# 5. 终极挑战：画一道"双彩虹"——
#    在原来的彩虹外面，再套一圈更淡的颜色
