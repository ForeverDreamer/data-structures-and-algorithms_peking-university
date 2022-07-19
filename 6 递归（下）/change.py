def get_change_greedy(coins, amount):
    change = []
    i = 0
    while i < len(coins):
        coin = coins[i]
        while coin <= amount:
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
        # 1.初始化一个最大值，即假设全部使用1分硬币
        min_count = step_amount * 1
        # 默认当前使用一分钱
        subtract = 1
        # 2.减去每个硬币，向后查最少硬币数，同时记录总的最少数
        filter_coins = [coin for coin in coins if coin <= step_amount]
        for c in filter_coins:
            # 如果使用当前硬币的解小于当前最优解，更新当前最优解，记录使用的硬币
            current_count = mins[step_amount-c] + 1
            if current_count < min_count:
                min_count = current_count
                subtract = c
        # 3.得到当前最少硬币数，记录到表中
        mins[step_amount] = min_count
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
