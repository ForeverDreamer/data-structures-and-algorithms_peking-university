"""
HJ100 等差数列

描述
等差数列 2，5，8，11，14。。。。
（从 2 开始的 3 为公差的等差数列）
输出求等差数列前n项和

本题有多组输入

数据范围： 1≤n≤1000
输入描述：
输入一个正整数n。

输出描述：
输出一个相加后的整数。

示例1
输入：
2
复制
输出：
7
复制
说明：
2+5=7
示例2
输入：
275
复制
输出：
113575
复制
说明：
2+5+...+821+824=113575
"""

# 代码1
# while True:
#     try:
#         s=int(input())
#         w=3*s+2
#         L=range(2,w,3)
#         print(sum(L))
#     except:
#         break


# 代码2
# def func(a0,d,n):
#     an = a0 + (n - 1) * d
#     return (a0 + an)/2*n
#
# while True:
#     try:
#         a = int(input())
#         b = func(2,3,a)
#         print(int(b))
#     except:
#         break


# 代码3
# while True:
#     try:
#         x = int(input())
#         s = 0
#         for i in range(x):
#             s += i*3 + 2
#         print(int(s))
#     except:
#         break
