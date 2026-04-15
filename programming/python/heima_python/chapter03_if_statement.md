## 第三章：Python 判断语句

### 01 — 布尔类型和比较运算符

**布尔类型（bool）：**
- 布尔类型只有两个值：`True`（真）和 `False`（假）。
- 布尔类型是 int 的子类：`True == 1`，`False == 0`。
- 定义布尔变量：
  ```python
  is_student = True
  is_adult = False
  ```

**比较运算符：**
| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `==` | 等于 | `3 == 3` | `True` |
| `!=` | 不等于 | `3 != 4` | `True` |
| `>` | 大于 | `5 > 3` | `True` |
| `<` | 小于 | `2 < 1` | `False` |
| `>=` | 大于等于 | `5 >= 5` | `True` |
| `<=` | 小于等于 | `3 <= 2` | `False` |

```python
print(10 > 5)     # True
print(10 == 10)   # True
print(10 != 5)    # True
print(type(10 > 5))   # <class 'bool'>
```

---

### 02 — if 语句的基本格式

- **作用**：根据条件判断，决定是否执行某段代码。
- **语法**：
  ```python
  if 条件表达式:
      条件成立时执行的代码块（必须缩进，通常4个空格）
  ```
- **注意**：`if` 后面有 **冒号 `:`**，下一行代码必须**缩进**（Python 以缩进表示代码块归属）。

```python
age = 20
if age >= 18:
    print("你已成年")
    print("可以做很多事情")
print("这行无论如何都会执行")
```

---

### 03 — 案例：成年人判断讲解

```python
# 需求：输入年龄，判断是否成年
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了！")
print("程序结束")
```

**执行流程：**
1. 获取用户输入的年龄
2. 判断 `age >= 18` 是否为 `True`
3. 是 → 执行 `print("你已经成年了！")`
4. 否 → 跳过该代码块
5. 无论如何都执行最后一行

---

### 04 — if-else 组合判断语句

- **作用**：条件成立走一条路，不成立走另一条路（二选一）。
- **语法**：
  ```python
  if 条件表达式:
      条件成立时执行
  else:
      条件不成立时执行
  ```

```python
age = int(input("请输入年龄："))
if age >= 18:
    print("成年人，可以买票")
else:
    print("未成年人，需要半价票")
```

- **if 和 else 是配对的**，`else` 不能单独使用，且不需要条件表达式。

---

### 05 — 案例：我要买票吗讲解

```python
# 需求：年龄 >= 18 买全票，否则买半票
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您需要购买全价票，票价：100 元")
else:
    print("您可以购买半价票，票价：50 元")
```

---

### 06 — if-elif-else 组合使用的语法

- **作用**：多条件分支判断（多选一）。
- **语法**：
  ```python
  if 条件1:
      条件1成立时执行
  elif 条件2:
      条件2成立时执行
  elif 条件3:
      条件3成立时执行
  else:
      所有条件都不成立时执行
  ```
- **执行规则**：从上到下依次判断，**一旦某个条件成立，执行其代码块后直接跳出整个 if 结构**，后面的条件不再判断。
- `else` 是可选的（可以没有 else）。

```python
score = int(input("请输入你的成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

---

### 07 — 案例：猜猜心里数字讲解

```python
import random
num = random.randint(1, 10)   # 随机生成 1~10 的整数
guess = int(input("请猜一个 1~10 的数字："))

if guess == num:
    print("恭喜你，猜对了！")
elif guess > num:
    print("猜大了，数字比你猜的小")
else:
    print("猜小了，数字比你猜的大")
```

---

### 08 — 判断语句的嵌套

- **嵌套**：在 `if` 的代码块内部，再写 `if` 语句，用于多层条件组合判断。
- **注意**：嵌套层级越多，越要注意**缩进**正确。

```python
# 需求：身高 > 1.2m 且有票才能进游乐场
height = float(input("请输入身高（米）："))
ticket = int(input("是否有票（1=有，0=没有）："))

if height > 1.2:
    print("身高达标")
    if ticket == 1:
        print("可以入场，欢迎游玩！")
    else:
        print("请先购票")
else:
    print("身高不足 1.2m，部分项目不可参与")
```

---

### 09 — 判断语句综合案例

**综合案例：石头剪刀布游戏**

```python
import random

# 规则：1=石头，2=剪刀，3=布
computer = random.randint(1, 3)
player = int(input("请出拳（1=石头，2=剪刀，3=布）："))

print(f"你出了：{player}，电脑出了：{computer}")

if player == computer:
    print("平局！")
elif (player == 1 and computer == 2) or \
     (player == 2 and computer == 3) or \
     (player == 3 and computer == 1):
    print("你赢了！")
else:
    print("电脑赢了！")
```

**逻辑运算符补充：**
| 运算符 | 含义 | 示例 |
|--------|------|------|
| `and` | 且（两个条件都为 True） | `a > 0 and b > 0` |
| `or` | 或（至少一个为 True） | `a > 0 or b > 0` |
| `not` | 非（取反） | `not True` → `False` |

---

## 笔记总结

| 章节 | 核心内容 |
|------|---------|
| **第一章** | Python 简介与历史、编程语言概念、环境安装（Win/Mac/Linux）、第一个程序、Python 解释器、PyCharm IDE |
| **第二章** | 字面量、注释、变量、数据类型、类型转换、标识符、运算符、字符串三种定义方式、字符串拼接与格式化（%/format/f-string）、精度控制、input 输入 |
| **第三章** | 布尔类型、比较运算符、if 语句、if-else、if-elif-else、嵌套判断、逻辑运算符 and/or/not |

> 📌 **学习建议**：每节课后动手敲一遍代码，不要只看不练。前三章是 Python 的基石，后续循环、函数、数据结构都建立在这些概念之上。
