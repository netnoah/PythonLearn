# -*- coding: utf-8 -*-
# ============================================================
# 第 10 课：谜题闯关 🎯（综合 if 小项目）
# 复习：input、int()、== 比较、if / elif / else、random、%
# 作品：趣味问答闯关小游戏
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

print("谜题闯关开始！")
print("答对一题得 1 分，看看你能得几分！")
print()

score = 0   # 记分牌：先放 0 分

# ---------- 第 1 关：数字题 ----------
# int(input(...)) 把输入变数字，== 比较（第 8 课）
answer = int(input("第 1 关：3 + 5 等于几？"))

if answer == 8:
    print("答对啦！+1 分 🎉")
    score = score + 1
else:
    print("答错啦，正确答案是 8")

# ---------- 第 2 关：脑筋急转弯 ----------
# 文字题：直接 input()，和字符串比（要带引号）
answer = input("第 2 关：什么东西越洗越脏？")

if answer == "水":
    print("答对啦！+1 分 🎉")
    score = score + 1
else:
    print("答错啦，答案是「水」")

# ---------- 第 3 关：数字题 ----------
answer = int(input("第 3 关：5 × 4 等于几？"))

if answer == 20:
    print("答对啦！+1 分 🎉")
    score = score + 1
else:
    print("答错啦，正确答案是 20")

# ---------- 彩蛋关：随机单双 ----------
# 电脑随机出 1~10，你猜单还是双；% 求余判单双（第 5 课 + 第 6 课）
secret = random.randint(1, 10)
guess = input("彩蛋关：我出了个 1~10 的数，你猜「单」还是「双」？")

if secret % 2 == 0:      # 能被 2 整除 = 双数
    right = "双"
else:
    right = "单"

if guess == right:
    print("猜对啦！我出的是", secret, "（", right, "） +1 分 🎉")
    score = score + 1
else:
    print("猜错啦，我出的是", secret, "（", right, "）")

# ---------- 结算 ----------
print()
print("=== 闯关结束！===")
print("你一共得了", score, "分（满分 4 分）")

# 用 elif 给最终评级（第 9 课）
if score == 4:
    print("满分通关！你是闯关大王！👑")
elif score >= 2:
    print("不错哦，继续加油！⭐")
else:
    print("再试一次，你会更棒！💪")
