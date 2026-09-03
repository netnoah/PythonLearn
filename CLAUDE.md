# CLAUDE.md（本项目）

## 项目
教用户 11 岁的儿子（六年级、零基础）学 Python。兴趣优先，约 20 课、5 个单元，完整总纲见 `README.md`。

## 学生画像
- 11 岁男孩，喜欢电子游戏、数学/科学/谜题。
- 示例尽量用游戏、谜题、动画主题，生动有趣。
- 代码用英文关键字，注释和讲解全用中文。

## 配色（重要）
- 课件幻灯片**不要用粉色等偏女性化的色系**。
- 用蓝色、青色、绿色、橙色等中性、清爽的色系。

## 每课产出
- 每课一个文件夹 `lessons/NN-slug/`，含 4 个文件：
  - `slides.html` —— 自包含 HTML 幻灯片（离线双击打开、键盘翻页）
  - `demo.py` —— 课堂示例
  - `challenge.py` —— 挑战题（可选）
  - `teaching-notes.md` —— 家长讲稿
- 每个 `demo.py` / `challenge.py` 开头**必须**带 Windows 防乱码开关（`sys.stdout/stdin.reconfigure` 成 UTF-8），否则 GBK 控制台会中文乱码、表情符号崩溃。
- 示例只用标准库，保证 `python demo.py` 直接能跑。
