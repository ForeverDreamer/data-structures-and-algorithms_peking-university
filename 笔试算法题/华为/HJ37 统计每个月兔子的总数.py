"""
HJ37 统计每个月兔子的总数

描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？

本题有多组数据。

数据范围：每组输入满足 1≤n≤31
输入描述：
多行输入，一行输入一个int型整数表示第n个月

输出描述：
每一行输出对应的兔子总数

示例1
输入：
1
2
3
4
5
9
输出：
1
1
2
3
5
34
"""

input_seq = ['1', '2', '3', '4', '5', '9']


# def execute(n):
#     if n < 3:
#         return 1
#     if n == 3:
#         return 2
#     rabbit_arr = [[1, 1], [2, 0]]
#     today = 4
#     while today <= n:
#         for birthday, birth_num in rabbit_arr:
#             # 是否生兔子
#             if today - birthday > 1:
#                 rabbit_arr.append([today, 0])
#         today += 1
#     return sum(rabbit_dic.values())


def fib(n):
    if n <= 2:
        return 1
    return fib(n-2)+fib(n-1)


def count_rabbit(seq):
    output_seq = []
    for n in seq:
        n = int(n)
        output_seq.append(fib(n))
    return output_seq


for item in count_rabbit(input_seq):
    print(item)
