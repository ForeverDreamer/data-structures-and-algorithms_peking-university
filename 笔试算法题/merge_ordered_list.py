"""有序列表合并"""
from linked_list import OrderedList


def merge_list(list1, list2):
    """合并数组"""
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError('只接受list参数类型！')
    # if len(list1) == 0 or len(list2) == 0:
    #     raise ValueError('数组不能为空！')

    merged = []
    pos1 = 0
    pos2 = 0
    length1 = len(list1)
    length2 = len(list2)

    while pos1 < length1 and pos2 < length2:
        if list1[pos1] < list2[pos2]:
            merged.append(list1[pos1])
            pos1 += 1
        else:
            merged.append(list2[pos2])
            pos2 += 1

    left = list1[pos1:] if pos1 < length1 else list2[pos2:]
    merged.extend(left)

    return merged


def merge_linked_list(linked1, linked2):
    if not isinstance(linked1, OrderedList) or not isinstance(linked2, OrderedList):
        raise ValueError('只接受OrderedList参数类型!')

    merged = OrderedList()
    next_node1 = linked1.head
    next_node2 = linked2.head
    while next_node1 and next_node2:
        if next_node1.data < next_node2.data:
            merged.add(next_node1.data)
            next_node1 = next_node1.next
        else:
            merged.add(next_node2.data)
            next_node2 = next_node2.next

    if next_node1:
        merged.add_node_to_tail(next_node1)
    else:
        merged.add_node_to_tail(next_node2)

    return merged


def main_merge_list():
    li1 = [11, 21, 38]
    li2 = [1, 3, 6, 8, 9]
    print(merge_list(li1, li2))


def main_merge_linked_list():
    link1 = OrderedList()
    for data in [11, 21, 38]:
        link1.add(data)
    link2 = OrderedList()
    for data in [1, 3, 6, 8, 9]:
        link2.add(data)
    print(link1)
    print(link2)
    merged = merge_linked_list(link1, link2)
    print(merged)


if __name__ == '__main__':
    main_merge_list()
    print('===================================')
    main_merge_linked_list()
