"""谢尔排序"""


def gap_insertion_sort(items, start, gap):
    for i in range(start+gap, len(items), gap):
        current = items[i]
        pos = i
        while pos >= gap and items[pos-gap] > current:
            items[pos] = items[pos-gap]
            pos -= gap
        items[pos] = current


def shell_sort(items):
    sub_list_count = len(items) // 2
    while sub_list_count > 0:
        for start_pos in range(sub_list_count):
            gap_insertion_sort(items, start_pos, sub_list_count)
        print(f'After increments of size {sub_list_count}, the list is {items}')
        sub_list_count //= 2
