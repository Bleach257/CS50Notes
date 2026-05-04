# 第七章 Python 文件操作

> 本文根据B站黑马程序员Python教程整理

## 一、文件的编码

计算机中常用文件编码：
- UTF-8
- GBK
- Big5
- 等

> UTF-8是目前全球通用的编码格式，除非有特殊需求，否则一律以UTF-8格式进行文件编码即可。

---

## 二、文件的读取

### 2.1 open()打开函数

> 注意：此时的`f`是open函数的文件对象，对象是Python中一种特殊的数据类型，拥有属性和方法，可以使用`对象.属性`或`对象.方法`对其进行访问，后续面向对象课程会做详细介绍。

**参数说明：**
- `name`：要打开的目标文件名的字符串（可包含文件具体路径）
- `mode`：设置打开文件的模式（访问模式）：只读、写入、追加等
- `encoding`：编码格式（推荐使用UTF-8）

**语法：**`open(name, mode, encoding)`

**示例：**
```python
f = open('./test.txt', 'r', encoding='utf-8')
```

### 2.2 mode常用的三种基础访问模式

| 模式 | 描述 |
|------|------|
| r | 以只读方式打开文件，文件指针放在文件开头，是默认模式 |
| w | 打开文件只用于写入：文件已存在则从开头编辑，原有内容会被删除；文件不存在则创建新文件 |
| a | 打开文件用于追加：文件已存在则新内容写入到已有内容之后；文件不存在则创建新文件 |

### 2.3 读操作相关方法

#### 操作汇总

| 操作 | 功能 |
|------|------|
| 文件对象 = open(file, mode, encoding) | 打开文件获得文件对象 |
| 文件对象.read(num) | 读取指定长度字节，不指定num则读取文件全部内容 |
| 文件对象.readline() | 读取一行内容 |
| 文件对象.readlines() | 读取全部行，返回列表（每行为一个元素） |
| for line in 文件对象 | 循环读取文件行，每次循环得到一行数据 |
| 文件对象.close() | 关闭文件对象，释放文件占用 |
| with open() as f | 语法糖，操作完成后自动关闭文件，避免遗漏close方法 |

#### 2.3.1 read()方法

```python
# num表示要读取的数据长度（单位是字节），无传入num则读取文件所有数据
文件对象.read(num)
```

#### 2.3.2 readlines()方法

`readlines`按行一次性读取整个文件内容，返回列表，每行数据为列表的一个元素：

```python
f = open('python.txt')

content = f.readlines()
# 输出示例：['hello world\n', 'abcdefg\n', 'aaa\n', 'bbb\n', 'ccc']
print(content)

# 关闭文件
f.close()
```

`readline()`方法：一次读取一行内容

```python
f = open('python.txt')

content = f.readline()
print(f'第一行：{content}')

content = f.readline()
print(f'第二行：{content}')

# 关闭文件
f.close()
```

**for循环读取文件行：**

```python
for line in open("python.txt", "r"):
    print(line)
# 每个line临时变量对应文件的一行数据
```

#### 2.3.3 close() 关闭文件对象

```python
f = open("python.txt", "r")
f.close()

# 调用close关闭文件对象，释放文件占用
# 若不调用close且程序未停止，文件会一直被Python程序占用
```

#### 2.3.4 with open 语法

```python
with open("python.txt", "r") as f:
    f.readlines()

# with代码块内操作文件，执行完后自动调用close，无需手动关闭
```

#### 练习案例：统计itheima单词出现次数

测试文件`test.txt`内容：
```
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima
```

实现代码：
```python
index = 0
with open('./test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        str = line.split(' ')
        print(str)
        for val in str:
            if val == 'itheima':
                index += 1

print(f'index：{index}')
```

---

## 三、文件的写入

### 3.1 写操作快速入门

> 注意：
> - 直接调用`write`，内容会先积攒在程序内存的缓冲区，不会立即写入文件
> - 调用`flush`时内容才会真正写入文件，避免频繁操作硬盘降低效率
> - 文件不存在时，使用`w`模式会创建新文件
> - 文件存在时，使用`w`模式会清空原有内容

**示例：**
```python
# 1. 打开文件
f = open('python.txt', 'w')

# 2. 文件写入
f.write('hello world')

# 3. 内容刷新，真正写入磁盘
f.flush()
```

---

## 四、文件的追加

### 4.1 追加写入操作快速入门

> 注意：
> - `a`模式下文件不存在会创建新文件
> - `a`模式下文件存在则新内容追加到原有内容之后

**示例：**
```python
# 1. 用a模式打开文件
f = open('python.txt', 'a')

# 2. 文件写入
f.write('hello world')

# 3. 内容刷新
f.flush()
```

---

## 五、文件操作综合案例：文件备份

### 原始文件`bill.txt`内容

```
name,date,money,type,remarks
周杰轮,2022-01-01,100000,消费,正式
周杰轮,2022-01-02,300000,收入,正式
周杰轮,2022-01-03,100000,消费,测试
林俊节,2022-01-01,300000,收入,正式
林俊节,2022-01-02,100000,消费,测试
林俊节,2022-01-03,100000,消费,正式
林俊节,2022-01-04,100000,消费,测试
林俊节,2022-01-05,500000,收入,正式
张学油,2022-01-01,100000,消费,正式
张学油,2022-01-02,500000,收入,正式
张学油,2022-01-03,900000,收入,测试
王力鸿,2022-01-01,500000,消费,正式
王力鸿,2022-01-02,300000,消费,测试
王力鸿,2022-01-03,950000,收入,正式
刘德滑,2022-01-01,300000,消费,测试
刘德滑,2022-01-02,100000,消费,正式
刘德滑,2022-01-03,300000,消费,正式
```

### 备份需求：过滤掉备注为「测试」的行，生成备份文件`bill.txt.bak`

实现代码：
```python
f2 = open('bill.txt.bak', 'a', encoding="utf-8")
with open('bill.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        str = line.split(',')
        if str[4] == '测试':
            continue
        else:
            f2.write(f'{line}\n')

f2.close()
```

---

## 总结

以上就是Python文件操作的基础内容，包括：
- 文件的编码（推荐使用UTF-8）
- 文件的读取（read、readline、readlines、for循环读取）
- 文件的写入（write、flush）
- 文件的追加（append模式）
- 文件备份综合案例
