"""
HJ76 尼科彻斯定理

描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。

例如：

1^3=1

2^3=3+5

3^3=7+9+11

4^3=13+15+17+19

输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。
本题含有多组输入数据。
数据范围：数据组数：1≤t≤5 ，1≤m≤100
进阶：时间复杂度：O(1) ，空间复杂度：O(1)

输入描述：
输入一个int整数

输出描述：
输出分解后的string

示例1
输入：
6
复制
输出：
31+33+35+37+39+41


题目分析
题目给定一个数字n
这个数字要求立方值
求得的结果要拆成n个连续奇数和
输出这n个奇数
方法一：暴力
实现思路
我们直接从1到n^3建一个奇数列表

然后从奇数列表起点遍历，每次取n个数字和与目标数字比较

最终返回比较成功时的匹配结果
def solution(n):
    l = [i for i in range(1, n*n*n+1) if i&1]                   # 构造到n立方值的所有奇数列
    for i in range(len(l)):                                     # 暴力遍历所有的起点
        if sum(l[i:n+i]) == n*n*n:                              # 尝试结果是否为n^3
            return "+".join(map(str, l[i:n+i]))                 # 返回最终结果
    return ""

while True:
    try:
        n = int(input())
        print(solution(n))
    except:
        break
复杂度分析
时间复杂度：O(n^4)，由于建表的代价为O(n^3)，而遍历的代价又是O(n))，因此最终为四次方
空间复杂度：O(n3)，建表大小是三次方的空间开销
"""


def solution(n):
    l = [i for i in range(1, n * n * n + 1) if i & 1]  # 构造到n立方值的所有奇数列
    for i in range(len(l)):  # 暴力遍历所有的起点
        if sum(l[i:n + i]) == n * n * n:  # 尝试结果是否为n^3
            return "+".join(map(str, l[i:n + i]))  # 返回最终结果
    return ""


while True:
    try:
        n = int(input())
        print(solution(n))
    except:
        break
