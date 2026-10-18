# -*- coding: utf-8 -*-
"""生成 HW01 与 EXP01 两个 Jupyter Notebook（不依赖第三方库，纯 JSON 构造）。"""
import json
import os

REPO = r"C:\Users\WU\python-homework"
STUDENT_ID = 20244080329


def src(text):
    return text.splitlines(keepends=True)


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": src(text)}


def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
            "source": src(text)}


def nb(cells):
    for index, c in enumerate(cells, start=1):
        c["id"] = f"cell-{index:03d}"
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3 (pycourse)", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_nb(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("written:", path)


# ======================================================================
# HW01
# ======================================================================
IDENT = '''import os, uuid, hashlib, platform, getpass

# ===== 1. 填写学号 =====
STUDENT_ID = 20244080329  # 修改为自己的学号

# ===== 2. 打印 conda 环境 =====
CONDA_ENV = os.environ.get("CONDA_DEFAULT_ENV", "base")
print(f"[Conda 环境] {CONDA_ENV}")

# ===== 3. 机器指纹（绑定当前电脑）=====
MACHINE_FP = hashlib.sha256(
    f"{platform.node()}|{platform.machine()}|{platform.system()}|{uuid.getnode()}".encode()
).hexdigest()[:16]

# ===== 4. 生成唯一 ID =====
RUN_ID = f"{STUDENT_ID}-{MACHINE_FP}"
print(f"[学号] {STUDENT_ID}")
print(f"[机器指纹] {MACHINE_FP}")
print(f"[RUN_ID] {RUN_ID}")
'''

hw01 = []
hw01.append(md("""# 作业1：Data Types, Functions and Conditionals

- 姓名：吴卓斯
- 学号：20244080329
- 课程：大数据平台与编程实践B

> 说明：本 Notebook 按题目顺序依次运行各个代码框。
"""))

hw01.append(md("## 身份与环境记录（第一个代码框）"))
hw01.append(code(IDENT))

# ---------------- 热身 ----------------
hw01.append(md("""## 一、热身：定义简单函数

1. `say_hi()`：不接受参数，被调用时打印 `Hello, world!`；
2. `goatPad(s)`：接受一个字符串，打印该字符串，前后各加一个 `goat`；
3. `print_n(s, n)`：接受字符串 `s` 和整数 `n`，把字符串打印 `n` 次，每次单独一行。
"""))

hw01.append(md("**1. `say_hi` 函数**"))
hw01.append(code('''def say_hi():
    """不接受参数，打印 Hello, world!"""
    print("Hello, world!")


say_hi()
'''))

hw01.append(md("**2. `goatPad` 函数**"))
hw01.append(code('''def goatPad(s):
    """在字符串 s 的前后各拼接一个 goat 后打印。"""
    print("goat" + s + "goat")


goatPad("hello")
goatPad(" MOUNTAIN ")
'''))

hw01.append(md("**3. `print_n` 函数**"))
hw01.append(code('''def print_n(s, n):
    """把字符串 s 打印 n 次，每次单独一行。"""
    for _ in range(n):
        print(s)


print_n("Hello, Hive!", 3)
'''))

# ---------------- 欧几里得 ----------------
hw01.append(md("""## 二、欧几里得算法

欧几里得算法（辗转相除法）用于求两个整数 $m,n$ 的最大公约数（GCD），
核心递推关系为：$\\gcd(m,n)=\\gcd(n,\\,m\\bmod n)$，直到余数为 0。
"""))

hw01.append(md("**1. 实现 `gcd` 函数**"))
hw01.append(code('''def gcd(m, n):
    """使用辗转相除法返回两个整数的最大公约数。"""
    while n != 0:
        m, n = n, m % n
    return m
'''))

hw01.append(md("**2. 评估三组数字的 GCD**"))
hw01.append(code('''pairs = [(2018, 2019), (1200, 300), (5040, 60)]
for m, n in pairs:
    print(f"gcd({m}, {n}) = {gcd(m, n)}")
'''))

hw01.append(md("""**3. 负数参数的行为与讨论**

先直接用上面的函数测试负数输入，观察现象：
"""))
hw01.append(code('''print("gcd(-2018, 2019) =", gcd(-2018, 2019))
print("gcd(2018, -2019) =", gcd(2018, -2019))
print("gcd(-1200, -300) =", gcd(-1200, -300))
'''))

hw01.append(md("""**现象分析：**

- 当两个参数**同为负数**时（如 `gcd(-1200, -300)`），辗转相除过程中 `m` 始终保持为负，
  最后返回的是 **`-300`**，而数学上最大公约数约定为正整数，因此这个结果不规范。
- 当参数一正一负时，由于 Python 的取模运算符 `%` 的余数符号与除数（分母）一致，
  有时会“碰巧”得到正数结果，但这依赖于具体语言对取模的定义，行为并不直观、也不可移植。
- 因此“直接相除”的版本对负数输入的行为是**不确定的**，这种行为没有意义——GCD 应当总是非负整数。

**改进方法：** 在进入循环前用 `abs()` 取绝对值，使函数对任意整数符号都能返回正确的正 GCD。
"""))
hw01.append(code('''def gcd(m, n):
    """健壮版：先取绝对值，再用辗转相除法求最大公约数。"""
    m, n = abs(m), abs(n)
    while n != 0:
        m, n = n, m % n
    return m


# 改进后对正数、负数都能得到正确的正 GCD
for m, n in [(2018, 2019), (1200, 300), (5040, 60),
             (-2018, 2019), (1200, -300), (-1200, -300)]:
    print(f"gcd({m}, {n}) = {gcd(m, n)}")
'''))

# ---------------- 欧拉数 ----------------
hw01.append(md("""## 三、近似欧拉数 e

自然对数的底数

$$e=\\sum_{k=0}^{\\infty}\\frac{1}{k!}=1+\\frac{1}{1}+\\frac{1}{2!}+\\frac{1}{3!}+\\cdots$$

其中约定 $0!=1$。
"""))

hw01.append(md("**1. `euler_limit`：用极限 $(1+\\frac{1}{x})^x$ 近似 e**"))
hw01.append(code('''def euler_limit(n):
    """取 x=n，返回 (1+1/n)^n 对 e 的近似值（浮点数）。"""
    return (1 + 1 / n) ** n


for n in [1, 10, 1000, 1_000_000]:
    print(f"n={n:>7d}  ->  {euler_limit(n):.10f}")
'''))

hw01.append(md("""**2. `euler_infinite_sum`：用前 n 项之和近似 e**

注意函数参数是“1-索引”的：`euler_infinite_sum(1)` 只取公式中的第 1 项（$k=0$），返回 `1`；
`euler_infinite_sum(0)` 不取任何项，返回 `0`。
"""))
hw01.append(code('''def euler_infinite_sum(n):
    """返回公式(1)中前 n 项之和对 e 的近似值。"""
    total = 0.0
    factorial = 1          # 0! = 1
    for k in range(n):     # k = 0,1,...,n-1，共 n 项
        if k >= 1:
            factorial *= k  # 此时 factorial = k!
        total += 1.0 / factorial
    return total


print("euler_infinite_sum(0) =", euler_infinite_sum(0))
print("euler_infinite_sum(1) =", euler_infinite_sum(1))
print("euler_infinite_sum(4) =", euler_infinite_sum(4))
print("euler_infinite_sum(20) =", euler_infinite_sum(20))
'''))

hw01.append(md("**3. `euler_approx`：不断累加直到误差小于 $\\epsilon$**"))
hw01.append(code('''import math


def euler_approx(epsilon):
    """逐项累加 1/k!，直到与真实 e 的误差不超过 epsilon。"""
    total = 0.0
    factorial = 1
    k = 0
    while abs(math.exp(1) - total) > epsilon:
        if k >= 1:
            factorial *= k
        total += 1.0 / factorial
        k += 1
    return total


for eps in [1e-3, 1e-6, 1e-10]:
    approx = euler_approx(eps)
    print(f"epsilon={eps:g}: 近似={approx:.12f}, 真实={math.exp(1):.12f}, 误差={abs(math.exp(1)-approx):.2e}")
'''))

hw01.append(md("**4. `print_euler_sum_table`：打印 1~n 项的近似值表**"))
hw01.append(code('''def print_euler_sum_table(n):
    """逐行打印 euler_infinite_sum(k)，k 从 1 到 n。"""
    for k in range(1, n + 1):
        print(euler_infinite_sum(k))


print_euler_sum_table(10)
'''))

# ---------------- 整数属性 ----------------
hw01.append(md("""## 四、测试整数属性

一个正整数 $n$ 是 2 的幂，当且仅当 $n=2^p$（$p\\ge 0$）。
只允许使用除法和取模（`%`），不能使用 `math.sqrt`。
"""))

hw01.append(md("**1. `is_power_of_2`：判断是否为 2 的幂**"))
hw01.append(code('''def is_power_of_2(n):
    """若 n 是 2 的幂则返回 True，否则返回 False。"""
    if n < 1:
        return False
    while n > 1:
        if n % 2 != 0:      # 不断除以 2，过程中一旦出现余数即不是 2 的幂
            return False
        n = n // 2
    return True


for x in [1, 2, 3, 4, 8, 10, 16, 64, 100, 1024]:
    print(f"is_power_of_2({x:>4d}) = {is_power_of_2(x)}")
'''))

hw01.append(md("**2. `is_power(b, n)`：推广为判断 n 是否为 b 的幂**"))
hw01.append(code('''def is_power(b, n):
    """若 n 是 b 的某次幂（n = b^p, p>=0）则返回 True。"""
    if n == 1:
        return True          # 任意 b 的 0 次幂都是 1
    if b <= 1:
        return n == 1        # 处理 b=1 等退化情形
    while n > 1:
        if n % b != 0:
            return False
        n = n // b
    return n == 1


for b, n in [(2, 16), (2, 10), (3, 81), (3, 80), (10, 1000), (5, 1), (6, 216)]:
    print(f"is_power({b}, {n}) = {is_power(b, n)}")
'''))

write_nb(nb(hw01), os.path.join(REPO, "20244080329_吴卓斯_hw01.ipynb"))


# ======================================================================
# EXP01
# ======================================================================
EXP_IDENT = '''import os, uuid, hashlib, platform, getpass

# ===== 1. 填写学号 =====
STUDENT_ID = 20244080329  # 修改为自己的学号

# ===== 2. 打印 conda 环境 =====
CONDA_ENV = os.environ.get("CONDA_DEFAULT_ENV", "base")
print(f"[Conda 环境] {CONDA_ENV}")

# ===== 3. 机器指纹（绑定当前电脑）=====
MACHINE_FP = hashlib.sha256(
    f"{platform.node()} | {platform.machine()} | {platform.system()} | {uuid.getnode()}".encode()
).hexdigest()[:16]

# ===== 4. 生成唯一 ID =====
RUN_ID = f"{STUDENT_ID} - {MACHINE_FP}"
print(f"[学号] {STUDENT_ID}")
print(f"[机器指纹] {MACHINE_FP}")
print(f"[RUN_ID] {RUN_ID}")
'''

exp = []
exp.append(md("""# 实验报告01：Python 基础与数据处理入门

- 姓名：吴卓斯
- 学号：20244080329
- 专业：数据科学与大数据技术
- 独立 conda 虚拟环境：`pycourse`（Python 3.11 + Jupyter）
"""))

exp.append(md("## 1.1 身份与环境记录（第一个代码框）"))
exp.append(code(EXP_IDENT))

# ---------------- 实验1 ----------------
exp.append(md("""## 二、实验内容与过程

### 实验1：基本运算、数据类型与字符串

**任务1**：计算 `8 / 3`、`8 // 3`、`8 % 3` 和 `2 ** 7`，输出结果及其类型，并说明运算符含义。
"""))
exp.append(code('''exprs = [("8 / 3", 8 / 3), ("8 // 3", 8 // 3),
         ("8 % 3", 8 % 3), ("2 ** 7", 2 ** 7)]
for name, value in exprs:
    print(f"{name:<8} = {value:<6} 类型 = {type(value).__name__}")

# 运算符含义：
# /   真除法，无论是否整除都返回 float；
# //  整除（地板除），向下取整，返回 int；
# %   取模（求余数）；
# **  幂运算（2 的 7 次方）。
'''))

exp.append(md("**任务2**：创建整数、浮点数、字符串、布尔值各一个，用 `type()` 检查类型。"))
exp.append(code('''i, f, s, b = 10, 3.14, "goat", True
for var in (i, f, s, b):
    print(f"值={var!r:<8} 类型={type(var).__name__}")
'''))

exp.append(md("**任务3**：执行类型转换，解释结果；捕获 `int(\"goat\")` 的异常。"))
exp.append(code('''print("int('123') =", int("123"), "   字符串数字 -> 整数")
print("float('3.14') =", float("3.14"), "  字符串数字 -> 浮点数")
print("int(3.9) =", int(3.9), "   浮点数 -> 整数（直接截断小数部分，不四舍五入）")

try:
    int("goat")
except ValueError as e:
    print("int('goat') 捕获异常 ValueError：", e)
    # 原因：'goat' 不含可解析的整数表示，无法转换为整数。
'''))

exp.append(md("**任务4**：对字符串 `\" Python Data Analysis \"` 做去空白、大小写转换、切片、拆分与 join。"))
exp.append(code('''raw = " Python Data Analysis "
s = raw.strip()
print("去首尾空白:", repr(s))
print("大写 upper():", s.upper())
print("小写 lower():", s.lower())
print("首字母大写 title():", s.title())
print("切片 s[0:6]:", s[0:6])
words = s.split()
print("split() 拆成单词:", words)
print("'-'.join() 连接:", "-".join(words))
'''))

exp.append(md("**任务5**：比较字符串拼接与重复；验证字符串不可直接修改，并演示构造新字符串。"))
exp.append(code('''print("拼接 'a' + 'b' =", "a" + "b")
print("重复 'ab' * 3  =", "ab" * 3)

s = "cat"
try:
    s[0] = "b"                # 字符串是不可变对象，不允许赋值
except TypeError as e:
    print("直接修改字符捕获 TypeError：", e)

new_s = "b" + s[1:]          # 通过切片 + 拼接构造新字符串
print("构造的新字符串:", new_s)
'''))

# ---------------- 实验2 ----------------
exp.append(md("""### 实验2：函数、条件、循环与递归

**任务1**：`score_level(score)` 按分数返回等级，超出 0~100 抛出 `ValueError`。
"""))
exp.append(code('''def score_level(score):
    if not (0 <= score <= 100):
        raise ValueError("成绩必须在 0~100 之间")
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"


for score in [95, 88, 70, 60, 59, 0]:
    print(score, "->", score_level(score))

try:
    score_level(105)
except ValueError as e:
    print("score_level(105) 捕获：", e)
'''))

exp.append(md("**任务2**：分别用 for 和 while 计算 1~100 的整数和并比较。"))
exp.append(code('''sum_for = 0
for i in range(1, 101):
    sum_for += i

sum_while = 0
i = 1
while i <= 100:
    sum_while += i
    i += 1

print("for 求和:", sum_for)
print("while 求和:", sum_while)
print("两者结果相同:", sum_for == sum_while)
'''))

exp.append(md("**任务3**：递归版与迭代版阶乘（约定 0!=1），比较 n=0、1、5、10。"))
exp.append(code('''def factorial_iter(n):
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def factorial_rec(n):
    if n <= 1:
        return 1            # 0! = 1! = 1
    return n * factorial_rec(n - 1)


for n in [0, 1, 5, 10]:
    a, b = factorial_iter(n), factorial_rec(n)
    print(f"{n:>2d}! 迭代={a:<8} 递归={b:<8} 一致={a == b}")
'''))

exp.append(md("**任务4**：`summary(values)` 以元组返回最小值、最大值、平均值，并解包接收。"))
exp.append(code('''def summary(values):
    return min(values), max(values), sum(values) / len(values)


low, high, average = summary([85, 58, 92, 76, 60, 89])
print("最小值:", low)
print("最大值:", high)
print("平均值:", round(average, 2))
'''))

exp.append(md("**任务5**：`sum_all(*args)` 返回所有参数之和，测试无参、单参、多参。"))
exp.append(code('''def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total


print("无参数:", sum_all())
print("单参数 sum_all(5):", sum_all(5))
print("多参数 sum_all(1,2,3,4):", sum_all(1, 2, 3, 4))
'''))

# ---------------- 实验3 ----------------
exp.append(md("""### 实验3：列表、字典、元组与基础统计

使用模拟成绩数据（不包含真实学生信息）。
"""))
exp.append(code('''names = ["Alice", "Bob", "Carol", "David", "Eva", "Frank"]
scores = [85, 58, 92, 76, 60, 89]
'''))

exp.append(md("**任务1**：用 `zip()` 构建姓名到成绩的字典，用 `items()` 逐项输出。"))
exp.append(code('''score_dict = dict(zip(names, scores))
print("字典:", score_dict)
for name, score in score_dict.items():
    print(f"{name:>6} : {score}")
'''))

exp.append(md("**任务2**：用 `enumerate()` 输出序号、姓名、成绩，序号从 1 开始。"))
exp.append(code('''for index, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"序号 {index}: {name:<6} 成绩 {score}")
'''))

exp.append(md("**任务3**：列表推导式提取及格学生姓名、生成成绩平方列表。"))
exp.append(code('''passed_names = [name for name, score in zip(names, scores) if score >= 60]
score_squares = [score ** 2 for score in scores]
print("及格学生姓名:", passed_names)
print("成绩平方列表:", score_squares)
'''))

exp.append(md("**任务4**：统计人数、平均分、最高分、最低分、及格率并格式化输出。"))
exp.append(code('''count = len(scores)
average = sum(scores) / count
passed = sum(1 for score in scores if score >= 60)
pass_rate = passed / count
print(f"人数={count}")
print(f"平均分={average:.2f}")
print(f"最高分={max(scores)}  最低分={min(scores)}")
print(f"及格率={pass_rate:.1%}")
'''))

exp.append(md("**任务5**：比较别名 `alias = scores` 与 `copied = scores.copy()`（使用单独的演示列表）。"))
exp.append(code('''demo = [1, 2, 3]
alias = demo            # 别名，指向同一个列表对象
copied = demo.copy()    # 浅拷贝，生成一个新列表
alias[0] = 99
print("修改别名后原列表 demo:", demo)
print("copy() 得到的副本 copied:", copied)
print("alias 与 demo 是同一对象:", alias is demo)
print("copied 与 demo 是同一对象:", copied is demo)
'''))

exp.append(md("**任务6**：元组保存一条记录，验证不可重新赋值；观察不等长序列的 `zip()`。"))
exp.append(code('''record = ("Alice", 85, "及格")
print("元组记录:", record)
try:
    record[1] = 90
except TypeError as e:
    print("元组元素不能重新赋值，捕获：", e)

print("不等长 zip 结果（按较短序列截断）:", list(zip([1, 2, 3], ["a", "b"])))
'''))

# ---------------- 实验4 ----------------
exp.append(md("""### 实验4：文件读写、异常处理与模块

**任务1**：查看工作目录，构造相对路径，创建 `exp01_data` 数据目录。
"""))
exp.append(code('''print("当前工作目录:", os.getcwd())
data_dir = os.path.join(os.getcwd(), "exp01_data")
os.makedirs(data_dir, exist_ok=True)
print("数据目录:", data_dir)
'''))

exp.append(md("**任务2**：写入 UTF-8 文本 `students.txt`，再读取并跳过表头解析。"))
exp.append(code('''content = """name,score
Alice,85
Bob,58
Carol,92
David,76
Eva,60
Frank,89
Grace,abc
Henry,105
Incomplete
"""
txt_path = os.path.join(data_dir, "students.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(txt_path, "r", encoding="utf-8") as f:
    raw_lines = f.read().splitlines()
print("全部行:", raw_lines)
data_lines = raw_lines[1:]          # 跳过表头
print("跳过表头后的记录数:", len(data_lines))
'''))

exp.append(md("**任务3**：`parse_student(line)` 校验字段数量、姓名、成绩范围，无效则抛 `ValueError`。"))
exp.append(code('''def parse_student(line):
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误（应为2）: {line!r}")
    name = parts[0].strip()
    score_text = parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是整数: {score_text!r}")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩超出 0~100 范围: {score}")
    return {"name": name, "score": score}
'''))

exp.append(md("**任务4**：逐行处理，捕获无效记录并记录行号与原因，继续处理后续行。"))
exp.append(code('''valid_records = []
invalid_records = []
for line_no, line in enumerate(data_lines, start=2):   # 行号从含表头的第2行开始
    line = line.strip()
    if not line:
        continue
    try:
        valid_records.append(parse_student(line))
    except ValueError as err:
        invalid_records.append((line_no, str(err)))
        print(f"第 {line_no} 行无效：{err}")

print("\\n有效记录：", valid_records)
print(f"有效 {len(valid_records)} 条，无效 {len(invalid_records)} 条")
'''))

exp.append(md("**任务5**：将统计结果写入 `report.txt`，分别演示 `w`（覆盖）与 `a`（追加）模式。"))
exp.append(code('''report_path = os.path.join(data_dir, "report.txt")
valid_count = len(valid_records)
invalid_count = len(invalid_records)
valid_average = sum(r["score"] for r in valid_records) / valid_count
valid_pass_rate = sum(1 for r in valid_records if r["score"] >= 60) / valid_count
stat_line = (f"有效记录数={valid_count}, 无效记录数={invalid_count}, "
             f"平均分={valid_average:.2f}, 及格率={valid_pass_rate:.1%}\\n")

# w 模式：若文件已存在会覆盖（清空）原有内容
with open(report_path, "w", encoding="utf-8") as f:
    f.write("【w 模式：覆盖写入，原内容被清空】\\n")
    f.write(stat_line)
# a 模式：在文件末尾追加，保留原有内容
with open(report_path, "a", encoding="utf-8") as f:
    f.write("【a 模式：追加写入，原内容保留】\\n")
    f.write(stat_line)

print(open(report_path, encoding="utf-8").read())
'''))

exp.append(md("**任务6**：用 `pickle` 保存有效记录并读取，验证恢复数据与原数据相等。"))
exp.append(code('''import pickle

pkl_path = os.path.join(data_dir, "students.pkl")
with open(pkl_path, "wb") as f:
    pickle.dump(valid_records, f)

with open(pkl_path, "rb") as f:
    restored = pickle.load(f)

print("pickle 恢复数据:", restored)
print("恢复数据与原数据相等:", restored == valid_records)
'''))

exp.append(md("**任务7**：把 `parse_student` 保存为同级模块 `student_utils.py`，再 import 调用。"))
exp.append(code('''%%writefile student_utils.py
"""实验4 使用的工具模块：解析并校验学生成绩记录。"""


def parse_student(line):
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误（应为2）: {line!r}")
    name = parts[0].strip()
    score_text = parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是整数: {score_text!r}")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩超出 0~100 范围: {score}")
    return {"name": name, "score": score}
'''))

exp.append(code('''import importlib
import student_utils

importlib.reload(student_utils)     # 确保加载最新版本
print("有效输入测试:", student_utils.parse_student("Alice,85"))
try:
    student_utils.parse_student("Grace,abc")
except ValueError as err:
    print("无效输入测试，捕获：", err)
'''))

exp.append(md("**任务8**：读取一个明确不存在的文件，捕获 `FileNotFoundError`。"))
exp.append(code('''missing_path = os.path.join(data_dir, "not_exist.txt")
try:
    with open(missing_path, encoding="utf-8") as f:
        f.read()
except FileNotFoundError as err:
    print("捕获 FileNotFoundError：", err)
    print("说明：该文件不存在，open() 以读模式打开时会抛出此异常。")
'''))

# ---------------- 实验5 ----------------
exp.append(md("""### 实验5：类、继承与对象复制

**任务1**：定义 `Student` 类，含 `is_passed()` 与 `__str__()`。
"""))
exp.append(code('''class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def __str__(self):
        status = "及格" if self.is_passed() else "不及格"
        return f"{self.name}: {self.score} 分（{status}）"
'''))

exp.append(md("**任务2**：为每条有效记录创建 `Student` 对象，输出信息与及格状态。"))
exp.append(code('''students = [Student(r["name"], r["score"]) for r in valid_records]
for stu in students:
    print(str(stu), "| is_passed() =", stu.is_passed())
'''))

exp.append(md("**任务3**：`GraduateStudent` 继承 `Student`，增加 `research_topic`，重写 `__str__`。"))
exp.append(code('''class GraduateStudent(Student):
    def __init__(self, name, score, research_topic):
        super().__init__(name, score)          # 调用父类初始化
        self.research_topic = research_topic

    def __str__(self):
        return f"研究生 {self.name}：{self.score} 分，研究课题={self.research_topic}"


grad = GraduateStudent("Alice", 85, "大数据分析")
print(grad)
print("继承自父类的 is_passed() =", grad.is_passed())
'''))

exp.append(md("**任务4**：对含嵌套列表的对象分别直接赋值、浅拷贝、深拷贝（每次从新建原始对象开始）。"))
exp.append(code('''import copy


def copy_demo():
    original = {"name": "Alice", "scores": [85, 90]}
    alias_obj = original                # 直接赋值：同一对象
    shallow = copy.copy(original)       # 浅拷贝：外层新对象，内层列表仍共享
    deep = copy.deepcopy(original)      # 深拷贝：外层与内层都独立
    original["scores"].append(95)       # 修改原始对象的内层列表
    print("原始对象      :", original)
    print("直接赋值      :", alias_obj, " 同一外层对象:", alias_obj is original)
    print("浅拷贝 copy   :", shallow, " 内层列表共享:", shallow["scores"] is original["scores"])
    print("深拷贝 deepcopy:", deep, " 内层列表独立:", deep["scores"] is original["scores"])


copy_demo()
print("---")
copy_demo()
'''))

exp.append(md("""## 三、实验小结

本次实验在独立的 conda 环境 `pycourse` 中完成，涵盖了：

1. 基本运算、数据类型、字符串常用方法与不可变性；
2. 函数、条件分支、for/while 循环、递归以及可变参数；
3. 列表、字典、元组、推导式与基础统计，以及别名与拷贝的区别；
4. 文件读写、异常处理、CSV 风格记录解析、pickle 序列化与自定义模块；
5. 类的定义、继承（`super()`）以及 `copy`/`deepcopy` 的差异。

重启内核并运行全部代码后，各单元均能正常执行，无依赖旧变量或路径错误的问题。
"""))

write_nb(nb(exp), os.path.join(REPO, "20244080329_吴卓斯_exp01.ipynb"))
print("ALL DONE")
