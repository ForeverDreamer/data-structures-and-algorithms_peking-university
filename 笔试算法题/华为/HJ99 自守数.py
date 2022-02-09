"""
HJ99 自守数

描述
自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数

本题有多组输入数据

数据范围： 1≤n≤10000


输入描述：
int型整数

输出描述：
n以内自守数的数量。

示例1
输入：
5
2000
复制
输出：
3
8
复制
说明：
对于样例一，有0，1，5，这三个自守数
示例2
输入：
1
复制
输出：
2
复制
说明：
有0, 1这两个自守数
"""

# 代码1
# 自然数包括0，判断平方数减去原数能否被10的len(n)次方整除
# def get_ans(s):
#     ans=0
#     for i in range(0,s+1):
#         if is_num(i):
#             ans+=1
#     return ans
#
# def is_num(n):
#     mark=n**2
#     length=len(str(n))
#     return (mark-n)%(10**(length))==0
#
# if __name__=='__main__':
#     import sys
#     lines = []
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == "":
#             break
#         lines.append(line)
#     # 单个取
#     for item in lines:
#         print(get_ans(int(item)))


# 代码2
# 遍历
# 用range，从0开始，一直到n+1（这里要注意不能漏最后一个）
# 一个数字的末尾是2，3，4，7，8，9的话，不可能题目要求，平方的末尾都和自己不一样；
# 数字to字符串，对i的整体和j的倒数几位直接对比计数即可。
# while True:
#     try:
#         n = int(input())
#         c = 0
#         for i in range(n+1):
#             if i%10 in [2, 3, 4, 7, 8, 9]:
#                 continue
#             j = str(i**2)
#             i = str(i)
#             if i==j[-len(i):]:
#                 c += 1
#         print(c)
#     except:
#         break


# 代码3
# while True:
#     try:
#         n = int(input())
#         count = 0
#         for i in range(n+1):
#             if str(i) == str(i**2)[-len(str(i)):]:
#                 count += 1
#         print(count)
#     except:
#         break
