"""
HJ97 记负均正

描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。
0即不是正整数，也不是负数，不计入计算

数据范围： 1≤n ≤2000  ，输入的整数都满足 ∣val∣≤1000
输入描述：
本题有多组输入用例。
首先输入一个正整数n，
然后输入n个整数。

输出描述：
输出负数的个数，和所有正整数的平均值。

示例1
输入：
5
1 2 3 4 5
10
1 2 3 4 5 6 7 8 9 0
复制
输出：
0 3.0
0 5.0
复制
示例2
输入：
3
0 0 0
复制
输出：
0 0.0
"""

while True:
    try:
        n = int(input())
        nums = map(int, input().split())
        positive = []
        negative = 0
        for j in nums:
            if j > 0:
                positive.append(j)
            elif j < 0:
                negative += 1
            else:
                pass
        res = float(0.0)
        for i in range(len(positive)):
            res += positive[i]
        print(negative, round(res / len(positive), 1))
    except:
        break
