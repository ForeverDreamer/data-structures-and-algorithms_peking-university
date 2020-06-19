"""{2}--502二分查找算法及分析12m20s"""


def binary_search(item_list, target):
    first = 0
    last = len(item_list) - 1
    found = False

    while first < last and not found:
        mid_point = (first + last) // 2
        if item_list[mid_point] == target:
            found = True
        else:
            if target < item_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1

    return found


def recursion_binary_search(item_list, target):
    if len(item_list) == 0:
        return False
    else:
        mid_point = len(item_list) // 2
        middle = item_list[mid_point]
        if middle == target:
            return True
        else:
            if target < middle:
                return recursion_binary_search(item_list[:mid_point], target)
            else:
                return recursion_binary_search(item_list[mid_point+1:], target)


ordered_items = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(ordered_items, 3))
print(binary_search(ordered_items, 13))

print(recursion_binary_search(ordered_items, 3))
print(recursion_binary_search(ordered_items, 13))
