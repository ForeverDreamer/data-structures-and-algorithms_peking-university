"""
HJ41 称砝码

描述
现有一组砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。


注：

称重重量包括 0

本题有多组输入

数据范围：每组输入数据满足 1≤n≤10  ， 1≤mi≤2000  ， 1≤xi≤10
输入描述：
输入包含多组测试数据。
对于每组测试数据：
第一行：n --- 砝码数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
输出描述：
利用给定的砝码可以称出的不同的重量数

示例1
输入：
2
1 2
2 1
10
4 185 35 191 26 148 149 3 172 147
3 5 2 1 5 5 3 1 4 2
复制
输出：
5
3375

问题分析：
本质上属于排列组合问题，
时间复杂度：(x1+1)*(x2+1)*(x3+1)*...*(xn+1), 即O(k**n), k受xi的影响，
空间复杂度：1 + len(m) + len(x), 即2n+1, O(n)

提交会超时，应该有更优的算法实现
"""


# 牛客网答案
while True:
    try:
        n = int(input())
        m = list(map(int, input().split()))
        x = list(map(int, input().split()))
    except:
        break
    else:
        amount = []
        weights = {0, }
        for i in range(n):
            for j in range(x[i]):
                amount.append(m[i])

        for i in amount:
            for j in list(weights):
                weights.add(i + j)
        print(len(weights))


# input_seq = ['10', '4 185 35 191 26 148 149 3 172 147', '3 5 2 1 5 5 3 1 4 2']


# def execute(n, m, x, i, w, s):
#     if i >= n:
#         return
#     j = 0
#     while j <= x[i]:
#         w += m[i]*j
#         s.add(w)
#         execute(n, m, x, i+1, w, s)
#         w -= m[i]*j
#         j += 1
#
#
# def count_chars(seq):
#     output_seq = []
#     i = 0
#     while i + 2 < len(seq):
#         n = int(seq[i])
#         m = [int(m_i) for m_i in seq[i+1].split(' ')]
#         x = [int(x_i) for x_i in seq[i+2].split(' ')]
#         s = set()
#         execute(n, m, x, 0, 0, s)
#         output_seq.append(len(s))
#         i += 3
#     return output_seq
#
#
# for item in count_chars(input_seq):
#     print(item)