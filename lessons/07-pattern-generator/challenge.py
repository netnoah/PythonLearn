# -*- coding: utf-8 -*-
# ============================================================
# 第 7 课 挑战题：多边形曼陀罗 🌀
# 把圆换成正方形，转着画，生成一朵"方形花"
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
turtle.bgcolor("midnightblue")

print("挑战：画一朵多边形曼陀罗！")

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

times = 18            # 画 18 个正方形
angle = 360 / times   # 每个转 20 度，正好一圈

for i in range(times):
    t.pencolor(random.choice(colors))

    # 内层循环：画一个正方形（第 5 课的循环）
    for j in range(4):
        t.forward(70)
        t.left(90)

    # 外层循环：转一点，画下一个
    t.right(angle)

print("多边形曼陀罗画好了！")

turtle.done()

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 把正方形换成三角形 / 六边形：
#    改内层循环 range(4) 成 range(3) 或 range(6)，
#    同时把 left(90) 改成 left(120) 或 left(60)
#
# 2. 更复杂的雪花：给每条臂的分叉上再加"小分叉"
#    （在 forward(30) 之后再画一个小小的 V）
#
# 3. 随机大小圆：把 demo.py 里的 circle(120) 换成
#    circle(random.randint(40, 120))，看看会变成什么
#
# 4. 把曼陀罗和雪花画在同一张画里（不擦掉，摆在不同位置）
#
# 5. 终极挑战：做一个真正的"随机图案生成器"——
#    用 random.randint 随机决定 times 和形状，每次运行都不同
