# 宝物的重量和价值
treasures = [
    None,
    {'w': 2, 'v': 3},
    {'w': 3, 'v': 4},
    {'w': 4, 'v': 8},
    {'w': 5, 'v': 8},
    {'w': 9, 'v': 10},
]

# 大盗最大负重
max_w = 20

# 初始化二维表格m[(i, w)]
# 表示前i个宝物中，最大重量w的组合，所得到的最大价值
# 当i什么都不取，或w上限为0，价值均为0
values = {(i, w): [0, i, False, []] for i in range(len(treasures)) for w in range(max_w + 1)}
# combinations = {(i, w): [] for i in range(len(treasures)) for w in range(max_w + 1)}

# 逐个填写二维表格
for i in range(1, len(treasures)):
    for w in range(1, max_w + 1):
        # ps: 同样只能按顺序在前i件宝物中选择0~i件宝物，负重越大，能装载的价值肯定越大
        # 也就是说如果w>0，(i, w) >= (i, (0 ~ w-1))，所以不装第i个宝物时，values[(i, w)] = values[(i-1, w)]
        # 装不下第i个宝物
        if treasures[i]['w'] > w:
            # 不装第i个宝物
            values[(i, w)][0] = values[(i-1, w)][0]
        else:
            # 不装第i个宝物/装第i个宝物，两种情况下的最大价值
            # values[(i, w)] = max(values[(i-1, w)], values[(i-1, w-treasures[i]['w'])] + treasures[i]['v'])
            if values[(i-1, w)][0] > values[(i-1, w - treasures[i]['w'])][0] + treasures[i]['v']:
                values[(i, w)][0] = values[(i-1, w)][0]
            else:
                last_w = w - treasures[i]['w']
                last_v, last_i, taken, _ = values[(i-1, last_w)]
                values[(i, w)][0] = last_v + treasures[i]['v']
                values[(i, w)][2] = True
                values[(i, w)][3].append(i)
                while last_i > 0:
                    if taken:
                        values[(i, w)][3].append(last_i)
                        last_w -= treasures[last_i]['w']
                    # if last_w < 0:
                    #     break
                    last_v, last_i, taken, _ = values[(last_i-1, last_w)]


print(values[(len(treasures)-1, max_w)])
# print(combinations[(len(treasures)-1, max_w)])
