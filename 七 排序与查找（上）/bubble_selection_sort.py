"""{3}--503冒泡和选择排序算法及分析12m14s"""


def bubble_sort1(item_list):
    # 每交换一趟都会把最大的一个数排到最后，所以后边的比对就不再需要比对已经排好的数据
    for last in range(len(item_list)-1, 0, -1):
        for i in range(last):
            if item_list[i] > item_list[i+1]:
                item_list[i], item_list[i+1] = item_list[i+1], item_list[i]


def bubble_sort2(item_list):
    last = len(item_list) - 1
    while last > 0:
        exchange = False
        for i in range(last):
            if item_list[i] > item_list[i + 1]:
                exchange = True
                item_list[i], item_list[i + 1] = item_list[i + 1], item_list[i]
        if not exchange:
            break
        last -= 1


def selection_sort(item_list):
    for fill_slot in range(len(item_list)-1, 0, -1):
        pos_of_max = 0
        for pos in range(1, fill_slot+1):
            if item_list[pos] > item_list[pos_of_max]:
                pos_of_max = pos
        item_list[fill_slot], item_list[pos_of_max] = item_list[pos_of_max], item_list[fill_slot]


unordered_items1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort1(unordered_items1)
print(unordered_items1)

unordered_items2 = [20, 30, 90, 50, 40, 60, 110, 100, 80, 120]
bubble_sort2(unordered_items2)
print(unordered_items2)

unordered_items3 = [2, 3, 9, 5, 4, 6, 11, 10, 8, 12]
selection_sort(unordered_items3)
print(unordered_items3)
