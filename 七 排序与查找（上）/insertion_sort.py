"""{4}--504插入排序算法及分析7m06s"""


def insertion_sort(items):
    for index in range(1, len(items)):
        current_val = items[index]
        position = index
        while position > 0 and items[position-1] > current_val:
            items[position] = items[position-1]
            position -= 1
        items[position] = current_val


if __name__ == '__main__':
    item_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(item_list)
    print(item_list)
