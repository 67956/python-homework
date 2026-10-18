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
