"""
HJ103 Redraiment的走法

描述
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？

数据范围：每组数据长度满足 1≤n≤200  ， 数据大小满足 1≤val≤350
本题含有多组样例输入


输入描述：
输入多组数据，1组有2行，第1行先输入数组的个数，第2行再输入梅花桩的高度

输出描述：
一组输出一个结果

示例1
输入：
6
2 5 1 5 4 5
3
3 2 1
复制
输出：
3
1
复制
说明：
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5 ，下标分别是 1 5 6
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5， 下标分别是 3 5 6
从第5格开始走最多有2步,4 5， 下标分别是 5 6
所以这个结果是3。
"""

# 代码1
while True:
    try:
        n = int(input())
        s = [int(x) for x in input().split()]
        L = [1]* n
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if s[j] > s[i]:
                    L[i] = max(L[i], L[j] + 1)

        max_len = max(L)
        print(max_len)
    except:
        break


# 代码2
# import bisect #引入二分法
# # 最大上升子序LIS
# def lengthOfLIS(lst):
#
#     arr = [lst[0]] #定义列表，将传入函数的列表第一个元素放入当前元素
#     dp = [1]*len(lst) #定义一个列表，默认子序列有当前元素1，长度是传入函数的列表长度
#     for i in range(1,len(lst)): #从第二个元素开始查找
#         if lst[i] > arr[-1]: #如果元素大于arr列表的最后一个元素，就把它插入列表末尾
#             arr.append(lst[i])
#             dp[i] = len(arr)# 获取这个元素子序列的长度
#         else: # 否则，利用二分法找到比元素大的元素的位置，用新的元素替代比它大的那个元素的值，这样就能制造出一个顺序排列的子序列
#             pos = bisect.bisect_left(arr, lst[i])
#             arr[pos] = lst[i]
#             dp[i] =pos+1 # 获取这个元素子序列的长度
#     return max(dp)
#
# #二分法排序，将对应长度的最后一个数字放到列表里
# #     n = len(lst)
# #     if n <= 1:
# #         return n
# #     temp = [0] * n
# #     temp[0] = lst[0]
# #     l = 1
# #     for i in range(1,n):
# #         left = 0
# #         right = l
# #         if lst[i] > temp[l-1]:
# #             temp[l]=lst[i]
# #             l+=1
# #             print(temp)
# #             continue
# #         while left < right:
# #             index = (left+right)//2
# #             if lst[i] > temp[index]:
# #                 left = index +1
# #             else:
# #                 right = index
# #         temp[left] = lst[i]
# #         print(temp)
# #     print(temp)
# #     return l
#
# #常规做法
# #     dp = [1] * len(lst)
# #     for i in range(len(lst)):
# #         for j in range(i):
# #             if lst[i] > lst[j]:
# #                 dp[i] = max(dp[i], dp[j] + 1)
# #     return max(dp)
#
# while True:
#     try:
#         n, nums = int(input()), list(map(int, input().split()))
#         print(lengthOfLIS(nums))
#     except:
#         break