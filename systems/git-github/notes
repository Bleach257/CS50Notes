# Git 学习笔记

## 📁 基础终端命令

| 命令 | 说明 |
|------|------|
| `cd desktop` | 进入桌面目录（如果文件夹存储在桌面） |
| `cd 文件夹名` | 进入指定文件夹 |
| `pwd` | 显示当前所在路径 |
| `mkdir 文件夹名` | 创建新文件夹 |
| `touch 文件名` | 创建新文件 |
| `ls` | 列出当前目录的文件和文件夹 |
| `ls -la` | 列出所有文件（包含隐藏文件，如 `.git` 文件夹） |
| `clear` | 清空终端屏幕 |

> 💡 **小技巧**：在 `git init` 之前先输入 `ls -la`，可以查看是否已存在 `.git` 隐藏文件夹，避免重复初始化。

---

## 🚀 创建仓库的两种方式

### 方式1：本地初始化
```bash
git init
```
在当前目录创建一个新的本地 Git 仓库，会生成一个隐藏的 `.git` 文件夹。

### 方式2：从云端克隆
```bash
git clone <仓库链接>
```
将远程仓库完整下载到本地，包含所有历史记录。

---

## 🔍 查看状态

```bash
git status
```
查看当前哪些文件被修改、哪些已暂存、哪些未被追踪。

---

## ➕ 添加文件到暂存区（git add）

| 命令 | 说明 |
|------|------|
| `git add .` | 暂存**当前目录及其子目录**下所有变更（包括新增、修改、删除） |
| `git add --all` 或 `git add -A` | 暂存**整个仓库**所有变更，包括新增文件夹 |
| `git add *` | 暂存新增和修改的文件，**不包含**已删除的文件 |
| `git add 文件名` | 只暂存指定的单个文件 |
| `git add *.txt` | 暂存当前目录下所有 `.txt` 文件（不含已删除） |

> ⚠️ **区别总结**：
> - `git add .` → 当前目录范围，包含删除
> - `git add *` → 当前目录范围，不含删除
> - `git add -A` → 整个仓库范围，包含删除

---

## 💾 提交（git commit）

```bash
git commit -m "描述本次修改的内容"
```
将暂存区的内容正式保存为一次提交，`-m` 后面填写提交说明。

---

## ↩️ 撤销操作

| 命令 | 说明 |
|------|------|
| `git reset` | 将所有已暂存的文件退回到未暂存状态（不丢失修改内容） |
| `git reset --hard` | ⚠️ **危险**：彻底回退到上一次提交，所有未提交的修改将永久丢失 |
| `git restore 文件名` | 撤销工作区中指定文件的修改（恢复到上次提交的状态） |
| `git restore --staged .` | 将暂存区的所有文件退回到未暂存状态（保留修改内容） |
| `git restore --staged 文件名` | 将指定文件从暂存区退回到未暂存状态 |

---

## 🗑️ 删除文件（git rm）

| 命令 | 说明 |
|------|------|
| `git rm 文件名` | 从暂存区和工作目录同时删除文件 |
| `git rm -f 文件名` | 强制删除（文件已修改或已暂存时使用） |
| `git rm --cached 文件名` | **只从暂存区移除**，保留本地文件（常用于取消追踪） |
| `git rm -r 文件夹名` | 递归删除整个文件夹 |

---

## 🌿 分支管理（git branch）

```bash
git branch                  # 查看所有本地分支
git branch 分支名            # 创建新分支
git branch -d 分支名         # 删除分支（已合并才能删）
git branch -D 分支名         # 强制删除分支
```

---

## 🔀 切换分支（git checkout）

```bash
git checkout 分支名          # 切换到指定分支
git checkout -b 分支名       # 创建并立即切换到新分支
git checkout 文件名          # 撤销指定文件的修改（旧版写法）
```

> 💡 新版 Git 推荐使用 `git switch` 切换分支，`git restore` 撤销文件修改。

---

## 📜 查看历史（git log）

```bash
git log                     # 查看完整提交历史
git log --oneline           # 简洁版，每条提交只显示一行
git log --oneline --graph   # 图形化显示分支结构
git log -5                  # 只显示最近5条提交
```

---

## 🔎 查看差异（git diff）

```bash
git diff                    # 查看工作区与暂存区的差异
git diff --staged           # 查看暂存区与上次提交的差异
git diff 分支1 分支2         # 比较两个分支的差异
```

---

## 🌐 远程仓库操作

```bash
git remote add origin <链接>    # 关联远程仓库
git remote -v                   # 查看已关联的远程仓库
git push -u origin main         # 首次推送，设置追踪关系
git push                        # 后续推送
```

### pull = fetch + merge

```bash
git fetch                   # 从远程拉取最新内容，但不合并到本地
git merge                   # 将拉取的内容合并到当前分支
git pull                    # = fetch + merge，直接拉取并合并
```

---

## ⚙️ 全局配置（git config）

```bash
git config --global user.email "你的邮箱"
git config --global user.name "你的用户名"
git config --list            # 查看所有配置
```

---

## 🧠 常用命令速查表

```
初始化    git init
克隆      git clone <链接>
状态      git status
暂存      git add .
提交      git commit -m "说明"
推送      git push
拉取      git pull
分支      git branch / git checkout
日志      git log --oneline
差异      git diff
撤销暂存  git restore --staged .
撤销修改  git restore 文件名
```
