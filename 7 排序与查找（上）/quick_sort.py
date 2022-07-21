"""{7}--507快速排序算法及分析12m30s"""


def split(items, first, last):
    pivot = items[first]
    left_mark = first + 1
    right_mark = last

    while True:
        while left_mark <= right_mark and items[left_mark] <= pivot:
            left_mark += 1
        while left_mark <= right_mark and items[right_mark] >= pivot:
            right_mark -= 1
        if left_mark > right_mark:
            break
        else:
            items[left_mark], items[right_mark] = items[right_mark], items[left_mark]

    items[first], items[right_mark] = items[right_mark], items[first]

    return right_mark


def quick_sort(items, first, last):
    if first < last:
        pos = split(items, first, last)
        quick_sort(items, first, pos-1)
        quick_sort(items, pos+1, last)


if __name__ == '__main__':
    item_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(item_list, 0, len(item_list)-1)
    print(item_list)
