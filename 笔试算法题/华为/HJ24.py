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
"""

input_seq = ['8', '186 186 150 200 160 130 197 200']


def validate_queue(queue):
    reach_middle = False
    idx = 0
    while idx+1 < len(queue):
        if idx == 0:
            if queue[idx] >= queue[idx + 1]:
                return False
        if not reach_middle:
            if queue[idx] < queue[idx+1]:
                idx += 1
            else:
                reach_middle = True
        else:
            if queue[idx] > queue[idx+1]:
                idx += 1


def minimum_out_dp(heights, num):
    minimum = 0
    idx = 1
    while idx < len(heights):
        middle = heights[idx]


# def minimum_out_dp(heights, num):
#     minimums = [0]*(num+1)
#     subtracts = [0]*(num+1)
#     for step_num in range(3, num+1):
#         # 默认不需要任何人出列
#         minimum = 0
#         if validate_queue(heights):
#             minimums[step_num] = 0
#         else:
#             pass
#         # 默认使用一分钱为最优解
#         subtract = filter_coins[-1]
#         for c in filter_coins:
#             if mins[step_amount-c]+1 < coin_count:
#                 coin_count = mins[step_amount-c] + 1
#                 subtract = c
#         # 3.得到当前最少硬币数，记录到表中
#         mins[step_amount] = coin_count
#         subtracts[step_amount] = subtract
#     # 返回最后一个结果
#     return mins[amount], collect_coins(amount, subtracts)


def collect_coins(amount, subtracts):
    coins = []
    left_amount = amount
    while left_amount > 0:
        subtract = subtracts[left_amount]
        coins.append(subtract)
        left_amount -= subtract
    return coins


def minimum_out(seq):
    output_seq = []
    idx = 0
    while idx < len(seq):
        num = int(seq[idx])
        heights = [int(height) for height in seq[idx].split(' ')]
        minimum_out_dp(heights, num)
    return output_seq


for item in minimum_out(input_seq):
    print(item)
