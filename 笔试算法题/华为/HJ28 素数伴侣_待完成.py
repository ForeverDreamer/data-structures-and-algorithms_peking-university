"""
HJ28 素数伴侣

描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:

输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。

数据范围： 1≤n≤100  ，输入的数据大小满足 2≤val≤30000

本题有多组输入
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数
题目有多组输入

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。

示例1
输入：
4
2 5 6 13
2
3 6
输出：
2
0

示例2
输入：
2
3 6
输出：
0

题意整理。
输入N（N为偶数）个正整数，从其中挑选出若干对组成“素数伴侣”。
问怎么挑选，可以使得“素数伴侣”的对数最多。
如果两个正整数的和为素数，则这两个正整数称之为“素数伴侣”。
方法一（匈牙利算法）
1.解题思路
首先定义两个list容器，分别存储输入整数中的奇数和偶数。
然后利用匈牙利算法找到“素数伴侣”对数最多时的配对数。匈牙利算法的核心思想是先到先得，能让就让。
最后输出“素数伴侣”最多时的对数。
图解展示（匈牙利算法）：
见图片
举例说明：如图所示，首先A1和B2配对（先到先得），然后轮到A2，A2也可以和B2配对，这时候B2发现A1还可以和B4配对，所以放弃了A1，
选择和A2组成伴侣（能让就让）。接着A3直接和B1配对（先到先得）。最后A4尝试与B4配对，但是这样A1就只能与B2配对，而A2就找不到伴侣了，
一层层递归下来，发现不可行，所以A4不能与B4配对
"""


def is_prime(x):  # 判断是否是质数
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1


def match(i):  # i表示第几行，左侧元素
    for j in range(n):  # j表示第几列，右侧元素
        if array[i][j] == 1 and not visited[j]:  # 有边且未访问
            visited[j] = True  # 记录状态为访问过
            if matched[j] == -1 or match(matched[j]):  # 如果该右侧元素暂无匹配，或者原来匹配的左侧元素可以找到新的匹配
                matched[j] = i  # 当前左侧元素成为当前右侧元素的新匹配
                return True
    return False  # 循环结束，仍未找到匹配，返回匹配失败


while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
    except:
        break
    else:
        evens, odds = [], []
        for i in a:  # 对偶数和奇数进行分组。偶数加奇数才有可能是质数
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        # 求关于是否是prime的矩阵，即得到邻接矩阵
        m = len(odds)  # 行，左侧元素
        n = len(evens)  # 列，右侧元素
        array = [[-1 for i in range(n)] for j in range(m)]
        for i, x in enumerate(odds):  # odds和evens谁先谁后无所谓
            for j, y in enumerate(evens):
                array[i][j] = is_prime(x + y)

        # 开始匈牙利算法，进行匹配
        matched = [-1 for i in range(n)]  # 记录当前已匹配的右侧元素(列)所对应的左侧元素(行)
        counter = 0
        for i in range(m):
            visited = [False for k in range(n)]  # 记录右侧元素是否已被访问过。每切换左侧元素时进行重置。
            if match(i):
                counter += 1
        print(counter)


# 备用代码
# '''
# 匈牙利算法(求二分图的最大匹配):要用到递归,思想:后来者居上
# '''
# import sys
# #1.判断是否是素数(若在1到该数平方根之间都没有可除尽的数)
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# #2.寻找'增广路径'(这个数可否匹配,该跟谁连)
# def find(odd, visited, choose, evens):
#     for j, even in enumerate(evens):#扫描每个待被匹配的even
#         if is_prime(odd + even) and not visited[j]:
#             visited[j] = True
#             if choose[j] == 0 or find(choose[j], visited, choose, evens):
#                 #如果第j位even还没被选 或者 选它的那个odd还有别的选择even可以选择,那就把这位even让给当前的odd
#                 choose[j] = odd
#                 return True #说明匹配
#     return False
#
# #3.开始odd先生和even小姐们入场,并各自到自己队列,开始匹配
# while True:
#     try:
#         n = int(input())
#         nums = list(map(int, input().split()))
#         count = 0
#         #奇数+奇数 = 偶数, 偶数 + 偶数 = 偶数,都不能成为素数.只能奇数+偶数的组合才有可能
#         odds,evens = [], []#把数分为奇数和偶数
#         #每次拿一个数,添加到对应的list里
#         for num in nums:
#             if num % 2 == 1:
#                 odds.append(num)
#             else:
#                 evens.append(num)
#
#         #对每个odd,去找自己的even
#         choose = [0] * len(evens) #用来装匹配这位even的对应的odd先生
#         for odd in odds:
#             visited = [False] * len(evens)
#             if find(odd, visited, choose, evens):
#                 count += 1
#         print(count)
#     except:
# #         print(sys.exc_info())
#         break
