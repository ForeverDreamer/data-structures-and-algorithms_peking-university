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

# 代码1
# 这道题目不是很难，但是我们必须要深刻理解题目的含义。
#
# 根据题意，我们可以知道，兔子有三种状态:
#
# （1）年龄为3个月及以上：可以生产，设为num。
#
# （2）年龄为2个月：不可以生产，设为num2。
#
# （3）年龄为1个月：不可生产，刚出生，设为num1。
#
# 我们可以先分析输入输出，可以得出，我们最开始获得的是一只一个月的兔子，并不是一只成年的兔子，因此在最初的两个月中，该兔子需要成长，不能生育，这是需要特别注意的，题目没有具体说清楚。
#
# 因此，我们可以假设num，num1，num2初始值为0，针对第n月的情况，我们可以使用for循环处理，在循环中，需要特别处理前两个月的情况，因为这两个月，没有成年的兔子可以生育，当到达第三个月以及以后时，我们可以按照正常的逻辑进行处理。
#
# 首先，我们先讨论特例的情况。当n=1时，此时三种兔子都是0，加入第一只小兔子，设num1=1；当n=2时，没有成年的兔子可以生产，此时有一只兔子的年龄增加一岁。
#
# 当n>=3时，此时，已有可以生产的成年兔子了，num2增加一月，此时成年兔子为num=num+num2，而num1中的兔子年龄增加一月，num2=num1。当月新出生的兔子num1=num。
#
# 最后输出三种兔子的总和就是最终的结果。
# while True:
#     try:
#         n = int(input())
#         num = 0
#         num1 = 0
#         num2 = 0
#         for i in range(n):
#             num += num2
#             num2 = num1
#             if num == 0 and num2 == 0:
#                 num1 = 1
#             elif num == 0 and num2 == 1:
#                 num1 = 0
#             else:
#                 num1 = num
#         print(num + num1 + num2)
#
#     except:
#         break


# 代码2
# while True:
#     try:
#         # 获取输入数据
#         data1 = int(input())
#         # 设置初值
#         # 一个月兔子个数
#         N1 = 1
#         # 两个月兔子个数
#         N2 = 0
#         # 三个月以及三个月以上兔子个数
#         N3 = 0
#         for n in range(1, data1):
#             N3 = N3 + N2
#             N2 = N1
#             N1 = N3
#         print(N1 + N2 + N3)
#     except:
#         break


# 代码3
import sys
# for s in sys.stdin:#s=input()读入数据的1行
#     month=int(s)
#     L=[]
#     for i in range(month):
#         if i<2:#前两个月都为1
#             total=1
#             L.append(total)
#         else:
#             total=L[i-1]+L[i-2]#之后均为前两个数的和
#             L.append(total)
#     print(L[-1])#最后的列表L=[1, 1, 2, 3, 5, 8, 13, 21, 34]


# input_seq = ['1', '2', '3', '4', '5', '9']


# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-2)+fib(n-1)
#
#
# def count_rabbit(seq):
#     output_seq = []
#     for n in seq:
#         n = int(n)
#         output_seq.append(fib(n))
#     return output_seq
#
#
# for item in count_rabbit(input_seq):
#     print(item)
