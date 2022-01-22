"""
HJ45 名字的漂亮度

描述
给出一个名字，该名字有26个字符组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。

给出多个名字，计算每个名字最大可能的“漂亮度”。

本题含有多组数据。

数据范围：输入的名字长度满足 1≤n≤10000

输入描述：
整数N，后续N个名字

输出描述：
每个名称可能的最大漂亮程度

示例1
输入：
2
zhangsan
lisi
输出：
192
101

解题思路：
每个名字漂亮度最大，也就是对于每个名字里面出现最多的赋值最大的数字，依次类推
"""

input_seq = ['2', 'zhangsan', 'lisi']


def execute(name):
    chars = set(name.lower())  # 用set去重，找到不同字母
    maximum = 0  # 存漂亮度
    char_counts = []
    for c in chars:
        char_counts.append(name.count(c))
    char_counts.sort(reverse=True)  # 降序排序
    for i in range(len(char_counts)):
        maximum += char_counts[i] * (26 - i)  # char_counts降序，所以[0]是出现次数最多的，次数乘26，[1]是第二多，乘（26-1）
    return maximum


def beautiful_degree(seq):
    output_seq = []
    n = int(seq[0])
    i = 1
    while i <= n:
        output_seq.append(execute(seq[i]))
        i += 1
    return output_seq


for item in beautiful_degree(input_seq):
    print(item)
