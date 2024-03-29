"""
HJ9 提取不重复的整数

描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围：
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入：
9876673
输出：
37689
"""

input_num = '9876673'
# input_num = input().strip()


def unique_nums(num_str):
    num = num_str[::-1]
    output_seq = []
    for n in num:
        if n not in output_seq:
            output_seq.append(n)
    return ''.join(output_seq)


print(unique_nums(input_num))
