"""
HJ40 统计字符

描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

本题包含多组输入。

数据范围：输入的字符串长度满足 1≤n≤1000

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数

示例1
输入：
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
输出：
26
3
10
12
"""

from string import ascii_lowercase, ascii_uppercase, digits

input_seq = [r'1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][']


def execute(chars):
    l = 0
    s = 0
    d = 0
    o = 0
    for c in chars:
        if c in ascii_lowercase+ascii_uppercase:
            l += 1
        elif c in digits:
            d += 1
        elif c == ' ':
            s += 1
        else:
            o += 1
    return l, s, d, o


def count_chars(seq):
    output_seq = []
    for chars in seq:
        output_seq.append(execute(chars)[0])
        output_seq.append(execute(chars)[1])
        output_seq.append(execute(chars)[2])
        output_seq.append(execute(chars)[3])
    return output_seq


for item in count_chars(input_seq):
    print(item)
