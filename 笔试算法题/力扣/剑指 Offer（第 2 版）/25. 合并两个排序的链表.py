"""
剑指 Offer 25. 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：
0 <= 链表长度 <= 1000
"""

from utils import ListNode, List


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        cur_1, cur_2 = l1, l2
        while cur_1 and cur_2:
            if cur_1.val < cur_2.val:
                cur.next, cur_1 = cur_1, cur_1.next
            else:
                cur.next, cur_2 = cur_2, cur_2.next
            cur = cur.next
        cur.next = cur_1 if cur_1 else cur_2
        return dum.next


head = Solution().mergeTwoLists(List([1, 2, 4]).head, List([1, 3, 4]).head)
cur = head
while cur:
    print(cur.val)
    cur = cur.next
