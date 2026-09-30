# -*- coding: utf-8 -*-
# ============================================================
# 第 12 课 挑战题：购物清单
# 创建一个购物清单，加东西、划掉东西、数数量
# ============================================================

# 防乱码开关（先不用管）
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8")
except Exception:
    pass

print("购物清单！")

# 1. 创建一个清单
shopping = ["牛奶", "面包", "鸡蛋"]
print("要买：", shopping)

# 2. 想起来还要买别的，用 append 加上
shopping.append("苹果")
shopping.append("香蕉")
print("加完水果：", shopping)

# 3. 数一数一共几样
print("一共", len(shopping), "样东西")

# 4. 家里还有鸡蛋，用 remove 划掉（删掉第一个匹配的）
shopping.remove("鸡蛋")
print("划掉鸡蛋后：", shopping)

# 5. 看看第一个要买啥
print("第一样要买的是：", shopping[0])

# ---- 更多挑战（自己动手，可以把上面的代码先注释掉）----
#
# 1. 抽奖转盘：prizes = ["铅笔", "橡皮", "贴纸", "糖果"]，
#    用 random.choice(prizes) 抽一个奖
#
# 2. 我的背包：创建自己的游戏道具列表，
#    用 [编号] 取出、append 加、len 数
#
# 3. 倒着数：打印 shopping[-1]、shopping[-2] 看看是什么
