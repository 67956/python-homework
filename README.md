# Python 课程作业

这是我在「大数据平台与编程实践B」这门课上的 Python 作业，基本信息如下：

- 学号：20244080329
- 姓名：吴卓斯
- 专业：数据科学与大数据技术
- 学校：南华大学

## 这个仓库里都有什么

| 文件 | 是干什么的 |
| --- | --- |
| `20244080329_吴卓斯_hw01.ipynb` | HW01 作业：数据类型、函数与条件，包含欧几里得 gcd、欧拉数 e、整数幂判定 |
| `20244080329_吴卓斯_exp01.ipynb` | EXP01 实验：Python 基础与数据处理，一共 5 个小实验 |
| `build_notebooks.py` | 用来生成上面两份 Notebook 的脚本，是它们的“源头” |
| `student_utils.py` | EXP01 实验四用到的学生数据解析模块（运行 Notebook 时自动生成） |
| `exp01_data/` | EXP01 实验四的数据文件夹，里面有 `students.txt`、`report.txt`、`students.pkl` |

## 运行环境

作业是在一个独立的 conda 环境里完成的，环境名叫 `pycourse`，用的是 Python 3.11，需要的包有 `jupyter`、`nbconvert`、`nbformat`、`ipykernel`。

如果想在自己电脑上搭一个一样的环境，照着下面执行就行：

```bash
conda create -n pycourse python=3.11 jupyter nbconvert nbformat ipykernel -y
conda activate pycourse
```

## 怎么运行

在当前目录下，按顺序执行下面两条命令，就可以把两份 Notebook 从头到尾跑一遍。注意 EXP01 要在本目录下运行，因为它会在当前目录生成 `student_utils.py` 和 `exp01_data/`：

```bash
jupyter nbconvert --to notebook --execute --inplace 20244080329_吴卓斯_hw01.ipynb
jupyter nbconvert --to notebook --execute --inplace 20244080329_吴卓斯_exp01.ipynb
```

## 作业内容大致是这样

- **HW01（作业1）**：先写几个热身函数（`say_hi` / `goatPad` / `print_n`）热热身；然后用欧几里得算法求最大公约数，顺带处理了负数的情况；再用几种办法一点点逼近欧拉数 e；最后判断一个数是不是 2 的幂，并推广成判断是不是任意数的幂（`is_power_of_2` / `is_power`）。
- **EXP01（实验1）** 一共五块：
  1. 熟悉数据类型和字符串怎么用；
  2. 练习函数、条件判断、循环和递归；
  3. 用列表、字典、元组做点简单统计；
  4. 练习文件读写、异常处理和模块，包括解析学生成绩、算平均分和及格率、用 pickle 存取数据；
  5. 认识类和继承，顺便对比一下浅拷贝和深拷贝的区别。
