# -*- coding: utf-8 -*-
# ============================================================
# 第 3 课：小海龟登场
# 学：import turtle、前进/后退、左转/右转
# 用海龟画出正方形和三角形
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

# 把"海龟"工具箱拿来，这样才能指挥海龟
import turtle

# 造一只小海龟，起名叫 t（t 是 turtle 的缩写）
t = turtle.Turtle()

# 海龟走路的速度：1 最慢，10 最快，这里用 5 刚刚好
t.speed(5)

print("小海龟要开始画画啦！")

# ============================================
# 海龟会听这 4 个命令：
#   t.forward(100)   向前走 100 步
#   t.backward(100)  向后走 100 步
#   t.left(90)       向左转 90 度
#   t.right(90)      向右转 90 度
# ============================================

# ---------- 画一个正方形 ----------
# 正方形有 4 条边、4 个角
# 海龟转一圈是 360 度，360 ÷ 4 = 90，所以每个角转 90 度
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# ---------- 再画一个三角形 ----------
# 三角形有 3 条边、3 个角
# 360 ÷ 3 = 120，所以每个角转 120 度
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)

# 画完了！这行让窗口不关闭，等我们慢慢看
turtle.done()
