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
