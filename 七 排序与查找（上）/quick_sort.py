"""{7}--507快速排序算法及分析12m30s"""


def partition(items, first, last):
    pivot = items[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and items[left_mark] <= pivot:
            left_mark += 1
        while right_mark >= left_mark and items[right_mark] >= pivot:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            items[left_mark], items[right_mark] = items[right_mark], items[left_mark]

    items[first], items[right_mark] = items[right_mark], items[first]

    return right_mark


def quick_sort_helper(items, first, last):
    if first < last:
        split_point = partition(items, first, last)
        quick_sort_helper(items, first, split_point-1)
        quick_sort_helper(items, split_point+1, last)


def quick_sort(items):
    quick_sort_helper(items, 0, len(items)-1)


if __name__ == '__main__':
    item_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(item_list)
    print(item_list)
