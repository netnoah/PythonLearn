# -*- coding: utf-8 -*-
# ============================================================
# 第 11 课 挑战题：限次猜数字
# 最多猜 10 次，猜不中就算输
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

import random

print("限次猜数字！你只有 10 次机会")

secret = random.randint(1, 100)
guess = 0
times = 0

# while 条件有两个：没猜对（guess != secret）而且（and）还没用完次数（times < 10）
while guess != secret and times < 10:
    guess = int(input("猜一个 1~100 的数字："))
    times = times + 1

    if guess > secret:
        print("太大了，往小猜！")
    elif guess < secret:
        print("太小了，往大猜！")

# 循环结束后，看看是因为猜对，还是次数用完了
if guess == secret:
    print("猜对啦！你用了", times, "次 🎉")
else:
    print("10 次用完了……答案是", secret)

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 倒数发射 🚀：n = 10，while n > 0 打印 n 并 n = n - 1，
#    最后打印"发射！"
#
# 2. 累加器：一直输入数字，输入 0 就结束，打印所有数字的和
#
# 3. 石头剪刀布直到赢：把第 9 课的猜拳包进 while，
#    平局或输就再来，赢了才停
