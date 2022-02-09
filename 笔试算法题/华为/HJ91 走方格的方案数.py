"""
HJ91 走方格的方案数

描述
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。

注：沿棋盘格之间的边缘线行走

本题含有多组样例输入。

数据范围： 1≤n,m≤8


输入描述：
每组样例输入两个正整数n和m，用空格隔开。(1≤n,m≤8)

输出描述：
每组样例输出一行结果

示例1
输入：
2 2
1 2
复制
输出：
6
3
"""

# 代码1
#动态规划解决
#nowcoder不能导入numpy模块，只能手工创建二维数组
#重点注意二维数据的创建方法，重点注意其横竖坐标，注意注意
#dp = [[1 for i in range(n+1)] for j in range(m+1)]，横坐标是 n, 竖坐标是m
# while True:
#     try:
#         n,m = map(int, input().split(' '))
#         dp = [[1 for i in range(n+1)] for j in range(m+1)]
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 dp[i][j] = dp[i-1][j]+dp[i][j-1]
#         print(dp[m][n])
#     except:
#         break


# 代码2
# def func(x,y):
#     if x < 0 or y < 0:
#         return 0
#     elif x == 0 or y == 0:
#         return 1
#     else:
#         return func(x-1, y)+func(x, y-1)
#
# while True:
#     try:
#         a,b = map(int,input().split())
#         c = func(a, b)
#         print(c)
#     except:
#         break

