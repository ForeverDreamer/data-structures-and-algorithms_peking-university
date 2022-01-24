"""
HJ62 查找输入整数二进制中1的个数

描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！

数据范围： 1≤n≤2的31次方−1
输入描述：
输入一个整数

输出描述：
计算整数二进制中1的个数

示例1
输入：
5
输出：
2
说明：
5的二进制表示是101，有2个1

示例2
输入：
0
输出：
0
"""

input_seq = ['5', '0']


def execute(quotient):
    count = 0

    while quotient > 0:
        if quotient % 2 == 1:
            count += 1
        quotient = quotient // 2

    return count


def decimal_to_binary(seq):
    output_seq = []
    for n in seq:
        output_seq.append(execute(int(n)))
    for item in output_seq:
        print(item)


decimal_to_binary(input_seq)
