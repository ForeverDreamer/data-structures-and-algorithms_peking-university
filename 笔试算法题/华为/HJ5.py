"""
HJ5 进制转换

描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在

注意本题有多组输入
输入描述：
输入一个十六进制的数值字符串。注意：一个用例会同时有多组输入数据，请参考帖子https://www.nowcoder.com/discuss/276处理多组输入的问题。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。

示例1
输入：
0xA
0xAA
输出：
10
170
"""

import sys

input_seq = ['0xAb', '0xCd']

# input_seq = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line == '':
#         break
#     input_seq.append(line)

output_seq = []
tokens = '0123456789ABCDEF'


def hex_to_decimal(hex_str):
    hex_str = hex_str[:1:-1].upper()
    result = 0
    power = 0
    for s in hex_str:
        result += tokens.index(s) * 16**power
        power += 1
    output_seq.append(result)


for item in input_seq:
    hex_to_decimal(item)

for item in output_seq:
    print(item)
