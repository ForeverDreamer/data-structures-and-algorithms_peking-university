"""
HJ8 合并表记录

描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
然后输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

示例1
输入：
4
0 1
0 2
1 2
3 4
输出：
0 3
1 2
3 4

示例2
输入：
3
0 1
0 2
8 9
输出：
0 3
8 9
"""

# import sys

# input_seq = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line == '':
#         break
#     input_seq.append(line)

input_seq = ['4', '1 2', '3 4', '0 1', '0 2', ]


def merge_keys(seq):
    n = int(seq[0])
    idx = 1
    output_dict = {}
    while idx <= n:
        k, v = seq[idx].split(' ')
        k, v = int(k), int(v)
        if k in output_dict:
            output_dict[k] += v
        else:
            output_dict[k] = v
        idx += 1
    output_seq = list(output_dict.items())
    output_seq.sort(key=lambda elem: elem[0])
    return [f'{str(k)} {str(v)}' for k, v in output_seq]


for item in merge_keys(input_seq):
    print(item)
