# -*- coding: utf-8 -*-
# ============================================================
# 第 5 课：循环的魔法
# 学：for 循环 + range，把重复的代码变短
# 作品：正方形 → 多边形 → 五角星 → 炫酷螺旋
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

turtle.setup(800, 600)
t = turtle.Turtle()
t.speed(0)              # 0 = 最快（瞬间画完）；改成 1~10 可以慢慢看它爬

turtle.bgcolor("skyblue")

print("循环的魔法开始啦！")

# ============================================
# 今天的新本领：for 循环
#   for i in range(4):   意思是"重复做 4 次"
#   下面"缩进"的代码（前面有空格的），会被执行 4 遍
# ============================================

# ---------- 1. 用循环画正方形 ----------
# 第 3 课画正方形写了 8 行，现在 3 行就搞定！
t.penup()
t.goto(-280, -50)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)

# ---------- 2. 多边形生成器 ----------
# 还记得"360 ÷ 边数 = 转角"吗？现在几边形都能画！
# 把 sides 改成 5、8、12……试试看
t.penup()
t.goto(-60, -40)
t.pendown()

sides = 6              # 想画几边形，就把这里改成几
t.pencolor("darkgreen")
t.fillcolor("lightgreen")
t.begin_fill()
for i in range(sides):
    t.forward(80)
    t.left(360 / sides)
t.end_fill()

# ---------- 3. 五角星 ----------
# 星形的秘密：每次转 144 度，转 5 次
# 5 × 144 = 720 = 整整两圈，所以海龟"绕两圈"画出一颗星
t.penup()
t.goto(130, -40)
t.pendown()
t.pencolor("gold")
t.pensize(3)
for i in range(5):
    t.forward(150)
    t.right(144)
t.pensize(1)

print("画完了！擦掉，看压轴大作：炫酷螺旋")

# ---------- 擦掉练习 ----------
t.clear()             # 把刚才的都擦掉（背景色还在）

# ---------- 4. 炫酷螺旋（压轴）----------
# for 循环的 i 每圈会变：0, 1, 2, 3, ...
# 让"前进的距离"跟着 i 变大，线就越画越长，转成螺旋
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(3)

for i in range(100):
    t.pencolor(colors[i % 6])   # i % 6 = "i 除以 6 的余数"，让颜色循环用
    t.forward(i * 2)            # i 越大，走得越远
    t.right(91)                 # 转 91 度（比 90 多 1 度，所以慢慢旋开）

# 画完了！让窗口不关闭
turtle.done()
