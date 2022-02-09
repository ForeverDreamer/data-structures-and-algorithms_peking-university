"""
HJ108 求最小公倍数

描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

数据范围：1≤a,b≤100000
输入描述：
输入两个正整数A和B。

输出描述：
输出A和B的最小公倍数。

示例1
输入：
5 7
复制
输出：
35
复制
示例2
输入：
2 4
复制
输出：
4
"""

# 代码1
# 在大的数的倍数里面去找最小的能整除另外一个数的数，就是最小公倍数，按照大的来找，循环次数能够降到很少，提升效率
while True:
    try:
        a,b=list(map(int, input().split()))
        if a < b:
            a,b=b,a
        for i in range(a,a*b+1,a):
            if i%b==0:
                print(i)
                break
    except:
        break


# 代码2
#方法1：暴力方法 遍历一遍
'''
#两种生成a,b的方法，一种是map，一种是[ ]列表生成器
a,b=map(int,input().split())
a,b=[int(x) for x in input().split()]
'''
while True:
    try:
        a, b = [int(x) for x in input().split()]
        if a < b:
            a,b=b,a
        for i in range(b):
            if((a*(i+1)) % b == 0):
                print(a*(i+1))
                break
    except:
        break

'''        
a, b = map(int, input().split())
#方法2：最大公因数的计算式子和最小公倍数的乘积=a*b, 所以用a*b/最大公因数就可以
def gys(a, b):
    while (b != 0):
        c=a%b
        a=b
        b=c
    return a
print(int((a*b)/gys(a,b)))
'''