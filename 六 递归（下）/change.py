def get_change_greedy(coins, amount):
    change = []
    i = 0
    while i < len(coins):
        coin = coins[i]
        if coin <= amount:
            change.append(coin)
            amount = amount - coin
        else:
            i += 1
    return change


def get_change_min(coins, amount):
    min_num = amount
    filter_coins = [coin for coin in coins if coin <= amount]
    # filter_coins = filter(lambda c: c <= amount, coins)
    if amount in filter_coins:
        return 1
    else:
        for coin in filter_coins:
            num = 1 + get_change_min(filter_coins, amount-coin)
            if num < min_num:
                min_num = num
    return min_num


def get_change_dp(coins, amount):
    mins = [0]*64
    subtracts = [0]*64
    # 从1分开始到amount逐个计算最少硬币数
    for step_amount in range(1, amount+1):
        # 1.初始化一个最大值
        coin_count = step_amount
        # 2.减去每个硬币，向后查最少硬币数，同时记录总的最少数
        filter_coins = [coin for coin in coins if coin <= step_amount]
        subtract = filter_coins[-1]
        for c in filter_coins:
            if mins[step_amount-c]+1 < coin_count:
                coin_count = mins[step_amount-c] + 1
                subtract = c
        # 3.得到当前最少硬币数，记录到表中
        mins[step_amount] = coin_count
        subtracts[step_amount] = subtract
    # 返回最后一个结果
    return mins[amount], collect_coins(amount, subtracts)


def collect_coins(amount, subtracts):
    coins = []
    left_amount = amount
    while left_amount > 0:
        subtract = subtracts[left_amount]
        coins.append(subtract)
        left_amount -= subtract
    return coins


print(get_change_greedy([25, 10, 5, 1], 63))
# print(get_change_min([25, 10, 5, 1], 63))
print(get_change_dp([25, 21, 10, 5, 1], 63))
