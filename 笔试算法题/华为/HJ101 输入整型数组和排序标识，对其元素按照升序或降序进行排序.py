"""
HJ101 输入整型数组和排序标识，对其元素按照升序或降序进行排序

描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序

数据范围： 1≤n≤1000  ，元素大小满足 0≤val≤100000
输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述：
输出排好序的数字

示例1
输入：
8
1 2 4 9 3 55 64 25
0
复制
输出：
1 2 3 4 9 25 55 64
复制
示例2
输入：
5
1 2 3 4 5
1
复制
输出：
5 4 3 2 1
"""

# 代码1
# n=int(input())
# d=list(map(int,input().split()))
# x=int(input())
# if x == 0:
#     for i in sorted(d):
#         print(i,end=" ")
# else:
#     d=sorted(d,reverse=True)
#     for i in d:
#         print(i,end=" ")


# 代码2
# n = int(input())
# ls = list(map(int, input().split()))    # 需要转成整数，才能排序
# rnk = int(input())
# if rnk == 0:
#     ls.sort()
#     ls = map(str,ls)    # 需要转回字符串，才能拼接
#     print(' '.join(ls))
# elif rnk == 1:
#     ls.sort(reverse=True)
#     ls = map(str, ls)
#     print(' '.join(ls))


# 代码3
# def func(i,lst,bol):
#     i1= int(i)
#     bol1 = bool(int(bol))
#     lst1 = list(map(int,lst))
#     lst1.sort(reverse= bol1)
#     lst2 = [ str(x) for x in lst1 ]
#     str1 = " "
#     return str1.join(lst2)
# i = input()
# lst = input().split()
# bol = input()
# print(func(i,lst,bol))