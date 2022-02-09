"""
HJ82 将真分数分解为埃及分数

"""

# 牛客网答案
# 代码1
# #解题思路:将真分数(a/b)拆分成a*(1/b),也就是a个1/b,然后我们从大到小依次找出a中能被B整除的数.
# 比如: 5/8 这个真分数首先我们看,5不能被8整除,但是4可以,那从5中把4分离出来,变成1+4,剩余的1不能拆分,那埃及分数就是1/8+1/2
#
# 再比如:7/8这个真分数,首先我们看,7不能被8整除,6不能被8整除,5不能被8整除,4可以整除,分子分离出4,还剩3,我们看3不能整除,2能整除,分离出2,还剩1, 埃及分数:1/8+1/4+1/2
# 翻译成以下代码:
# import sys
#
# for fs in sys.stdin.readlines():
#
#     fzfm = fs.strip("\n").split("/")
#     fz = int(fzfm[0])
#     fm = int(fzfm[1])
#     out_string = ""
#     num = fz
#     zy = num
#     contt = 0
#     while True:
#         try:
#             if fm % zy == 0:
#                 if contt == 0:
#                     out_string += ("1/" + str(fm // zy))
#                 else:
#                     out_string += ("+1/" + str(fm // zy))
#
#                 fz = fz - zy
#                 contt += 1
#                 zy = fz
#                 if fz == 0:
#                     print(out_string)
#                     break
#
#             else:
#                 zy -= 1
#                 if zy == 0:
#                     break
#
#         except Exception:
#             pass


# 代码2
# 代码主要运用公式寻找分解后的分母，公式为C = (分母//分子) + 1。用传入 分子/分母 - 1/c 的结果继续执行寻找新分母过程。这个代码的亮点为
# 增加了判断当前分母是否能被(分子 - 1)整除，如果能整除则小问题的答案就是 1 / 分母 和 1 / (分母/(分子-1))
# def fun(a, b):
#     if a == 1:  # 当传入的值分子为1时，记录分母b
#         l1.append(b)
#     elif b % a == 0:  # 当a能被b整除时,记录分母b//a
#         l1.append(b // a)
#     elif b % (a - 1) == 0:  # 当a-1能被b整除时,记录分母b//(a-1) 和 b
#         l1.append(b)
#         l1.append(b // (a - 1))
#     else:  # 利用公式算出最大子埃及分数、剩余分子、剩余分母。记录埃及分母c, z、m带入函数重新计算
#         c = b // a + 1
#         m = c * b
#         z = a * c - b
#         fun(z, m)
#         l1.append(c)
#
# while True:
#     try:
#         l1, l2 = [], []  # l1用来存放找到的分母，来用来辅助计算
#         a, b = map(int, input().split('/'))
#         fun(a, b)
#         l1.sort()
#         for i in l1:
#             l2.append('1/' + str(i))
#         print('+'.join(l2))
#     except:
#         break


# 代码3
# #根据任何真分数都是大于等于（分母除以分子加一）分之一来递归，使用数组接收递归的时候的减去的数据对应的分母
# def dfs(m, n, l):
#     m, n = dfs1(m, n)
#     if m == 1:
#         l.append(n)
#     else:
#         x = int(n / m) + 1
#         m = m * x - n
#         n = n * x
#         dfs(m, n, l)
#         l.append(x)
#     return l
#
# # 对传入的两个数据做处理，不能含有公约数
# def dfs1(m, n):
#     if m == 1:
#         return m, n
#     else:
#         for i in range(2, m + 1):
#             if m % i == 0 and n % i == 0:
#                 return dfs1(int(m / i), int(n / i))
#             elif i == m:
#                 return m, n
# while True :
#     try:
#         l = []
#         la = list(map(int, input().split("/")))
#         l = dfs(la[0], la[1], l)
#         for i in range(0, len(l)):
#             l[i] = "1/" + str(l[i])
#         print("+".join(l))
#     except:
#         break