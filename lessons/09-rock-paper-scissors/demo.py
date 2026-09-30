# -*- coding: utf-8 -*-
# ============================================================
# 第 9 课：更多选择（elif）
# 学：elif 多分支判断 + and（而且）
# 作品：和电脑玩石头剪刀布
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

print("更多选择！")

# ============================================
# 复习：if / else 只能"二选一"（第 8 课）
# 新本领：elif = "再不然如果"，能加第 3、第 4……个分支
# ============================================

# ---------- 1. 用 elif 给分数评级（3 个分支）----------
score = int(input("输入一个分数（0~100）："))

if score >= 90:
    print("优秀！⭐⭐⭐")
elif score >= 60:
    print("及格 ⭐")
else:
    print("还要加油哦 💪")

# ---------- 2. 石头剪刀布 ----------
print()
print("=== 石头剪刀布 ===")
print("1=石头  2=剪刀  3=布")

computer = random.randint(1, 3)          # 电脑随机出（第 6 课）
player = int(input("你出哪个？（1 / 2 / 3）："))

# 把数字"翻译"成名字（顺便再练一次 if / elif / else）
if computer == 1:
    computer_name = "石头"
elif computer == 2:
    computer_name = "剪刀"
else:
    computer_name = "布"

if player == 1:
    player_name = "石头"
elif player == 2:
    player_name = "剪刀"
else:
    player_name = "布"

print("你出", player_name, "，电脑出", computer_name)

# 判断输赢：and 表示"而且"，两个条件都要满足
if player == computer:
    print("平局！")
elif player == 1 and computer == 2:      # 石头砸剪刀
    print("你赢啦！🎉")
elif player == 2 and computer == 3:      # 剪刀剪布
    print("你赢啦！🎉")
elif player == 3 and computer == 1:      # 布包石头
    print("你赢啦！🎉")
else:
    print("电脑赢啦，再来一局！")
