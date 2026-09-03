# -*- coding: utf-8 -*-
# ============================================================
# 第 3 课 挑战题：画更多的图形
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import turtle

t = turtle.Turtle()
t.speed(5)

print("挑战开始！先画一个长方形")

# ---------- 长方形：两条长边 150，两条短边 80 ----------
t.forward(150)
t.right(90)
t.forward(80)
t.right(90)
t.forward(150)
t.right(90)
t.forward(80)
t.right(90)

turtle.done()

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 画一个五边形：
#    五边形有 5 条边、5 个角，360 ÷ 5 = 72，所以每次转 72 度
#
# 2. 画一个六边形：
#    六边形有 6 条边，360 ÷ 6 = 60，所以每次转 60 度
#
# 3. 画一座小房子：
#    正方形（墙）+ 三角形（屋顶）拼在一起
#
# 4. 试试把速度改成 t.speed(1)：
#    看海龟慢慢爬、一笔一笔地画，是不是很有意思？
#
# 5. 终极挑战：画一个"风车"——
#    画 4 个三角形，每个转 90 度围成一圈
