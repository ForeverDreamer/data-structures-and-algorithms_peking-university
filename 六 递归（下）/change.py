def get_change_greedy(coins, amount):
    change = []
    i = 0
    while i < len(coins):
        if coins[i] <= amount:
            change.append(coins[i])
            amount = amount - coins[i]
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


def get_change_dp(coins, amount, min_coins):
    # 从1分开始到amount逐个计算最少硬币数
    for cents in range(1, amount+1):
        # 1.初始化一个最大值
        coin_count = cents
        # 2.减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coins if c <= cents]:
            if min_coins[cents-j]+1 < coin_count:
                coin_count = min_coins[cents-j] + 1
        # 3.得到当前最少硬币数，记录到表中
        min_coins[cents] = coin_count
    # 返回最后一个结果
    return min_coins[amount]


# print(get_change_greedy([25, 10, 5, 1], 63))
# print(get_change_min([25, 10, 5, 1], 63))
print(get_change_dp([25, 21, 10, 5, 1], 63, [0]*64))
