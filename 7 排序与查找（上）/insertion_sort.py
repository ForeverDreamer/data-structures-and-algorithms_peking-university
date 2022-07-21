"""{4}--504插入排序算法及分析7m06s"""


def insertion_sort(items):
    for i in range(1, len(items)):
        pos = i
        curr_val = items[pos]
        while pos > 0 and items[pos-1] > curr_val:
            items[pos] = items[pos-1]
            pos -= 1
        items[pos] = curr_val


if __name__ == '__main__':
    item_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(item_list)
    print(item_list)
