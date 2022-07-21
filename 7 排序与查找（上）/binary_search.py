"""{2}--502二分查找算法及分析12m20s"""


def binary_search(item_list, target):
    first = 0
    last = len(item_list) - 1
    found = False

    while first < last:
        mid_point = (first + last) // 2
        middle = item_list[mid_point]
        if middle == target:
            found = True
            break
        else:
            if target < middle:
                last = mid_point - 1
            else:
                first = mid_point + 1

    return found


def recursion_binary_search(item_list, target, first, last):
    # if len(item_list) ==0:
    if first >= last:
        return False
    else:
        # mid_point = len(item_list) // 2
        mid_point = (first + last) // 2
        middle = item_list[mid_point]
        if middle == target:
            return True
        else:
            if target < middle:
                # return recursion_binary_search(item_list[:mid_point], target)
                return recursion_binary_search(item_list, target, first, mid_point - 1)
            else:
                # return recursion_binary_search(item_list[mid_point+1:], target)
                return recursion_binary_search(item_list, target, mid_point + 1, last)


ordered_items = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(ordered_items, 3))
print(binary_search(ordered_items, 13))

print(recursion_binary_search(ordered_items, 3, 0, len(ordered_items)-1))
print(recursion_binary_search(ordered_items, 13, 0, len(ordered_items)-1))
