"""
HJ60 查找组成一个偶数最接近的两个素数

描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

本题含有多组样例输入。

数据范围：输入的数据满足4≤n≤1000
输入描述：
输入一个大于2的偶数

输出描述：
输出两个素数

示例1
输入：
20
复制
输出：
7
13
复制
示例2
输入：
4
复制
输出：
2
2
"""


# 逼近法
def isPrime(num):  # 定义一个素数判断函数
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
        else:
            pass
    return True


while True:
    try:
        n = int(input())
        for i in range(2, n // 2 + 1):  # 截断整数部分
            if isPrime(i) and isPrime(n - i):  # 从两端开始逼近
                a, b = i, n - i
        print(a)
        print(b)
    except:
        break
