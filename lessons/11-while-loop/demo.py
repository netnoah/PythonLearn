# -*- coding: utf-8 -*-
# ============================================================
# 第 11 课：一直玩到赢（while 循环）
# 学：while 循环 —— 只要条件对，就一直重复
# 作品：升级版猜数字（反复猜 + 提示 + 计次数）
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

import random

print("一直玩到赢！")

# ============================================
# 复习：第 5 课 for 循环 —— 知道要重复几次
# 新本领：while 循环 —— 不知道几次，重复到"条件不成立"
# ============================================

# ---------- 1. 最简单的 while：数数 ----------
n = 1
while n <= 3:
    print("第", n, "次")
    n = n + 1        # ← 千万别忘！不然 n 永远是 1，程序停不下来

# ---------- 2. 升级版猜数字 ----------
# 第 8 课只能猜一次；现在用 while 反复猜，直到猜对为止
secret = random.randint(1, 100)

guess = 0    # 先放一个"肯定不对"的数，让循环先跑起来
times = 0    # 记录猜了几次

while guess != secret:
    guess = int(input("猜一个 1~100 的数字："))
    times = times + 1

    if guess > secret:
        print("太大了，往小猜！")
    elif guess < secret:
        print("太小了，往大猜！")
    else:
        print("猜对啦！🎉")

print("你一共猜了", times, "次")

# ---------- 3. 按次数评级 ----------
if times <= 5:
    print("太厉害了，猜数高手！👑")
elif times <= 10:
    print("不错哦！⭐")
else:
    print("多练练会更棒！💪")
