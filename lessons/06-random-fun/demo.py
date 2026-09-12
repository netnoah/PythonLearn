# -*- coding: utf-8 -*-
# ============================================================
# 第 6 课：随机大冒险
# 学：import random、randint、choice，让程序"随机"
# 作品：一片璀璨星空
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
import random               # 把"随机工具箱"拿来

turtle.setup(800, 600)
t = turtle.Turtle()
t.speed(0)

turtle.bgcolor("midnightblue")   # 深夜的深蓝夜空

print("随机大冒险开始啦！")

# ============================================
# 今天的新本领：
#   random.randint(a, b)   在 a~b 之间随机挑一个整数（含两端）
#   random.choice(列表)    从列表里随机挑一个
# ============================================

# ---------- 1. 掷骰子：random.randint ----------
# 骰子有 1 到 6 六个面，我们"随机"掷 3 次
print("掷 3 次骰子（1~6）：")
for i in range(3):
    print(random.randint(1, 6))

# ---------- 2. 随机抽颜色：random.choice ----------
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
print("随机抽 3 个颜色：")
for i in range(3):
    print(random.choice(colors))

# ---------- 3. 璀璨星空：循环 + 随机 ----------
# 星星的颜色：白、金、黄、浅蓝、淡青、米白
star_colors = ["white", "gold", "yellow", "lightblue", "lightcyan", "ivory"]

for i in range(60):
    x = random.randint(-380, 380)       # 随机左右位置
    y = random.randint(-280, 280)       # 随机上下位置
    size = random.randint(2, 9)         # 随机大小（直径）
    color = random.choice(star_colors)  # 随机颜色

    t.penup()
    t.goto(x, y)
    t.dot(size, color)                  # 画一颗实心"星星"

print("星空画好了！每次运行都不一样哦！")

# 画完了！让窗口不关闭
turtle.done()
