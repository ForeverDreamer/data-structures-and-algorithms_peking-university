"""
HJ57 高精度整数加法

描述
输入两个用字符串 str 表示的整数，求它们所表示的数之和。

本题含有多组样例输入。

数据范围： 1≤len(str)≤10000
输入描述：
输入两个字符串。保证字符串只含有'0'~'9'字符

输出描述：
输出求和后的结果

示例1
输入：
9876543210
1234567890
输出：
11111111100
"""

input_seq = ['9876543210', '1234567890']


def execute(n1, n2):
    return n1 + n2


def integer_addition(seq):
    output_seq = []
    i = 0
    while i+1 < len(seq):
        n1 = int(seq[i])
        n2 = int(seq[i+1])
        output_seq.append(execute(n1, n2))
        i += 2
    for item in output_seq:
        print(item)


integer_addition(input_seq)
