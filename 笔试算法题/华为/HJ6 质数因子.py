"""
HJ6 质数因子

描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围：
输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入：
180
输出：
2 2 3 3 5
"""

input_num = 180
# input_num = int(input().strip())


def prime_factors(n):
    i = 2
    factors = []

    while i**2 <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)

    factors.sort()
    factors = [str(factor) for factor in factors]
    return factors


print(' '.join(prime_factors(input_num)) + ' ')
