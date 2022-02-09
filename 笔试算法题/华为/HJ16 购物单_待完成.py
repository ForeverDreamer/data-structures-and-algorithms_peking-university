"""
HJ16 购物单

描述
王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：

主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无

如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
    设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
    请你帮助王强设计一个满足要求的购物单。

输入描述：
输入的第 1 行，为两个正整数，用一个空格隔开：N m
（其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）

输出描述：
 输出文件只有一个正整数，为不超过总钱数的物品的价格与重要度乘积的总和的最大值（ <200000 ）。
示例1
输入：
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
输出：
2200


解题思路
购物车
其实这题就是0-1背包问题
首先来看一下经典背包问题，稍作修改就可以得出这题的解答

0-1背包问题

问题描述：有一个背包可以装物品的总重量为W，现有N个物品，每个物品中w[i]，价值v[i]，用背包装物品，能装的最大价值是多少？

定义状态转移数组dp[i][j]，表示前i个物品，背包重量为j的情况下能装的最大价值。

例如，dp[3][4]=6，表示用前3个物品装入重量为4的背包所能获得的最大价值为6，此时并不是3个物品全部装入，而是3个物品满足装入背包的条件下的最大价值。

状态转移方程：

dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

dp[i-1][j]表示当前物品不放入背包，dp[i-1][j-w[i]]+v[i]表示当前物品放入背包，即当前第i个物品要么放入背包，要么不放入背包。

dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if j-w[i]>=0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]
return dp[m][n]
现在来看下购物车的解题思路

购物车本质上还是0-1背包问题，只不过多了主件和附件。假设先不看附件，那么就和0-1背包一样了。附件不能单独出现，要依赖于主件。

对应于背包问题，主件的个数就是物品的个数，考虑每个主件时要考虑可能出现的情况。

输入例子:
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0

在当前的例子当中物品的个数就是3。

考虑每个物品时要考虑每种可能出现的情况，1、主件，2、主件+附件1，3、主件+附件2，4、主件+附件1+附件2，不一定每种情况都出现，只有当存在附件时才会出现对应的情况。

w[i][k]表示第i个物品的第k种情况，k的取值范围0~3，分别对应以上4中情况，v[i][k]表示第i个物品对应第k种情况的价值，现在就把购物车问题转化为了0-1背包问题。

状态转移方程可以定义为

dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i][k]]+v[i][k])

dp[i-1][j]表示当前物品不放入背包，w[i][k]表示第i个主件对应第k中情况，即当前第i个物品的4中情况中价值最大的要么放入背包，要么不放入背包。

需要注意：dp[i][j] = max(物品不放入背包，主件，主件+附件1，主件+附件2，主件+附件1+附件2)

dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        max_i = dp[i-1][j]
        for k in range(len(w[i])):
            if j-w[i][k]>=0:
                max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
        dp[i][j] = max_i
print(dp[m][n])

具体代码如下：
n, m = map(int,input().split())
primary, annex = {}, {}
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:#主件
        primary[i] = [x, y]
    else:#附件
        if z in annex:#第二个附件
            annex[z].append([x, y])
        else:#第一个附件
            annex[z] = [[x,y]]
m = len(primary)#主件个数转化为物品个数
dp = [[0]*(n+1) for _ in range(m+1)]
w, v= [[]], [[]]
for key in primary:
    w_temp, v_temp = [], []
    w_temp.append(primary[key][0])#1、主件
    v_temp.append(primary[key][0]*primary[key][1])
    if key in annex:#存在主件
        w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
        v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#存在两主件
            w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
            v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
            w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
for i in range(1,m+1):
    for j in range(10,n+1,10):#物品的价格是10的整数倍
        max_i = dp[i-1][j]
        for k in range(len(w[i])):
            if j-w[i][k]>=0:
                max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
        dp[i][j] = max_i
print(dp[m][n])
继续优化

现在的时间复杂度是O(mn)，时间复杂度已经无法优化，空间复杂度O(mn)，可以继续优化到O(n)。

回顾下状态转移方程：
dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

dp[i]只依赖dp[i-1]，状态转移方程就可以改为：
dp[j] = max(dp_pre[j], dp_pre[j-w[i]]+v[i])

dp_pre[j]存储上一次得到的值，现在只需要2*n的空间就能得到结果。继续观察可以发现，其实只用一个一维dp数组就行，不需要额外的辅助数组。让j从n到1遍历，此时每次更新的dp[j]时，max函数中dp[j]和 dp[j-w[i]]都是上次保存的值。

状态转移方程变为：
for j in [n...1]:
dp[j] = max(dp[j], dp[j-w[i]]+v[i])

如果从1到n遍历的话dp[j-w[i]]不能保证还是上次的值，这也进一步说明为什么用一维数组时需要从n到1遍历。

优化后的代码如下：
n, m = map(int,input().split())
primary, annex = {}, {}
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:
        primary[i] = [x, y]
    else:
        if z in annex:
            annex[z].append([x, y])
        else:
            annex[z] = [[x,y]]
dp = [0]*(n+1)
for key in primary:
    w, v= [], []
    w.append(primary[key][0])#1、主件
    v.append(primary[key][0]*primary[key][1])
    if key in annex:#存在附件
        w.append(w[0]+annex[key][0][0])#2、主件+附件1
        v.append(v[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#附件个数为2
            w.append(w[0]+annex[key][1][0])#3、主件+附件2
            v.append(v[0]+annex[key][1][0]*annex[key][1][1])
            w.append(w[0]+annex[key][0][0]+annex[key][1][0])#4、主件+附件1+附件2
            v.append(v[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    for j in range(n,-1,-10):#物品的价格是10的整数倍
        for k in range(len(w)):
            if j-w[k]>=0:
                dp[j] = max(dp[j], dp[j-w[k]]+v[k])
print(dp[n])
"""


# 牛客网答案
# 代码1优化版本
# n, m = map(int,input().split())
# primary, annex = {}, {}
# for i in range(1,m+1):
#     x, y, z = map(int, input().split())
#     if z==0:
#         primary[i] = [x, y]
#     else:
#         if z in annex:
#             annex[z].append([x, y])
#         else:
#             annex[z] = [[x,y]]
# dp = [0]*(n+1)
# for key in primary:
#     w, v= [], []
#     w.append(primary[key][0])#1、主件
#     v.append(primary[key][0]*primary[key][1])
#     if key in annex:#存在附件
#         w.append(w[0]+annex[key][0][0])#2、主件+附件1
#         v.append(v[0]+annex[key][0][0]*annex[key][0][1])
#         if len(annex[key])>1:#附件个数为2
#             w.append(w[0]+annex[key][1][0])#3、主件+附件2
#             v.append(v[0]+annex[key][1][0]*annex[key][1][1])
#             w.append(w[0]+annex[key][0][0]+annex[key][1][0])#4、主件+附件1+附件2
#             v.append(v[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
#     for j in range(n,-1,-10):#物品的价格是10的整数倍
#         for k in range(len(w)):
#             if j-w[k]>=0:
#                 dp[j] = max(dp[j], dp[j-w[k]]+v[k])
# print(dp[n])