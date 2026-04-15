# 黑马程序员 Python 入门教程 — 第四至六章笔记

> **课程来源**：[黑马程序员python零基础全套教程，8天python从入门到精通](https://www.bilibili.com/video/BV1qW4y1a7fU)  
> **本文覆盖**：第四章（循环语句）· 第五章（函数）· 第六章（数据容器）

---

## 第四章：Python 循环语句

### 01 — while 循环的基础应用

- **作用**：在条件满足的情况下，反复执行一段代码，直到条件不再成立。
- **语法**：
  ```python
  while 条件表达式:
      循环体（条件为 True 时重复执行）
  ```
- **执行流程**：判断条件 → 为 True 执行循环体 → 再次判断 → 直到为 False 退出。

```python
# 打印 1 到 5
i = 1
while i <= 5:
    print(i)
    i += 1
```

- **注意**：循环变量（如 `i`）必须在循环体内有更新操作，否则会形成**无限循环（死循环）**。

---

### 02 — 案例：求 1~100 的和

```python
# 需求：计算 1 + 2 + 3 + ... + 100 的结果
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(f"1到100的和为：{total}")   # 5050
```

**解题思路**：
1. 定义累加变量 `total = 0`，循环计数变量 `i = 1`
2. 每次循环将 `i` 加入 `total`，同时 `i += 1`
3. 当 `i > 100` 时退出循环

---

### 03 — while 循环猜数字案例

```python
import random
num = random.randint(1, 100)   # 随机生成 1~100 的整数

guess = int(input("请输入一个 1~100 的数字："))
while guess != num:
    if guess > num:
        print("猜大了！")
    else:
        print("猜小了！")
    guess = int(input("再猜一次："))

print("恭喜你猜对了！")
```

---

### 04 — while 循环的嵌套应用

- **嵌套**：while 循环体内再写一个 while 循环。
- **执行规律**：外层循环每执行一次，内层循环完整跑完一遍。
- **注意**：内外层循环变量**不能同名**；每次外层循环时，内层变量需要**重置**。

```python
# 语法结构
while 外层条件:
    外层代码
    while 内层条件:
        内层代码
    内层变量重置
```

---

### 05 — while 循环案例：九九乘法表

```python
i = 1
while i <= 9:       # 外层控制"行"（1~9行）
    j = 1
    while j <= i:   # 内层控制"列"（1~i列）
        print(f"{j}×{i}={j*i}\t", end='')  # end='' 不换行
        j += 1
    print()         # 每行结束后换行
    i += 1
```

输出效果：
```
1×1=1	
1×2=2	2×2=4	
1×3=3	2×3=6	3×3=9	
...
```

---

### 06 — for 循环的基础语法

- **作用**：对一个**序列（或可迭代对象）**中的每个元素依次执行操作。
- **语法**：
  ```python
  for 临时变量 in 待处理数据集:
      循环体
  ```
- **特点**：
  - 无需手动维护循环变量，自动取出每个元素。
  - 遍历完所有元素后自动结束，不会无限循环。

```python
# 遍历字符串
name = "黑马程序员"
for char in name:
    print(char)

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

### 07 — for 循环案例：数一数多少个字母 a

```python
# 需求：统计字符串中字母 'a' 的个数
sentence = "itheima is a brand of itcast"
count = 0
for char in sentence:
    if char == 'a':
        count += 1
print(f"字母 a 共出现了 {count} 次")   # 4次
```

---

### 08 — range 语句

- **作用**：生成一个整数序列，常配合 for 循环使用。
- **三种用法**：

  | 语法 | 说明 | 生成范围 |
  |------|------|---------|
  | `range(n)` | 从 0 到 n-1 | `[0, 1, 2, ..., n-1]` |
  | `range(start, end)` | 从 start 到 end-1 | `[start, ..., end-1]` |
  | `range(start, end, step)` | 指定步长 | 每隔 step 取一个 |

```python
for i in range(5):
    print(i)          # 0 1 2 3 4

for i in range(1, 6):
    print(i)          # 1 2 3 4 5

for i in range(1, 10, 2):
    print(i)          # 1 3 5 7 9（步长为2）

for i in range(10, 0, -1):
    print(i)          # 10 9 8 ... 1（倒序）
```

---

### 09 — for 循环临时变量作用域

- for 循环的**临时变量**（如 `for i in ...` 中的 `i`）在语法上属于**函数级作用域**。
- 循环结束后，临时变量**在理论上不应在循环外使用**（虽然 Python 不会报错，但规范上不推荐）。

```python
for i in range(5):
    pass
# print(i)  # 虽然可以输出 4，但不推荐这样写
```

- **规范做法**：如需循环外使用，应在循环前先定义该变量。

---

### 10 — for 循环的嵌套使用

- 与 while 嵌套类似，外层每执行一次，内层完整跑完一遍。

```python
# 使用 for 嵌套打印图案（5行 * 号）
for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()
```

---

### 11 — for 循环打印九九乘法表

```python
for i in range(1, 10):          # 行：1~9
    for j in range(1, i + 1):   # 列：1~i
        print(f"{j}×{i}={j*i}", end='\t')
    print()                     # 换行
```

---

### 12 — continue 和 break

**continue — 跳过本次循环，继续下一次：**
```python
# 打印 1~10 中的奇数（跳过偶数）
for i in range(1, 11):
    if i % 2 == 0:
        continue    # 偶数时跳过，不打印
    print(i)        # 1 3 5 7 9
```

**break — 终止整个循环：**
```python
# 遇到数字 5 就停止
for i in range(1, 11):
    if i == 5:
        break       # 直接跳出整个 for 循环
    print(i)        # 1 2 3 4
```

**关键区别：**
| 关键字 | 作用范围 | 效果 |
|--------|---------|------|
| `continue` | 当次循环 | 跳过剩余代码，进入下一次循环 |
| `break` | 整个循环 | 立即终止循环，执行循环后的代码 |

- 两者都**只作用于所在的那一层循环**，不影响外层循环。

---

### 13 — 循环综合案例

**案例：发工资（模拟逢 3 发双倍工资，遇到员工编号含 7 则停止）**

```python
# 模拟给员工发工资，员工编号 1~20
# 规则：编号是3的倍数发双倍，编号含7则停止发薪
for i in range(1, 21):
    if i % 7 == 0:          # 编号含7（7、17）
        print(f"员工 {i}：停止发薪！")
        break
    if i % 3 == 0:          # 编号是3的倍数
        print(f"员工 {i}：发双倍工资 🎉")
        continue
    print(f"员工 {i}：发普通工资")
```

---
