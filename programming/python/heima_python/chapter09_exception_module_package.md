# 第九章 Python 异常、模块与包

> 本文根据B站黑马程序员Python教程整理

---

## 一、异常

### 1.1 了解异常的概念

- **什么是异常**：当检测到一个错误时，Python解释器就无法继续执行了，反而出现错误提示，这就是所谓的"异常"，也就是常说的BUG。

- **异常演示**：以`r`方式打开不存在的文件会直接触发异常：
  ```python
  f = open('linux.txt', 'r')
  ```

### 1.2 异常的捕获方法

捕获异常的作用：提前假设某处会出现异常并做好预案，当异常真的发生时可以有后续处理手段。

#### 1.2.1 捕获常规异常

**基本语法：**
```python
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
```

**快速入门案例**：尝试以r模式打开文件，文件不存在则以w方式打开：
```python
try:
    f = open('linux.txt', 'r')
except:
    f = open('linux.txt', 'w')
```

#### 1.2.2 捕获指定异常

> 注意：
> ① 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
> ② 一般try下方只放一行尝试执行的代码。

**基本语法：**
```python
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
```

#### 1.2.3 捕获多个异常

捕获多个异常时，将异常类型放到except后，用元组形式书写：
```python
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')
```

#### 1.2.4 捕获异常并输出描述信息

**基本语法：**
```python
try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    print(e)
```

#### 1.2.5 捕获所有异常

**基本语法**（用`Exception`作为通用异常类型）：
```python
try:
    print(name)
except Exception as e:
    print(e)
```

#### 1.2.6 异常else分支

`else`表示**没有异常时要执行的代码**：
```python
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')
```

#### 1.2.7 异常finally分支

`finally`表示**无论是否发生异常都要执行的代码**，常用于资源释放（如关闭文件）：
```python
try:
    f = open('test.txt', 'r')
except Exception as e:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()
```

### 1.3 异常的传递

异常具有传递性：
- 当函数`func01`发生异常且未捕获时，异常会传递到调用它的函数`func02`
- 如果`func02`也未捕获，最终会传递到入口函数（如`main`）
- 若所有函数都未处理则程序直接报错

> 提示：当所有函数都没有捕获异常的时候，程序就会报错。

---

## 二、Python模块

### 2.1 模块的导入

#### 2.1.1 什么是模块

- **定义**：Python模块是`.py`结尾的Python文件，可定义函数、类、变量，也可包含可执行代码。
- **作用**：每个模块相当于一个工具包，可帮助我们快速实现特定功能，例如时间相关功能可使用`time`模块。

#### 2.1.2 模块的导入方式

模块使用前需先导入，常用导入形式如下：

##### （1）`import 模块名`

**基本语法：**
```python
import 模块名
import 模块名1, 模块名2  # 同时导入多个模块
模块名.功能名()  # 调用功能
```

**案例**：导入time模块
```python
import time

print("开始")
time.sleep(1)  # 阻塞1秒
print("结束")
```

##### （2）`from 模块名 import 功能名`

**基本语法：**
```python
from 模块名 import 功能名
功能名()  # 无需加模块名前缀
```

**案例**：导入time模块的sleep方法
```python
from time import sleep

print("开始")
sleep(1)
print("结束")
```

##### （3）`from 模块名 import *`

**基本语法**（导入模块所有功能）：
```python
from 模块名 import *
功能名()
```

**案例**：导入time模块所有方法
```python
from time import *

print("开始")
sleep(1)
print("结束")
```

##### （4）`import 模块名 as 别名`

给模块定义别名，简化调用：
```python
import time as tt

tt.sleep(2)
print('hello')
```

##### （5）`from 模块名 import 功能名 as 别名`

给具体功能定义别名：
```python
from time import sleep as sl

sl(2)
print('hello')
```

### 2.2 自定义模块

> 注意：每个Python文件都可以作为模块，模块名就是文件名，必须符合标识符命名规则。

**案例**：新建`my_module1.py`文件，定义test函数。

#### 2.2.1 测试模块 `__main__`

用`if __name__ == '__main__':` 可以限制代码只在当前文件运行时执行，被导入时不执行：
```python
def test(a, b):
    print(a + b)

# 仅当前文件运行时会执行test(1,1)，被其他文件导入时不执行
if __name__ == '__main__':
    test(1, 1)
```

> 注意事项：如果导入多个模块且存在同名功能，调用时会生效**最后导入的模块**的功能。

#### 2.2.2 `__all__`变量

如果模块中定义了`__all__`列表，使用`from xxx import *`时，只会导入`__all__`中声明的元素。

---

## 三、Python包

### 3.1 自定义包

#### 什么是Python包

- **物理层面**：包是一个包含`__init__.py`文件的文件夹，可存放多个模块文件。
- **逻辑层面**：包的本质依然是模块。
- **作用**：当模块数量增多时，用包可以规范管理模块。

#### 3.1.1 快速入门

**创建步骤：**
1. 新建包`my_package`
2. 包内新建模块`my_module1`、`my_module2`
3. 编写模块代码

**PyCharm操作路径**：`[New] => [Python Package] => 输入包名 => [OK] => 新建模块`

> 注意：新建包后会自动生成`__init__.py`文件，该文件控制包的导入行为。

#### 3.1.2 导入包

##### 方式一：直接导入包内模块
```python
import 包名.模块名
包名.模块名.目标功能()
```

##### 方式二：通配符导入（需配合`__init__.py`）

> 必须在包的`__init__.py`中添加`__all__ = [允许导入的模块列表]`，否则`import *`无法生效：
```python
from 包名 import *
模块名.目标功能()
```

---

## 四、安装第三方包

Python生态有大量第三方包可提高开发效率，常用包包括：
- 科学计算：`numpy`
- 数据分析：`pandas`
- 大数据计算：`pyspark`、`apache-flink`
- 图形可视化：`matplotlib`、`pyecharts`
- 人工智能：`tensorflow`等

### 4.1 用PIP安装第三方包

Python内置pip工具可直接安装第三方包，命令提示符中输入：
```bash
# 默认从官方源安装
pip install 包名称

# 使用清华国内源加速安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
```

### 4.2 用PyCharm安装第三方包

在PyCharm中可通过图形界面安装第三方包：
1. 打开设置：`File => Settings => Project => Python Interpreter`
2. 点击`+`号
3. 搜索并安装所需包

---

## 总结

以上就是Python异常、模块与包的全部核心内容：
- **异常**：捕获和处理异常（try-except-else-finally）
- **模块**：导入和使用自定义模块、系统模块
- **包**：组织和管理多个模块
- **第三方包**：使用pip安装和管理的外部包
