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

