"""{1}--501顺序查找算法及分析9m41s"""


def unordered_search(item_list, target):
    pos = 0
    found = False

    while pos < len(item_list):
        if item_list[pos] == target:
            found = True
            break
        else:
            pos += 1

    return found


def ordered_search(item_list, target):
    pos = 0
    found = False

    while pos < len(item_list):
        if item_list[pos] == target:
            found = True
            break
        else:
            if item_list[pos] > target:
                break
            else:
                pos += 1

    return found


unordered_items = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(unordered_search(unordered_items, 3))
print(unordered_search(unordered_items, 13))

ordered_items = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_search(ordered_items, 3))
print(ordered_search(ordered_items, 13))
