"""{6}--506归并排序算法及分析9m13s"""


def merge_sort(items):
    # 递归结束条件
    if len(items) <= 1:
        return items

    # 分解问题，递归调用
    middle = len(items) // 2
    left = merge_sort(items[:middle])   # 左半部分排好序
    right = merge_sort(items[middle:])  # 右半部分排好序

    # 合并左右部分，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged


if __name__ == '__main__':
    item_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(item_list))
