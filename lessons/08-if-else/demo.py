# -*- coding: utf-8 -*-
# ============================================================
# 第 8 课：如果…就…（if / else）
# 学：if / else 判断 + 比较运算符，让程序"会思考"
# 作品：猜数字小游戏
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

print("让程序会思考！")

# ============================================
# 比较运算符：程序能"比较"两个数
#   结果只有两种：对（True）或 错（False）
#   == 等于   != 不等于   > 大于   < 小于
#   >= 大于等于   <= 小于等于
# ============================================
print("比较一下：")
print("5 > 3  是", 5 > 3)     # True，对
print("5 == 3 是", 5 == 3)    # False，错
print("5 != 3 是", 5 != 3)    # True，对

# ---------- 1. if / else：两个分支 ----------
# if 后面的条件"对"，就做冒号下面的事；"不对"，就做 else 下面的事
score = 80
if score >= 60:
    print("你的分数是", score, "—— 及格啦！")
else:
    print("你的分数是", score, "—— 还要加油哦")

# ---------- 2. if 也可以单独用（没有 else）----------
n = 7
if n > 5:
    print(n, "比 5 大")

# ---------- 3. 猜数字小游戏 ----------
# 电脑随机想一个 1~10 的数字，你来猜一次
secret = random.randint(1, 10)

# int(...) 把输入的文字变成数字（input 拿到的本来是"文字"）
guess = int(input("猜一个 1~10 的数字："))

if guess == secret:
    print("猜对啦！🎉 就是", secret, "！")
else:
    print("猜错了……其实是", secret)
