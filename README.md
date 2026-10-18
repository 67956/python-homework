# Python 课程作业

- 学号：20244080329
- 姓名：吴卓斯
- 专业：数据科学与大数据技术
- 学校：南华大学

## 目录说明

| 文件 | 内容 |
| --- | --- |
| `20244080329_吴卓斯_hw01.ipynb` | HW01：数据类型、函数与条件、欧几里得 gcd、欧拉数 e、整数幂 |
| `20244080329_吴卓斯_exp01.ipynb` | EXP01：Python 基础与数据处理（5 个实验） |
| `build_notebooks.py` | 生成上面两份 Notebook 的源脚本 |
| `student_utils.py` | EXP01 实验四：学生数据解析模块（由 Notebook 生成） |
| `exp01_data/` | EXP01 实验四数据：`students.txt`、`report.txt`、`students.pkl` |

## 运行环境

- 独立 conda 环境 `pycourse`（Python 3.11）
- 依赖：`jupyter`、`nbconvert`、`nbformat`、`ipykernel`

复现环境：

```bash
conda create -n pycourse python=3.11 jupyter nbconvert nbformat ipykernel -y
conda activate pycourse
```

## 执行方式

在本目录下依次执行（EXP01 依赖当前工作目录，以生成 `student_utils.py` 与 `exp01_data/`）：

```bash
jupyter nbconvert --to notebook --execute --inplace 20244080329_吴卓斯_hw01.ipynb
jupyter nbconvert --to notebook --execute --inplace 20244080329_吴卓斯_exp01.ipynb
```

## 实验内容概要

- **HW01**：热身函数（`say_hi`/`goatPad`/`print_n`）、欧几里得算法求最大公约数（含负数处理）、三种方式逼近欧拉数 e、整数幂判定（`is_power_of_2`/`is_power`）。
- **EXP01**：
  1. 数据类型与字符串；
  2. 函数、条件、循环与递归；
  3. 列表/字典/元组统计；
  4. 文件读写、异常处理与模块（学生成绩解析、平均成绩、及格率、pickle 序列化）；
  5. 类、继承与 `copy` 浅/深拷贝对比。
