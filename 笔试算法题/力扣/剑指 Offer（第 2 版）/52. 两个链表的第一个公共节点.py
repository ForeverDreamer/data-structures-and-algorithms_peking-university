"""
剑指 Offer 52. 两个链表的第一个公共节点
"""


class Solution:
    def getIntersectionNode(self, headA, headB):
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
