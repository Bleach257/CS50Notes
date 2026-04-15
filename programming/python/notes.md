# 黑马程序员 Python 入门教程 — 前三章笔记

> **课程来源**：[黑马程序员python零基础全套教程，8天python从入门到精通](https://www.bilibili.com/video/BV1qW4y1a7fU)  
> **整理说明**：以下笔记按课程章节逐节整理，涵盖第一章至第三章所有知识点。

---

## 第一章：初识 Python

### 01 — 初识 Python

- Python 是一种 **通用型编程语言**，由荷兰程序员 **吉多·范罗苏姆（Guido van Rossum）** 于 **1989 年圣诞假期** 开始开发，1991 年发布第一个版本。
- 名字来源于吉多喜爱的英国喜剧《蒙提·派森的飞行马戏团》（Monty Python's Flying Circus）。
- 口号：**"人生苦短，我用 Python！"**
- **Python 的优势**：
  - 语法简洁优雅，代码可读性强
  - 应用领域极广：Web 开发、数据分析、人工智能、自动化脚本、科学计算等
  - 拥有庞大的第三方库生态（pip 包管理）
  - 跨平台，支持 Windows / macOS / Linux

---

### 02 — 什么是编程语言

- **计算机** 只能识别 **二进制（0 和 1）**，无法直接理解人类语言。
- **编程语言** 是人类与计算机之间沟通的桥梁，程序员用编程语言编写代码，再由工具翻译成计算机能执行的指令。
- 编程语言分类：
  | 类别 | 特点 | 代表语言 |
  |------|------|---------|
  | 编译型 | 一次性将所有代码编译为机器码，执行速度快 | C、C++、Go |
  | 解释型 | 逐行翻译、逐行执行，开发效率高 | Python、JavaScript |
- Python 是 **解释型语言**，代码由 **Python 解释器** 逐行翻译后执行。

---

### 03 — Python 环境安装（Windows）

1. 访问官网：[https://www.python.org/downloads/](https://www.python.org/downloads/)
2. 下载最新稳定版（课程使用 **Python 3.10**）。
3. 安装时 **必须勾选** `Add python.exe to PATH`（将 Python 添加到系统环境变量）。
4. 可选自定义安装路径（建议不含中文及空格）。
5. 验证安装：打开命令行（CMD），输入 `python`，出现版本号即安装成功。

```
C:\Users\xxx> python
Python 3.10.x ...
>>>
```

---

### 04 — 【拓展】Python 环境安装（macOS）

- macOS 预装了 Python 2，但课程使用 Python 3，需另行安装。
- 两种方式：
  1. **官网下载**：下载 `.pkg` 安装包，直接双击安装，安装后使用 `python3` 命令。
  2. **Homebrew 安装**：`brew install python3`
- 验证：在终端输入 `python3 --version`。
- 注意：macOS 终端用 `python3`，不要用 `python`（那是系统自带的 Python 2）。

---

### 05 — 【拓展】Python 环境安装（Linux）

- 大多数 Linux 发行版已预装 Python 3，可先用 `python3 --version` 检查。
- 如需安装：
  - Ubuntu/Debian：`sudo apt-get install python3`
  - CentOS/RHEL：`sudo yum install python3`
- 同样使用 `python3` 命令运行。

---

### 06 — 第一个 Python 程序 — Hello World

**两种运行方式：**

**方式一：交互式（命令行）**
```python
# 终端输入 python3 进入交互模式
>>> print("Hello World")
Hello World
```

**方式二：文件式（推荐）**
1. 新建文本文件，命名为 `hello.py`（扩展名必须是 `.py`）。
2. 写入代码：`print("Hello World")`
3. 在终端执行：`python3 hello.py`

**`print()` 函数说明：**
- 功能：将内容输出到终端屏幕。
- 可以输出字符串、数字、变量等。
- 示例：`print("你好，Python！")`

---

### 07 — 第一个 Python 程序 — 练习讲解

- **练习题**：编写程序，用 `print()` 依次输出以下内容：
  ```
  Hello World
  黑马程序员
  学Python
  ```
- **参考代码**：
  ```python
  print("Hello World")
  print("黑马程序员")
  print("学Python")
  ```
- **要点**：每个 `print()` 语句默认末尾换行，多次调用就会逐行输出。

---

### 08 — 第一个 Python 程序 — 常见问题解答

| 常见问题 | 原因 | 解决方法 |
|---------|------|---------|
| `python` 不是内部命令 | 环境变量未配置 | 重新安装，勾选 Add to PATH |
| `SyntaxError: invalid syntax` | 使用了中文符号（如中文括号、中文引号） | 检查并改为英文符号 |
| 文件名含中文/空格导致路径报错 | 路径解析问题 | 文件名/路径使用英文 |
| 运行后窗口一闪而过 | 用双击运行了 .py 文件 | 在命令行用 `python3 文件名.py` 执行 |

---

### 09 — Python 解释器

- **什么是 Python 解释器**：负责将 Python 代码翻译为计算机底层二进制指令并执行的程序。
- **工作流程**：
  ```
  Python 代码(.py) → Python 解释器 → 二进制机器码 → CPU 执行
  ```
- **常见的 Python 解释器版本**：
  | 解释器 | 说明 |
  |--------|------|
  | CPython | 官方标准解释器，用 C 语言编写，最常用 |
  | Jython | 运行在 Java 平台的解释器 |
  | IronPython | 面向 .NET 平台 |
  | PyPy | 速度更快，使用 JIT 编译技术 |
- 我们日常学习安装的就是 **CPython**，即 Python 官网下载的版本。
- 安装 Python 的本质 = 安装 CPython 解释器。

---

### 10 — PyCharm 开发工具的安装和基础使用

- **IDE（集成开发环境）**：比记事本更专业的代码编辑器，提供语法高亮、自动补全、调试等功能。
- **PyCharm** 是 JetBrains 公司出品的 Python 专业 IDE，有 **社区版（免费）** 和 **专业版（收费）**，学习阶段使用社区版即可。

**安装步骤：**
1. 官网下载：[https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)，选择 Community（社区版）。
2. 双击安装包，选择安装路径（不含中文）。
3. 勾选「Create Desktop Shortcut」（创建桌面快捷方式）。

**创建项目与文件：**
1. 打开 PyCharm → New Project（新建工程）。
2. 配置项目路径，选择已安装的 Python 解释器。
3. 右键项目名 → New → Python File，命名后开始编写代码。
4. 右键文件 → Run，或使用快捷键 `Shift+F10` 运行。

**基础设置：**
- 修改主题：File → Settings → Appearance & Behavior → Theme
- 修改字体/字号：File → Settings → Editor → Font
- 安装汉化插件：Settings → Plugins → 搜索 `Chinese`，安装后重启

---

### 11 — 【拓展】PyCharm 的基础使用

- **快捷键**：
  | 快捷键 | 功能 |
  |--------|------|
  | `Ctrl + /` | 注释/取消注释当前行 |
  | `Ctrl + Z` | 撤销 |
  | `Ctrl + Shift + Z` | 重做 |
  | `Shift + F10` | 运行当前程序 |
  | `Alt + Enter` | 快速修复提示 |
- **调试功能（Debug）**：
  - 点击代码行号左侧设置**断点（红点）**。
  - 右键 → Debug，程序执行到断点处会暂停，可查看变量值。
- **Python Console**：PyCharm 内置的交互式终端，可在 Tools → Python Console 打开。

---

### 12 — 第一章内容重点回顾

| 知识点 | 核心内容 |
|--------|---------|
| Python 简介 | 吉多创造，1991年诞生，口号"人生苦短我用Python" |
| 编程语言 | 人机交流工具，Python 是解释型语言 |
| 环境安装 | 官网下载 Python，勾选 Add to PATH |
| Hello World | `print("Hello World")` |
| 常见错误 | 中文符号、环境变量未配置 |
| Python 解释器 | 翻译 Python 代码为机器码，CPython 是官方默认 |
| PyCharm | 专业 Python IDE，社区版免费 |

---

## 第二章：Python 基础语法

### 01 — 字面量

- **字面量**：在代码中 **直接写出来的固定值**，即"所见即所得"的数据。
- Python 中常用字面量类型：

  | 类型 | 说明 | 示例 |
  |------|------|------|
  | 整数（int） | 正整数、负整数、零 | `10`、`-5`、`0` |
  | 浮点数（float） | 小数 | `3.14`、`-0.5` |
  | 复数（complex） | 含虚数部分 | `4+3j` |
  | 布尔（bool） | 真假值 | `True`、`False` |
  | 字符串（str） | 文字 | `"Hello"`、`'Python'` |
  | 列表（list） | 有序集合 | `[1, 2, 3]` |
  | 元组（tuple） | 不可变有序集合 | `(1, 2, 3)` |
  | 集合（set） | 无序不重复集合 | `{1, 2, 3}` |
  | 字典（dict） | 键值对集合 | `{"name": "Tom"}` |

- 字面量可以直接用 `print()` 输出：
  ```python
  print(666)         # 整数
  print(3.14)        # 浮点数
  print("Python")    # 字符串
  ```

---

### 02 — 注释

- **注释**：代码中不会被执行的说明文字，用于提高代码可读性。

**单行注释：**
```python
# 这是一行注释（# 后建议加一个空格）
print("Hello")  # 这也是注释，写在代码行末尾
```

**多行注释（文档注释）：**
```python
"""
这是多行注释
可以跨越多行
常用于函数/类的文档说明
"""
```

- **注意**：注释不影响程序运行，是写给"人"看的。
- **快捷键**：在 PyCharm 中，`Ctrl + /` 可快速注释/取消注释。

---

### 03 — 变量

- **变量**：程序运行时，用于 **临时存储数据** 的容器，值可以被修改。
- **定义格式**：
  ```python
  变量名 = 变量值
  ```
- **示例**：
  ```python
  money = 50
  print(money)   # 输出 50
  money = 30
  print(money)   # 输出 30（值被修改）
  ```
- **特点**：
  - Python 是动态类型语言，变量无需声明类型。
  - 变量的类型由赋给它的值决定。
  - 同一个变量可以先后存储不同类型的值。

---

### 04 — 数据类型

- **查看数据类型**：使用 `type()` 函数。
  ```python
  print(type(10))        # <class 'int'>
  print(type(3.14))      # <class 'float'>
  print(type("Hello"))   # <class 'str'>
  print(type(True))      # <class 'bool'>
  ```
- **嵌套用法**（查看变量的类型）：
  ```python
  name = "黑马程序员"
  print(type(name))      # <class 'str'>
  ```
- 入门阶段主要掌握：`int`（整数）、`float`（浮点数）、`str`（字符串）这三种基础类型。

---

### 05 — 数据类型转换

- 程序开发中经常需要在不同类型之间转换（如将字符串转为数字进行计算）。

  | 函数 | 作用 | 注意 |
  |------|------|------|
  | `int(x)` | 转为整数 | 字符串内容必须是纯整数字 |
  | `float(x)` | 转为浮点数 | 字符串内容必须是数字 |
  | `str(x)` | 转为字符串 | 任意类型均可转 |

- **示例**：
  ```python
  num_str = "10"
  num = int(num_str)
  print(num + 5)      # 15

  pi = 3.14
  print(str(pi))      # "3.14"（字符串）

  print(int(3.9))     # 3（直接截断小数，不四舍五入）
  ```
- **常见报错**：
  ```python
  int("hello")        # ValueError：字符串含非数字字符
  int("3.14")         # ValueError：浮点数字符串不能直接转整数
  ```

---

### 06 — 标识符

- **标识符**：变量名、函数名、类名等"自定义名称"的统称。
- **命名规则（硬性）**：
  1. 只能包含 **字母、数字、下划线（_）**
  2. **不能以数字开头**
  3. **区分大小写**（`Name` 与 `name` 是不同变量）
  4. **不能使用 Python 关键字**（如 `if`、`for`、`while` 等）

- **命名规范（建议遵守）**：
  - 使用 **英文**，不推荐中文
  - 见名知意（`student_age` 比 `a` 好得多）
  - 多个单词用 **下划线分隔**（`snake_case`）：`my_name`、`student_score`

- **Python 关键字示例**（不可用作标识符）：
  ```
  False, True, None, and, or, not, if, elif, else,
  for, while, break, continue, return, def, class, import, ...
  ```

---

### 07 — 运算符

**算术运算符：**

| 运算符 | 描述 | 示例 | 结果 |
|--------|------|------|------|
| `+` | 加 | `1 + 1` | `2` |
| `-` | 减 | `5 - 3` | `2` |
| `*` | 乘 | `3 * 4` | `12` |
| `/` | 除（结果为浮点数） | `10 / 3` | `3.3333...` |
| `//` | 整除（取商的整数部分） | `10 // 3` | `3` |
| `%` | 取模（取余数） | `10 % 3` | `1` |
| `**` | 幂运算 | `2 ** 3` | `8` |

**赋值运算符：**

| 运算符 | 示例 | 等价于 |
|--------|------|--------|
| `=` | `a = 10` | 赋值 |
| `+=` | `a += 5` | `a = a + 5` |
| `-=` | `a -= 3` | `a = a - 3` |
| `*=` | `a *= 2` | `a = a * 2` |
| `/=` | `a /= 4` | `a = a / 4` |
| `//=` | `a //= 3` | `a = a // 3` |
| `%=` | `a %= 2` | `a = a % 2` |

---

### 08 — 字符串的三种定义方式

Python 中字符串用引号包裹，共有三种形式：

```python
# 1. 单引号
name1 = 'Hello Python'

# 2. 双引号
name2 = "Hello Python"

# 3. 三引号（支持换行，常用于多行文本）
name3 = """Hello
Python"""
```

**引号嵌套技巧：**
```python
# 字符串中包含单引号，外层用双引号
msg1 = "I'm Tom"

# 字符串中包含双引号，外层用单引号
msg2 = 'He said "Hello"'

# 使用转义字符 \
msg3 = 'I\'m Tom'
```

---

### 09 — 字符串的拼接

- 使用 `+` 运算符拼接两个字符串：
  ```python
  first = "黑马"
  last = "程序员"
  full = first + last
  print(full)       # 黑马程序员
  ```
- **注意**：`+` 只能连接**同为字符串**类型的值，不能将字符串与数字直接拼接：
  ```python
  age = 18
  # print("我今年" + age)   # TypeError!
  print("我今年" + str(age))  # 正确：先转换为字符串
  ```

---

### 10 — 字符串格式化

字符串格式化是将变量嵌入字符串模板的方法，有多种方式：

**方式一：`%` 占位符（旧式）**
| 占位符 | 对应类型 |
|--------|---------|
| `%s` | 字符串（万能，任何类型均可） |
| `%d` | 整数 |
| `%f` | 浮点数（默认保留6位小数） |

```python
name = "小明"
age = 18
score = 98.5

print("姓名：%s，年龄：%d，成绩：%f" % (name, age, score))
# 输出：姓名：小明，年龄：18，成绩：98.500000
```

---

### 11 — 字符串格式化的精度控制

- 在 `%f` 中使用 `m.n` 控制数字的宽度和小数位数：
  - `m`：控制最小宽度（整体占几个字符位）
  - `.n`：控制小数点后几位（**四舍五入**）

```python
num = 3.1415926
print("%.2f" % num)    # 3.14（保留2位小数）
print("%10.3f" % num)  #      3.142（宽度10，保留3位小数）
print("%d" % 3.9)      # 3（整数格式化会截断小数，不四舍五入）
```

---

### 12 — 字符串格式化的方式 2（format）

**方式二：`format()` 方法**
```python
name = "小明"
age = 18
print("姓名：{}，年龄：{}".format(name, age))
# 输出：姓名：小明，年龄：18
```

---

### 13 — 对表达式进行格式化（f-string）

**方式三：f-string（Python 3.6+，最推荐）**
- 在字符串前加 `f`，大括号 `{}` 内可以放变量或**任意表达式**：

```python
name = "小明"
age = 18
score = 98.5

# 普通变量
print(f"姓名：{name}，年龄：{age}")

# 表达式也可以直接写进去
print(f"明年 {name} 就 {age + 1} 岁了")

# 格式化浮点数精度
print(f"成绩：{score:.2f}")    # 98.50
```

- **优势**：直观、简洁，支持表达式，是现代 Python 最推荐的格式化方式。

---

### 14 — 字符串格式化练习题讲解

**综合练习：**
```python
# 题目：格式化输出用户信息
name = "小明"
age = 20
money = 12345.678

# 要求：使用 f-string，金额保留2位小数
print(f"我叫{name}，今年{age}岁，存款{money:.2f}元")
# 输出：我叫小明，今年20岁，存款12345.68元
```

**三种格式化方式对比：**
| 方式 | 写法 | 推荐程度 |
|------|------|---------|
| `%` 占位符 | `"%s" % var` | 旧式，了解即可 |
| `format()` | `"{}".format(var)` | 较通用 |
| f-string | `f"{var}"` | ⭐⭐⭐ 最推荐 |

---

### 15 — 数据输入（input 语句）

- **`input()` 函数**：获取用户从键盘输入的内容。
- **语法**：
  ```python
  变量 = input("提示信息")
  ```
- **关键特点**：无论用户输入什么，`input()` 的返回值**始终是字符串（str）类型**！

```python
name = input("请输入你的名字：")
print(f"你好，{name}！")

age_str = input("请输入你的年龄：")
age = int(age_str)      # 必须转换才能参与数学计算
print(f"明年你{age + 1}岁")
```

- **完整练习**：
  ```python
  num1 = int(input("请输入第一个数字："))
  num2 = int(input("请输入第二个数字："))
  print(f"{num1} + {num2} = {num1 + num2}")
  ```

---

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

## 第五章：Python 函数

### 01 — 函数的初体验

- **函数**：将一段具有特定功能的代码**封装起来**，可以反复调用，避免代码重复。
- **好处**：
  - 提高代码复用性
  - 提升代码可维护性
  - 让程序结构更清晰

```python
# 没有函数：重复写相同逻辑
print(1 + 2 + 3)
print(4 + 5 + 6)

# 有函数：封装后复用
def sum_three(a, b, c):
    print(a + b + c)

sum_three(1, 2, 3)
sum_three(4, 5, 6)
```

---

### 02 — 函数的基础定义语法

- **语法**：
  ```python
  def 函数名(参数):
      函数体
      return 返回值
  ```
- **要点**：
  - `def` 是关键字，必须有
  - 函数名命名规则同变量（小写+下划线）
  - 小括号 `()` 不可省略
  - 参数和 `return` **可以省略**
  - 先定义，后调用（否则报 `NameError`）

```python
def greet():
    print("你好，欢迎学习Python！")

greet()     # 调用函数
greet()     # 可多次调用
```

---

### 03 — 函数基础定义练习案例

```python
# 定义一个函数，输出个人信息
def print_info():
    print("姓名：小明")
    print("年龄：18")
    print("爱好：学Python")

print_info()
```

---

### 04 — 函数的传入参数

- **形参**：定义函数时括号内的参数名（占位符）。
- **实参**：调用函数时传入的实际值。
- 传参时实参与形参**位置一一对应**，数量需一致（否则报 `TypeError`）。

```python
def add(a, b):      # a, b 是形参
    print(a + b)

add(3, 5)           # 3, 5 是实参，输出 8
add(10, 20)         # 输出 30
```

**多个参数：**
```python
def introduce(name, age, city):
    print(f"我叫{name}，{age}岁，来自{city}")

introduce("小明", 18, "北京")
```

---

### 05 — 函数的参数练习案例

```python
# 定义函数：计算两个数的最大值
def get_max(a, b):
    if a > b:
        print(f"最大值是：{a}")
    else:
        print(f"最大值是：{b}")

get_max(10, 20)     # 最大值是：20
get_max(99, 66)     # 最大值是：99
```

---

### 06 — 函数的返回值定义语法

- **return**：将函数的计算结果返回给调用方，调用方可以接收并使用。
- **语法**：
  ```python
  def 函数名():
      ...
      return 结果
  ```
- **注意**：`return` 执行后，函数**立即结束**，后面的代码不会执行。

```python
def add(a, b):
    result = a + b
    return result       # 返回结果

total = add(3, 5)       # 接收返回值
print(total)            # 8
print(add(10, 20))      # 也可直接在 print 中使用
```

---

### 07 — 函数返回值之 None 类型

- 如果函数没有 `return`，或写了 `return` 但后面没有值，则默认返回 **`None`**。
- `None` 是 Python 中表示"空/无值"的特殊对象，类型为 `NoneType`。

```python
def say_hello():
    print("Hello")
    # 没有 return

result = say_hello()
print(result)           # None
print(type(result))     # <class 'NoneType'>
```

**None 的三种应用场景：**
```python
# 1. 函数无返回值时默认返回 None
def func(): pass
print(func())           # None

# 2. 作为 if 判断（None 等价于 False）
result = None
if not result:
    print("result 为空")

# 3. 声明一个暂无数据的变量
name = None             # 先声明，后赋值
```

---

### 08 — 函数的说明文档

- **说明文档（Docstring）**：用三引号写在函数体第一行，说明函数的功能、参数和返回值。
- 在 PyCharm 中将鼠标悬停在函数上，可以看到说明文档提示。

```python
def add(a, b):
    """
    计算两个数的和

    :param a: 第一个加数（数字类型）
    :param b: 第二个加数（数字类型）
    :return:  两数之和
    """
    return a + b
```

---

### 09 — 函数的嵌套调用

- **嵌套调用**：在一个函数的内部，调用另一个函数。
- **执行顺序**：遇到内层函数调用时，先执行完内层函数的全部代码，再继续执行外层函数。

```python
def func_b():
    print("--- func_b 开始 ---")
    print("我是 func_b")
    print("--- func_b 结束 ---")

def func_a():
    print("--- func_a 开始 ---")
    func_b()            # 调用 func_b
    print("--- func_a 结束 ---")

func_a()
# 输出：
# --- func_a 开始 ---
# --- func_b 开始 ---
# 我是 func_b
# --- func_b 结束 ---
# --- func_a 结束 ---
```

---

### 10 — 变量在函数中的作用域

**局部变量：**
- 在**函数内部**定义的变量，只在该函数内部有效，外部无法访问。

```python
def my_func():
    local_var = "我是局部变量"
    print(local_var)    # ✅ 可以访问

my_func()
# print(local_var)      # ❌ NameError，外部无法访问
```

**全局变量：**
- 在**函数外部**定义的变量，函数内部可以**读取**但不能直接修改。
- 若需在函数内**修改**全局变量，需先用 `global` 关键字声明。

```python
money = 1000            # 全局变量

def show():
    print(money)        # ✅ 读取全局变量

def spend():
    global money        # 声明要修改全局变量
    money -= 200
    print(f"消费后余额：{money}")

show()                  # 1000
spend()                 # 消费后余额：800
show()                  # 800
```

---

### 11 — 函数综合案例：ATM 模拟系统

```python
# 全局余额
balance = 5000000

def query():
    """查询余额"""
    print(f"当前余额：{balance} 元")

def deposit(amount):
    """存款"""
    global balance
    balance += amount
    print(f"存款 {amount} 元成功，当前余额：{balance} 元")

def withdraw(amount):
    """取款"""
    global balance
    if amount > balance:
        print("余额不足！")
    else:
        balance -= amount
        print(f"取款 {amount} 元成功，当前余额：{balance} 元")

def menu():
    """主菜单"""
    print("------ATM 系统------")
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出")

# 主程序
while True:
    menu()
    choice = int(input("请选择操作："))
    if choice == 1:
        query()
    elif choice == 2:
        amt = int(input("请输入存款金额："))
        deposit(amt)
    elif choice == 3:
        amt = int(input("请输入取款金额："))
        withdraw(amt)
    elif choice == 4:
        print("感谢使用，再见！")
        break
    else:
        print("无效选项，请重新输入")
```

---

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
