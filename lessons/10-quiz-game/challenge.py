# -*- coding: utf-8 -*-
# ============================================================
# 第 10 课 挑战题：乘法小考官
# 电脑随机出 3 道乘法题，你答，最后判分
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import random

print("乘法小考官！3 道题，答对 +1 分")

score = 0

# ---------- 第 1 题 ----------
a = random.randint(1, 9)
b = random.randint(1, 9)
print(a, "×", b, "= ?")
answer = int(input("你的答案："))

if answer == a * b:
    print("答对啦！+1 分 🎉")
    score = score + 1
else:
    print("答错啦，答案是", a * b)

# ---------- 第 2 题 ----------
a = random.randint(1, 9)
b = random.randint(1, 9)
print(a, "×", b, "= ?")
answer = int(input("你的答案："))

if answer == a * b:
    print("答对啦！+1 分 🎉")
    score = score + 1
else:
    print("答错啦，答案是", a * b)

# ---------- 第 3 题 ----------
a = random.randint(1, 9)
b = random.randint(1, 9)
print(a, "×", b, "= ?")
answer = int(input("你的答案："))

if answer == a * b:
    print("答对啦！+1 分 🎉")
    score = score + 1
else:
    print("答错啦，答案是", a * b)

print()
print("你得了", score, "分（满分 3 分）")

if score == 3:
    print("满分！乘法大王！👑")
elif score >= 1:
    print("不错哦！⭐")
else:
    print("再练练乘法吧！💪")

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 改成减法题，或者除法题（除法要出能整除的：
#    先出 b 和 c，再出 a = b * c，问 a ÷ b = ?）
#
# 2. 判断大小：随机两个数，问"谁更大"
#
# 3. 3 道题写成 3 段一模一样的代码，是不是很啰嗦？
#    下一课 while 循环能帮你"重复"而不重复写！
