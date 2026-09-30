# -*- coding: utf-8 -*-
# ============================================================
# 第 5 课：循环的魔法
# 学：for 循环 + range，把重复的代码变短
# 作品：正方形 → 多边形 → 五角星 → 炫酷螺旋
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

turtle.setup(800, 600)
t = turtle.Turtle()
t.speed(10)
q=0              # 0 = 最快（瞬间画完）；改成 1~10 可以慢慢看它爬
# for i in range(100):
#    q=q+2
#    print(q) 
    
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# q=1000
# for i in range(q):
#     t.forward(1)
#     t.right(360/q)



# colors = ["red","orange","yellow",
#           "green","blue","purple"]
# for i in range(10000000000000000000):
#     t.pencolor(colors[i % 6])
#     t.forward(i * 2)
#     t.right(99)


q=4
for i in range(q):
    for k in range(i):
        print(k)

for k in range(2):
    print(k)

# 画完了！让窗口不关闭
turtle.done()
