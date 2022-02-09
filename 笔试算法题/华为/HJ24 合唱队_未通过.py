"""
HJ24 合唱队

描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

说明：

N 位同学站成一排，音乐老师要请其中的 (N - K) 位同学出列，使得剩下的 K 位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为 1，2…，K ，他们的身高分别为 T1，T2，…，TK ，   则他们的身高满足存在 i （1<=i<=K） 使得 T1<T2<......<Ti-1<Ti>Ti+1>......>TK 。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等
请注意处理多组输入输出！

数据范围：

输入描述：
有多组用例，每组都包含两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列

示例1
输入：
8
186 186 150 200 160 130 197 200
输出：
4
说明：
由于不允许改变队列元素的先后顺序，所以最终剩下的队列应该为186 200 160 130或150 200 160 130

LIS问题介绍：
    首先来说一下什么是LIS问题：

有一个长为n的数列a0, a1, ......, a(n-1)。请求出这个序列中最长的上升子序列的长度。上升子序列指的是对于任意的i<j都满足ai<aj的子序列，该问题被称为最长上升子序列（LIS，Longest Increasing Subsequence）的著名问题。

举个栗子：给你一个序列为（1，5 ，2，6，9，10，3，15），那么它的最长上升子序列为：（1，2，6，9，10，15）

这个问题用DP的思想很容易解决，那么现在再来说一下DP（动态规划）的思想。

DP简介（大佬可以忽略此标题里的内容）
别急一会 会！详！！！谈LIS问题以及它的优化方法，为了更好的理解LIS问题，所以先来谈一下DP，如果做过一些DP的题的可以忽略这段入门DP的讲解，如果刚开始接触建议耐心读完，相信会有很大收获。
一、DP思想：
1、把一个大的问题分解成一个一个的子问题。
2、如果得到了这些子问题的解，然后经过一定的处理，就可以得到原问题的解。
3、如果这些子问题与原问题有着结构相同，即小问题还可以继续的分解。
4、这样一直把大的问题一直分下去，问题的规模不断地减小，直到子问题小到不能再小，最终会得到最小子问题。
5、最小子问题的解显而易见，这样递推回去，就可以得到原问题的解。

二、DP的具体实现：
1、分析问题，得到状态转换方程（递推方程）。
2、根据状态转换方程，从原子问题开始，不断的向上求解，知道得到原问题的解。
3、在通过递推方程不断求解的过程，实际上是一个填表的过程。

刚才说的我自己都觉得不好理解，太抽象了，为此举个2个栗子，让大家更好的理解DP的思想。

LIS详解：
首先我们来讲解一下他的递推关系式：
定义dp[ i ] 为：以 ai 为末尾的最长上升子序列的长度。
那么dp[ i ] 包含什么呢？

情况1`: 只包含它自己，也就是说它前面的元素全部都比他大；举个栗子：一个序列（7， 9， 6， 10， 7， 1， 3）分别为 （a1, a2, a3, a4, a5, a6, a7）那么dp[ 6 ] == 1;

情况2`：为了保证上升子序列尽可能的长，那么就有 dp[ i ]  尽可能的大， 但是再保证 dp[ i ] 尽可能大的基础上，还必须满足序列的上升； 所以呢 dp[ i ] = max ( 1 , dp[ j ] + 1 ) {  j < i && aj < ai   } 。这里的1就是当 ai 前面的数都比他大的时候，他自己为一个子序列；dp[ j ] + 1 指的是： 当第 i 个数前面有一个 第 j 个数满足 aj  <  ai  并且 j < i 这时候就说明 ai 元素可以承接在 aj 元素后面来尽可能的增加子序列的长度。

将 j 从 1 遍历到 i - 1  ，在这之间，找出尽可能大的dp[ i ]即为最长上升子序列的长度(提示下 dp[n] 不一定是最长的子序列，n为数列中数的个数，例如序列 [ 2, 3, 4, 5, 1 ]，dp[5] = 1(由子序列[1]构成)，然而 dp[4] = 4(由子序列 [2,3,4,5] 构成) )

上面说的还是有点笼统， 那么再举个栗子吧：
还是用刚才的序列：（7， 9， 6， 10， 7， 1， 3）分别为 （a1, a2, a3, a4, a5, a6, a7）

最开始a1 = 7,  令dp[ 1 ] = 1；
然后看下一个元素 a2 = 9, 令dp[ 2 ] = 1, 那么需要检查 i 前面是否有比他小的 因为 a1 < a2 而且 dp[ 1 ] + 1 > dp[ 2 ], 所以dp[ 2 ] = dp[ 1 ] + 1 == 2;
然后再看下一个元素 a3 = 6, 令 dp[ 3 ] = 1, 那么需要检查前面的元素 a1  与 a2 是否有比他小的， 一看没有，辣么 到目前为止，子序列就是他自己。
然后再看一下下一个元素 a4 = 10; 令 dp[ 4 ] = 1;  那么需要依次检查前面的元素 a1  与 a2 与 a3 是否有比他小的 , 一看a1比它小，而且呢，dp[ 1 ] + 1 > dp[ 4 ] 所以呢 dp[ 4 ] = dp[ 1 ] + 1 == 2, 说明此时 a1 与 a4 可以构成一个长度为 2 的上升子序列，再来看看还可不可以构成更长的子序列呢，所以咱们再来看看 a2 , a2 < a4 而且呢 dp[ 2 ] + 1 == 3 > dp[ 4 ] == 2  所以呢dp[ 4 ] = dp[ 2 ] + 1 == 3,  即将a4承接在a2后面比承接在a1后更好，承接在a2后面的序列为：a1 a2 a4 ，构成一个长度为 3 的上升子序列; 然后再来看 a3 , a3 < a4 但是可惜的是 d[ 3 ] + 1 == 2  < dp[ 4 ] == 3 ,  所以呢就不能把a4加在a3的后面 。
然后就是重复上述过程，找到最大的dp [ i ] 那么这个数就是最长上升子序列。
————————————————
版权声明：本文为CSDN博主「ltrbless」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ltrbless/article/details/81318935
"""

# 牛客网答案
# 通过测试代码
# import bisect #引入二分法
# def hcteam(l): #定义一个函数，寻找最长的子序列
#     arr = [l[0]] #定义列表，将传入函数的列表第一个元素放入当前元素
#     dp = [1]*len(l) #定义一个列表，默认子序列有当前元素1，长度是传入函数的列表长度
#     for i in range(1,len(l)): #从第二个元素开始查找
#         if l[i] > arr[-1]: #如果元素大于arr列表的最后一个元素，就把它插入列表末尾
#             arr.append(l[i])
#             dp[i] = len(arr)# 获取这个元素子序列的长度
#         else: # 否则，利用二分法找到比元素大的元素的位置，用新的元素替代比它大的那个元素的值，这样就能制造出一个顺序排列的子序列
#             pos = bisect.bisect_left(arr, l[i])
#             arr[pos] = l[i]
#             dp[i] =pos+1 # 获取这个元素子序列的长度
#     return dp
#
# while True:
#     try:
#         n = int(input())
#         sg = list(map(int,input().split()))
#         left_t = hcteam(sg) #向左遍历查找子序列
#         right_t = hcteam(sg[::-1])[::-1] #向右遍历查找子序列
#         res = [left_t[i]+right_t[i]-1 for i in range(len(sg))] #因为左右都包含原元素，所以需要减1 ；得到各元素能得到的子序列的最大长度
#         print(n-max(res)) # 源列表长度-可以生成的最长子序列长度  得到需要剔除的最小人数
#     except:
#         break

# 代码1：
# dp的顺序查找，时间复杂度O(N ^ 2)
# def left_max(l):
#  # 计算每个人左边出现的最多的人数
#  # 186 186 150 200 160 130 197 200
#  dp = [1] * len(l) # 若左边没有比自己小的数，则为自己本身，所以初始值为1
#  for i in range(len(l)): # 从左往右遍历
#      for j in range(i):
#          if l[j]<l[i] and dp[i]<dp[j]+1:
#              dp[i] = dp[j]+1
#        # if l[j]<l[i]:
#        #     dp[i] = max(dp[i],dp[j]+1) 会超时
#  return dp #1 1 1 2 2 1 3 4
#            # 从右往左推每个人右边可以站的最多的人数
#            # 3 3 2 3 2 1 1 1
# while True:
#  try:
#      N = int(input())
#      ss = list(map(int,input().split()))
#      left_s = left_max(ss)
#      right_s = left_max(ss[::-1])[::-1]
#      sum_s = []
#      for i in range(len(left_s)):
#          # left_s[i]+right_s[i]-1表示此人是中间位置的人时，合唱队的人数
#          sum_s.append(left_s[i]+right_s[i]-1)
#      print(str(N-max(sum_s)))
#  except:
#      break

# 代码2：
# 二分查找，时间复杂度0(logN)
# import bisect
# def max_l(l,dp):
#  dp += [1] # dp[i]表示第i个人左边能够站的最多的人数
#  b = [float('inf') for i in range(len(l))] # 往b列表中插入，则初始化应该为无穷大
#  b[0] = l[0] # 第一个人
#  for i in range(1,len(l)):
#      # print(b,l[i])
#      pos = bisect.bisect_left(b,l[i])
#      # 在 b 中找到 l[i] 合适的插入点以维持有序。
#      # print(pos)
#      b[pos] = l[i]
#      dp += [pos+1]
#  return dp
# while True:
# ...


# input_seq = ['8', '186 186 150 200 160 130 197 200']
#
#
# # 最长上升子序列（LIS，Longest Increasing Subsequence
# def lis(heights):
#     seq = []
#
#     i = 0
#     while i < len(heights):
#         seq.append(1)
#         j = 0
#         while j < i:
#             if heights[j] < heights[i]:
#                 seq[i] = max(seq[i], seq[j]+1)
#             j += 1
#         i += 1
#
#     return seq
#
#
# # 最长下降子序列（LDS，Longest Decreasing Subsequence），自己命名的。。。
# def lds(heights):
#     dic = {}
#
#     i = len(heights)-1
#     while i >= 0:
#         dic[i] = 1
#         j = len(heights)-1
#         while j > i:
#             if heights[j] < heights[i]:
#                 dic[i] = max(dic[i], dic[j] + 1)
#             j -= 1
#         i -= 1
#
#     return dic
#
#
# def minimum_out(num, heights):
#     left = lis(heights)
#     # right = lis(heights[::-1])[::-1]
#     right = lds(heights)
#     maximum = 0
#     i = 0
#     while i < num:
#         # 合唱队人数=左边人数+右边人数-1，中间的人被计算了2次，所以减1
#         if maximum < left[i]+right[i]-1:
#             maximum = left[i]+right[i]-1
#         i += 1
#     # 出列人数=总人数-合唱队人数
#     return num-maximum
#
#
# def minimum_out_seq(seq):
#     output_seq = []
#     i = 0
#     while i+1 < len(seq):
#         num = int(seq[i])
#         # heights_strs = seq[i + 1].split(' ')
#         # heights = []
#         # # heights_reverse = []
#         # start = 0
#         # # end = len(heights_strs)-1
#         # while start < len(heights_strs):
#         #     heights.append(int(heights_strs[start]))
#         #     # heights_reverse.append(heights_strs[end])
#         #     start += 1
#         #     # end -= 1
#         heights = [int(height) for height in seq[i + 1].split(' ')]
#         output_seq.append(minimum_out(num, heights))
#         i += 2
#     return output_seq
#
#
# for item in minimum_out_seq(input_seq):
#     print(item)