"""
HJ51 输出单向链表中倒数第k个结点

描述
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。

链表结点定义如下：

struct ListNode

{

int       m_nKey;

ListNode* m_pNext;

};



正常返回倒数第k个结点指针，异常返回空指针

数据范围：链表长度满足 1≤n≤1000，≤n，链表中数据满足 0≤val≤10000

本题有多组样例输入。


输入描述：
输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值

输出描述：
输出一个整数

示例1
输入：
8
1 2 3 4 5 6 7 8
4
输出：
5
"""

input_seq = ['8', '1 2 3 4 5 6 7 8', '4']


class Node:

    def __init__(self, d):
        self._data = d
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d):
        self._data = d

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n


class UnorderedList:

    def __init__(self):
        self._head = None

    def __str__(self):
        current = self._head
        datas = []
        while current:
            datas.append(current.data)
            current = current.next
        if len(datas) == 0:
            return None
        return ' '.join(datas)

    @property
    def head(self):
        return self._head

    def empty(self):
        return self._head is None

    def add_node_to_tail(self, data):
        new_node = Node(data)
        previous = None
        current = self._head
        while current:
            previous = current
            current = current.next
        if previous is None:
            self._head = new_node
        else:
            previous.next = new_node

    def search(self, idx):
        current = self._head
        i = 0
        while current:
            i += 1
            if i == idx:
                return current.data
            current = current.next

        return '0'


def execute(n, nodes, k):
    ll = UnorderedList()
    for data in nodes:
        ll.add_node_to_tail(data)
    return ll.search(n-k+1)


def linked_list_oper(seq):
    output_seq = []
    i = 0
    while i+2 < len(seq):
        n = int(seq[i])
        nodes = seq[i+1].split(' ')
        k = int(seq[i+2])
        output_seq.append(execute(n, nodes, k))
        i += 3
    return output_seq


for item in linked_list_oper(input_seq):
    print(item)
