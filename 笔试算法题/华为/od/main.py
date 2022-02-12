#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys

input_seq = []

for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))