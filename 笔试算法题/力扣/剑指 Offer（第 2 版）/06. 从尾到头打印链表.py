"""
剑指 Offer 06. 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 
限制：
0 <= 链表长度 <= 10000
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self):
        self._head = None

    def __repr__(self):
        if self._head is None:
            return []
        else:
            data = []
            current = self._head
            while current:
                data.append(current.val)
                current = current.next
            return str(data)

    @property
    def head(self):
        return self._head

    def add_node(self, node):
        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node


class Solution:
    def reversePrint(self, head):
        if head is None:
            return []
        data = []
        current = head
        while current:
            data.append(current.val)
            current = current.next
        # 逆序输出
        return data[::-1]


l = List()
for i in [2, 3, 1]:
    l.add_node(ListNode(i))

print(Solution().reversePrint(l.head))
