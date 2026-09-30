# -*- coding: utf-8 -*-
# ============================================================
# 第 7 课：图案生成器（综合复习小项目 🎯）
# 复习：turtle（第 3 课）+ 颜色（第 4 课）+ for 循环（第 5 课）+ 随机（第 6 课）
# 作品：曼陀罗花纹 + 雪花
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
import random

turtle.setup(800, 600)
t = turtle.Turtle()
t.speed(0)

turtle.bgcolor("midnightblue")   # 深蓝背景，花纹更醒目

print("图案生成器启动！")

# ---------- 图案 1：曼陀罗花纹 ----------
# 画一个圆，转一点点，再画一个……转满一圈，就"转"出了一朵花
# 关键：times（画几个）决定角度 360 ÷ times
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

times = 100            # ← 改成 12、18、24、72……花纹完全不一样
angle = 360 / times   # 每次转的角度，正好转满一圈

for i in range(times):
    t.pencolor(random.choice(colors))   # 随机颜色（第 6 课）
    t.circle(120)                       # 画一个圆（第 4 课）
    t.right(angle)                      # 转一点（第 3 课）

print("曼陀罗画好了！擦掉，画雪花")

t.clear()             # 擦掉（背景还在）

# # ---------- 图案 2：雪花 ----------
# # 一条"臂"：主干 + 两个小分叉；重复 6 次（360 ÷ 6 = 60 度）
t.pencolor("white")
t.pensize(3)
times = 1000             # 每条臂转的角度
angle = 360 / times   # 每条臂转的角度


for i in range(times):
    t.forward(80)          # 主干（从中心往外）
    t.left(30)             # 左分叉
    t.forward(30)
    t.backward(30)
    t.right(60)            # 右分叉
    t.forward(30)
    t.backward(30)
    t.left(30)             # 回到主干方向
    t.backward(80)         # 回到中心
    t.right(angle)            # 转 60 度，画下一条臂


# print("雪花也画好了！")

# 画完了！让窗口不关闭
turtle.done()
