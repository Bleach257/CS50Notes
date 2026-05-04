# 二阶段 第一章 Python 面向对象

> 本文根据B站黑马程序员Python教程整理

---

## 一、初识对象

使用对象组织数据：在程序中可以做到和生活中那样，设计表格、生产表格、填写表格的组织形式。

1. **在程序中设计表格**，称之为：**设计类（class）**
```python
class Student:
    name = None
```

2. **在程序中生产表格**，称之为：**创建对象**
```python
# 基于类创建对象
stu1 = Student()
stu2 = Student()
```

3. **在程序中填写表格**，称之为：**对象属性赋值**
```python
stu1.name = '111'
stu2.name = '111'
```

---

## 二、成员方法

### 2.1 类的定义和使用

**类的使用语法：**
- `class`是关键字，表示要定义类了
- 类的属性：定义在类中的变量（成员变量）
- 类的行为：定义在类中的函数（成员方法）

```python
class 类名称:
    类的属性
    类的行为
```

**创建类对象的语法：**
```python
对象 = 类名称()
```

### 2.2 成员变量和成员方法

- 类中定义的属性（变量）：**成员变量**
- 类中定义的行为（函数）：**成员方法**

#### 2.2.1 成员方法的定义语法

```python
def 方法名(self, 行参1, ..., 行参n):
    方法体
```

**`self`关键字说明：**
- 用来表示类对象自身的意思
- 使用类对象调用方法时，`self`会自动被Python传入
- 方法内部访问类的成员变量，必须使用`self`

**示例：**
```python
def say_hi(self):
    print(f"hi大家好，我是{self.name}")
```

> 注意事项：`self`关键字尽管在参数列表中，但是传参的时候可以忽略它。

---

## 三、类和对象

基于类创建对象的语法：
```python
对象名 = 类名称()
```

---

## 四、构造方法

Python类可以使用`__init__()`方法，称之为**构造方法**，可以实现：

1. 创建类对象（构造类）的时候，会自动执行。
2. 创建类对象（构造类）的时候，将传入参数自动传递给`__init__`方法使用。

> 在构造方法内定义成员变量，需要使用`self`关键字

**示例：**
```python
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

stu = Student('天天', 30, '1111')
```

---

## 五、其它内置方法（魔术方法）

上文学习的`__init__`构造方法是Python类内置方法之一，这些内置类方法各有特殊功能，统称为**魔术方法**。

| 方法 | 功能 |
|------|------|
| `__init__` | 构造方法，用于创建类对象的时候设置初始化行为 |
| `__str__` | 用于实现类对象转字符串的行为 |
| `__lt__` | 用于2个类对象进行小于或大于比较 |
| `__le__` | 用于2个类对象进行小于等于或大于等于比较 |
| `__eq__` | 用于2个类对象进行相等比较 |

### 5.1 `__str__` 字符串方法

默认类对象转字符串会输出内存地址，通过`__str__`方法可以控制类转换为字符串的行为：

- 方法名：`__str__`
- 返回值：字符串
- 内容：自行定义

**示例：**
```python
class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
```

### 5.2 `__lt__` 小于符号比较方法

直接对2个对象进行比较是不允许的，但是在类中实现`__lt__`方法，即可同时支持`<`和`>`两种比较。

> 比较大于符号的魔术方法是`__gt__`，不过实现了`__lt__`后，`__gt__`就没必要实现了。

- 方法名：`__lt__`
- 传入参数：`other`（另一个类对象）
- 返回值：`True` 或 `False`
- 内容：自行定义

### 5.3 `__le__` 小于等于比较符号方法

魔术方法`__le__`可用于`<=`、`>=`两种比较运算符。

> 实现`>=`的魔术方法是`__ge__`，实现`__le__`后`__ge__`无需再实现。

- 方法名：`__le__`
- 传入参数：`other`（另一个类对象）
- 返回值：`True` 或 `False`
- 内容：自行定义

### 5.4 `__eq__` 相等比较运算符实现方法

不实现`__eq__`方法时，对象之间`==`比较的是内存地址，不同对象的`==`结果一定是`False`。

实现`__eq__`方法后，可以按照自定义逻辑判断两个对象是否相等。

- 方法名：`__eq__`
- 传入参数：`other`（另一个类对象）
- 返回值：`True` 或 `False`
- 内容：自行定义

---

## 六、封装

### 面向对象的三大特性

1. 封装
2. 继承
3. 多态

封装表示将现实世界事物的**属性**、**行为**封装到类中，分别对应类中的：
- 成员变量
- 成员方法

### 6.1 私有成员

现实事物有不公开的属性和行为，类中通过私有成员支持这一特性：

- 私有成员变量：变量名以`__`开头（2个下划线）
- 私有成员方法：方法名以`__`开头（2个下划线）

**示例：**
```python
class Phone:
    __is_5g_enable = False  # 私有成员变量

    def __check_5g(self):  # 私有成员方法
        print('5g开启')
```

#### 练习：设计带有私有成员的手机

```python
# 设计带有私有成员的手机
import random

class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print('5g开启')
        else:
            print('5g关闭，使用4g网络')

    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中...')

phone: Phone = Phone()
phone.call_by_5g()

a = random.randint(1,2)
```

---

## 七、继承

1. **继承定义**：一个类继承另外一个类的成员变量和成员方法。
2. **语法**：子类构建的类对象可以拥有自己的成员变量和成员方法，也可以使用父类的成员变量和成员方法。
3. **分类**：
   - 单继承：一个类继承另一个类
   - 多继承：一个类继承多个类，按照顺序从左向右依次继承；多继承中如果父类有同名方法或属性，先继承的优先级高于后继承。
4. `pass`关键字：占位语句，用来保证函数（方法）或类定义的完整性，表示无内容、空的意思。

### 7.1 继承的基础语法

#### 7.1.1 单继承

```python
class 类名(父类名):
    类内容体
```

继承会将父类的成员变量和成员方法（不含私有）复制给子类。

#### 7.1.2 多继承

```python
class 类名(父类1，父类2，...., 父类n):
    类内容体
```

> 多继承注意事项：多个父类中如果有同名的成员，默认以继承顺序（从左到右）为优先级，先继承的保留，后继承的被覆盖。

### 7.2 复写和使用父类成员

#### 7.2.1 复写

复写指子类继承父类的成员属性和成员方法后，如果对其"不满意"，可以进行复写：在子类中重新定义同名的属性或方法即可。

**示例：**
```python
class FileReader:
    def read_file(self):
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们封装到list"""
        pass

# 文本文件的读取
class TextFileRead(FileReader):
    def __init__(self, path):
        self.path = path    # 定义文件路径

    # 复写父类的方法
    def read_file(self):
        print('11111')
```

#### 7.2.2 调用父类同名成员

一旦复写父类成员，类对象调用成员时会调用复写后的新成员。如果需要使用被复写的父类成员，需要特殊调用方式：

1. **方式1**：通过父类名调用
   - 使用成员变量：`父类名.成员变量`
   - 使用成员方法：`父类名.成员方法(self)`

2. **方式2**：通过`super()`调用
   - 使用成员变量：`super().成员变量`
   - 使用成员方法：`super().成员方法()`

> 注意：这两种方式只能在子类内调用父类的同名成员，子类的类对象直接调用会调用子类复写的成员。

---

## 八、类型注解

### 8.1 变量的类型注解

1. **基础语法**：`变量: 类型`

> 注意：
> - 元组类型设置类型详细注解，需要将每一个元素都标记出来
> - 字典类型设置类型详细注解，需要2个类型，第一个是key类型，第二个是value类型

2. **注释中类型注解语法**：`# type: 类型`

### 8.2 函数（方法）的类型注解

- **形参类型注解语法**：
```python
def 函数方法名(形参名：类型，形参名：类型,.....):
    pass
```

- **返回值类型注解语法**：
```python
def 函数方法名(形参名：类型，形参名：类型,.....) -> 返回值类型:
    pass
```

**示例：**
```python
def read_file(x: int, y: int) -> list[int]:
    pass
```

### 8.3 Union类型

`Union`用于标注变量/参数可以是多种类型中的一种：

1. 导包：`from typing import Union`
2. 使用：`Union[类型, ......, 类型]`

---

## 九、多态

多态指**多种状态**，即完成某个行为时，使用不同的对象会得到不同的状态。

### 9.1 抽象类（接口）

抽象类的设计含义：
- 父类用来确定有哪些方法
- 具体的方法实现由子类自行决定

**相关定义：**
- **抽象类**：含有抽象方法的类称之为抽象类
- **抽象方法**：方法体是空实现的（`pass`）称之为抽象方法

**抽象类的作用：**
1. 多用于做顶层设计（设计标准），以便子类做具体实现。
2. 是对子类的一种软性约束，要求子类必须复写（实现）父类的抽象方法。
3. 配合多态使用，获得不同的工作状态。

---

## 十、案例：数据分析案例

### main.py

```python
"""
    面向对象，数据案例分析
"""
from pyecharts.charts import Line, Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

from file_define import TextFileRead, JsonFileReader, FileReader
from data_define import Record

text_file_reader = TextFileRead('./data/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('./data/2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_file()
feb_data: list[Record] = json_file_reader.read_file()

# 将两个月份的数据合并为一个list
all_data: list[Record] = jan_data + feb_data

# 数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期有记录，做累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)

bar.render('每日销售额echarts.html')
```

### file_define.py

```python
"""
    和文件相关的类定义
"""
import json

from data_define import Record

class FileReader:
    def read_file(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们封装到list"""
        pass

# 文本文件的读取
class TextFileRead(FileReader):
    def __init__(self, path):
        self.path = path    # 定义文件路径

    # 复写父类的方法
    def read_file(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip() # 消除空格和换行
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

# Json文件的读取
class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path    # 定义文件路径

    def read_file(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == "__main__" :
    text_file = TextFileRead('./data/2011年1月销售数据.txt')
    text_json = JsonFileReader('./data/2011年2月销售数据JSON.txt')
    list1 = text_file.read_file()
    list2 = text_json.read_file()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
```

### data_define.py

```python
"""
    数据定义的类
"""
class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date    # 订单日期
        self.order_id = order_id    # 订单ID
        self.money = money  # 订单金额
        self.province = province    # 销售省份

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
```

---

## 总结

以上就是Python面向对象的全部核心内容：
- **初识对象**：类和对象的基础概念
- **成员方法**：类中定义的函数，使用self关键字
- **构造方法**：`__init__()`用于初始化对象
- **魔术方法**：`__str__`、`__lt__`、`__le__`、`__eq__`等
- **封装**：私有成员（`__`开头）
- **继承**：单继承、多继承、方法复写
- **类型注解**：变量、函数参数、返回值的类型标注
- **多态**：抽象类、抽象方法
- **综合案例**：面向对象数据分析实战
