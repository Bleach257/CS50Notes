
## 第六章：Python 数据容器

### 01 — 数据容器入门

- **数据容器**：可以容纳**多个元素**的数据类型，每个元素可以是任意类型。
- Python 中的五大数据容器：

  | 容器 | 关键字 | 特点 |
  |------|--------|------|
  | 列表 | `list` | 有序、可重复、**可修改** |
  | 元组 | `tuple` | 有序、可重复、**不可修改** |
  | 字符串 | `str` | 有序、可重复、**不可修改** |
  | 集合 | `set` | 无序、**不可重复**、可修改 |
  | 字典 | `dict` | 无序、key不可重复、可修改，存键值对 |

---

### 02 — 列表的定义语法

```python
# 字面量
[元素1, 元素2, 元素3, ...]

# 定义变量
my_list = ["Python", 666, True, 3.14]   # 可混合类型

# 空列表
empty = []
empty2 = list()

# 嵌套列表
nested = [[1, 2], [3, 4], [5, 6]]
```

---

### 03 — 列表的下标索引

- **正向索引**：从 `0` 开始，从左往右递增。
- **反向索引**：从 `-1` 开始，从右往左递减。

```python
names = ["小明", "小红", "小蓝", "小绿"]
#         0       1       2       3       正向
#        -4      -3      -2      -1       反向

print(names[0])     # 小明
print(names[-1])    # 小绿
print(names[2])     # 小蓝

# 嵌套列表取值
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0][1])   # 2（第0行第1列）
print(matrix[1][2])   # 6（第1行第2列）
```

---

### 04 — 列表的常用操作方法

| 操作 | 方法/语法 | 说明 |
|------|----------|------|
| 查找下标 | `list.index(元素)` | 返回第一个匹配元素的下标，不存在报 `ValueError` |
| 修改元素 | `list[下标] = 新值` | 直接通过下标赋新值 |
| 插入元素 | `list.insert(下标, 元素)` | 在指定位置插入，原元素后移 |
| 末尾追加 | `list.append(元素)` | 追加单个元素到末尾 |
| 批量追加 | `list.extend(容器)` | 将另一个容器的元素追加到末尾 |
| 删除元素 | `del list[下标]` | 按下标删除，无返回值 |
| 删除并返回 | `list.pop(下标)` | 按下标删除，**返回被删除的元素** |
| 删除匹配值 | `list.remove(元素)` | 删除第一个匹配的元素 |
| 清空列表 | `list.clear()` | 清空所有元素 |
| 统计次数 | `list.count(元素)` | 返回元素出现次数 |
| 获取长度 | `len(list)` | 返回元素总个数 |

```python
nums = [1, 2, 3, 4, 5]

nums.append(6)          # [1, 2, 3, 4, 5, 6]
nums.insert(0, 0)       # [0, 1, 2, 3, 4, 5, 6]
nums.remove(3)          # [0, 1, 2, 4, 5, 6]
popped = nums.pop(1)    # popped=1, nums=[0, 2, 4, 5, 6]
print(nums.index(4))    # 2
print(len(nums))        # 5
```

---

### 05 — 列表的常用操作课后练习讲解

```python
# 练习：将以下操作应用到列表 [21, 25, 21, 23, 22, 20]
ages = [21, 25, 21, 23, 22, 20]

# 1. 追加元素 31
ages.append(31)

# 2. 追加一个新列表 [29, 33, 30]
ages.extend([29, 33, 30])

# 3. 取出下标为 2 的元素
print(ages[2])           # 21

# 4. 删除第一个 21
ages.remove(21)

# 5. 清空列表
ages.clear()
print(ages)              # []
```

---

### 06 — 列表的循环遍历

**方式一：while 循环（通过下标）：**
```python
fruits = ["苹果", "香蕉", "西瓜"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

**方式二：for 循环（推荐）：**
```python
fruits = ["苹果", "香蕉", "西瓜"]
for fruit in fruits:
    print(fruit)
```

---

### 07 — 元组的定义和操作

- **元组（tuple）**：与列表相似，但**不可修改**（不能增删改元素）。
- 适合存储**不应被改变的数据**（如坐标、配置信息等）。

```python
# 定义元组
point = (10, 20)
info = ("小明", 18, "北京")

# 单元素元组（必须加逗号！）
single = (100,)         # ✅ 元组
not_tuple = (100)       # ❌ 这只是整数 100

# 空元组
empty = ()
empty2 = tuple()

# 下标访问（同列表）
print(info[0])          # 小明
print(info[-1])         # 北京
```

**元组支持的操作：**
```python
t = (1, 2, 3, 2, 1)
print(t.index(2))       # 1（第一个2的下标）
print(t.count(1))       # 2（1出现了2次）
print(len(t))           # 5
```

**元组的特殊规则：**
```python
# 元组内的列表可以被修改（列表本身是可变的）
t = (1, [2, 3], 4)
t[1][0] = 99            # ✅ 修改的是列表，不是元组结构
print(t)                # (1, [99, 3], 4)
```

---

### 08 — 字符串的定义和操作

- 字符串也是一种数据容器，每个字符就是一个元素，支持下标索引，但**不可修改**。

**常用操作方法：**
| 方法 | 功能 | 示例 |
|------|------|------|
| `str.index(子串)` | 查找子串起始下标 | `"Hello".index("l")` → `2` |
| `str.replace(旧, 新)` | 替换（**返回新字符串，原字符串不变**） | `"abc".replace("a", "A")` → `"Abc"` |
| `str.split(分隔符)` | 按分隔符分割，返回**列表** | `"a,b,c".split(",")` → `['a','b','c']` |
| `str.strip()` | 去除首尾**空白字符** | `"  hi  ".strip()` → `"hi"` |
| `str.strip(字符)` | 去除首尾**指定字符** | `"12abc21".strip("12")` → `"abc"` |
| `str.lstrip()` | 只去左侧空白 | — |
| `str.rstrip()` | 只去右侧空白 | — |
| `str.count(子串)` | 统计子串出现次数 | `"abcabc".count("a")` → `2` |
| `len(str)` | 字符串长度 | `len("Hello")` → `5` |

```python
text = "itheima and itcast"
print(text.index("and"))        # 8
print(text.replace("and", "or"))  # "itheima or itcast"
print(text.split(" "))          # ['itheima', 'and', 'itcast']
print("  hello  ".strip())      # "hello"
print(text.count("it"))         # 2
```

---

### 09 — 字符串的课后练习讲解

```python
# 给定字符串，去除首尾的 "it"，并将空格替换为逗号
s = "itheima and itcast"
s = s.strip("it")               # "heima and itcast" → "heima and itcas"
# 注意：strip("it") 会去除首尾所有 i 和 t 字符
s2 = s.replace(" ", ",")
print(s2)
```

---

### 10 — 数据容器（序列）的切片

- **序列**：内容连续、有序的容器 → 包括**列表、元组、字符串**。
- **切片**：从序列中取出一个**子序列**，原数据**不变**，返回**新对象**。

**语法：**
```python
序列[起始下标 : 结束下标 : 步长]
```

- 起始下标（含）、结束下标（不含）
- 步长默认为 1，可为负数（表示反向）
- 三个参数均可省略

```python
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(s[2:6])           # [2, 3, 4, 5]（下标2到5）
print(s[::2])           # [0, 2, 4, 6, 8]（步长2，每隔一个取一个）
print(s[::-1])          # [9, 8, 7, ..., 0]（反转）
print(s[1:8:3])         # [1, 4, 7]

# 字符串切片
text = "Hello World"
print(text[0:5])        # "Hello"
print(text[::-1])       # "dlroW olleH"

# 元组切片
t = (1, 2, 3, 4, 5)
print(t[1:4])           # (2, 3, 4)
```

---

### 11 — 序列的切片课后练习讲解

```python
# 将列表 [0,1,2,3,4,5,6,7,8,9] 倒序后，取偶数位元素
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = nums[::-1][::2]    # 先反转，再每隔一个取一个
print(result)               # [9, 7, 5, 3, 1]
```

---

### 12 — 集合的定义和操作

- **集合（set）**：无序、**不重复**的数据容器，常用于去重和集合运算。
- **不支持下标索引**（无序，无法用位置取值）。

```python
# 定义集合
s = {1, 2, 3, 2, 1}    # 自动去重
print(s)                # {1, 2, 3}

# 空集合（不能用 {}，那是空字典！）
empty = set()

# 基本操作
s.add(4)                # {1, 2, 3, 4}
s.remove(2)             # {1, 3, 4}
s.pop()                 # 随机移除一个元素
s.clear()               # 清空
print(len(s))           # 0
```

**集合运算：**
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.difference(b))          # 差集：{1, 2, 3}（a有但b没有的）
print(a.union(b))                # 并集：{1,2,3,4,5,6,7,8}
print(a.intersection(b))         # 交集：{4, 5}

# 消除差集（从a中删除b有的元素，原地修改）
a.difference_update(b)
print(a)                        # {1, 2, 3}
```

**遍历集合（只能用 for）：**
```python
s = {1, 2, 3, 4, 5}
for item in s:
    print(item)         # 顺序不定
```

---

### 13 — 集合的课后练习

```python
# 练习：对两组学生的选课数据去重并求交集
group_a = {"小明", "小红", "小蓝", "小明"}  # 自动去重
group_b = {"小蓝", "小绿", "小红"}

# 两组都选的学生（交集）
both = group_a.intersection(group_b)
print(f"两组都选的同学：{both}")   # {'小红', '小蓝'}
```

---

### 14 — 字典的定义

- **字典（dict）**：以**键值对（key-value）** 形式存储数据，通过 key 快速查找 value。
- **key 要求**：必须是**不可变类型**（字符串、数字、元组），且**不可重复**。
- **value**：任意类型。

```python
# 定义字典
person = {
    "name": "小明",
    "age": 18,
    "hobby": ["Python", "篮球"]
}

# 空字典
empty = {}
empty2 = dict()

# 通过 key 获取 value
print(person["name"])       # 小明
print(person["hobby"])      # ['Python', '篮球']
```

**嵌套字典（字典套字典）：**
```python
students = {
    "小明": {"age": 18, "score": 95},
    "小红": {"age": 17, "score": 88}
}
print(students["小明"]["score"])    # 95
```

---

### 15 — 字典的常用操作

| 操作 | 语法 | 说明 |
|------|------|------|
| 新增/修改 | `dict[key] = value` | key 存在则修改，不存在则新增 |
| 删除 | `dict.pop(key)` | 删除指定 key，返回对应 value |
| 获取全部 key | `dict.keys()` | 返回所有 key 的视图 |
| 获取全部 value | `dict.values()` | 返回所有 value 的视图 |
| 获取全部键值对 | `dict.items()` | 返回所有 (key, value) 对 |
| 清空 | `dict.clear()` | 清空所有元素 |
| 统计元素数 | `len(dict)` | 返回键值对个数 |

```python
d = {"a": 1, "b": 2, "c": 3}

d["d"] = 4              # 新增
d["a"] = 100            # 修改
d.pop("b")              # 删除 b，返回 2

print(d.keys())         # dict_keys(['a', 'c', 'd'])
print(d.values())       # dict_values([100, 3, 4])
print(d.items())        # dict_items([('a',100), ('c',3), ('d',4)])
```

**遍历字典：**
```python
d = {"name": "小明", "age": 18}

# 方式1：遍历 key
for key in d:
    print(key, d[key])

# 方式2：遍历键值对（推荐）
for key, value in d.items():
    print(f"{key} = {value}")
```

---

### 16 — 字典课后练习讲解

```python
# 统计字符串中各字符出现的次数
text = "itheima itcast"
result = {}

for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print(result)   # {'i': 3, 't': 3, 'h': 1, 'e': 1, ...}
```

---

### 17 — 五类数据容器的总结对比

| 特性 | 列表 list | 元组 tuple | 字符串 str | 集合 set | 字典 dict |
|------|-----------|-----------|-----------|---------|----------|
| 定义符号 | `[]` | `()` | `""` | `{}` | `{k:v}` |
| 是否有序 | ✅ | ✅ | ✅ | ❌ | ❌（3.7+有序） |
| 是否可修改 | ✅ | ❌ | ❌ | ✅ | ✅ |
| 是否允许重复 | ✅ | ✅ | ✅ | ❌ | key不可重复 |
| 支持下标 | ✅ | ✅ | ✅ | ❌ | ❌（用key） |
| 支持切片 | ✅ | ✅ | ✅ | ❌ | ❌ |
| 元素类型 | 任意 | 任意 | 仅字符 | 任意 | key为不可变 |
| 使用场景 | 通用、可改 | 不变数据 | 文本处理 | 去重运算 | 键值映射 |

---

### 18 — 数据容器的通用操作

所有数据容器都支持以下**通用操作**：

| 操作 | 语法 | 说明 |
|------|------|------|
| 统计长度 | `len(容器)` | 元素个数 |
| 最大值 | `max(容器)` | 返回最大元素 |
| 最小值 | `min(容器)` | 返回最小元素 |
| 排序（升序） | `sorted(容器)` | 返回**新列表** |
| 排序（降序） | `sorted(容器, reverse=True)` | 返回新列表 |
| 类型转换 | `list()` `tuple()` `set()` `str()` | 容器间转换 |

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(data))                    # 8
print(max(data))                    # 9
print(min(data))                    # 1
print(sorted(data))                 # [1, 1, 2, 3, 4, 5, 6, 9]
print(sorted(data, reverse=True))   # [9, 6, 5, 4, 3, 2, 1, 1]

# 类型转换示例
s = {1, 2, 3}
print(list(s))      # [1, 2, 3]（列表，可能顺序不同）
print(tuple(s))     # (1, 2, 3)

nums = [1, 2, 2, 3, 3]
print(set(nums))    # {1, 2, 3}（去重）
```

---

### 19 — 【拓展】字符串大小比较的方式

- 字符串比较基于**ASCII 码**逐位比较，第一个不同位的字符决定大小。
- 常用 ASCII 值（记住大小关系即可）：
  - `'0'`~`'9'`：48~57
  - `'A'`~`'Z'`：65~90
  - `'a'`~`'z'`：97~122
  - 规律：**数字 < 大写字母 < 小写字母**

```python
print("abc" > "abd")        # False（第3位 c < d）
print("abc" > "ab")         # True（前两位相同，长的更大）
print("B" > "A")            # True（66 > 65）
print("a" > "Z")            # True（97 > 90）
print(ord("a"))             # 97（查看字符的 ASCII 值）
print(chr(65))              # A（ASCII 值转字符）
```

---

## 本章笔记总结

| 章节 | 节数 | 核心知识点 |
|------|------|-----------|
| **第四章** 循环语句 | 13节 | while循环、嵌套循环、for循环、range()、变量作用域、continue/break、九九乘法表 |
| **第五章** 函数 | 11节 | 函数定义def、形参/实参、return返回值、None类型、说明文档、嵌套调用、局部/全局变量、global关键字 |
| **第六章** 数据容器 | 19节 | 列表(list)、元组(tuple)、字符串(str)、序列切片、集合(set)、字典(dict)、五类容器对比、通用操作 |

> 📌 **学习建议**：
> - 第四章重点练习**九九乘法表**，彻底理解嵌套循环逻辑。
> - 第五章务必掌握**全局变量/局部变量的区别**，是后续编程的基础。
> - 第六章**字典**最为重要，实际开发中使用频率极高，要熟练掌握增删改查和遍历。
