"""
剑指 Offer 35. 复杂链表的复制
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

    def __repr__(self):
        values = []
        cur = self
        while cur:
            values.append(f'{cur.val}->(next:{cur.next.val if cur.next else None}, random:{cur.random.val if cur.random else None})')
            cur = cur.next
        return str(values)


class List:
    def __init__(self):
        nodes = {
            7: Node(7),
            3: Node(3),
            1: Node(1),
            0: Node(0),
            2: Node(2),
        }
        nodes[7].next = nodes[3]
        nodes[7].random = None
        self.head = nodes[7]
        nodes[3].next = nodes[1]
        nodes[3].random = nodes[7]
        nodes[1].next = nodes[0]
        nodes[1].random = nodes[2]
        nodes[0].next = nodes[2]
        nodes[0].random = nodes[1]
        nodes[2].next = None
        nodes[2].random = nodes[7]


class Solution:
    def copyRandomList(self, head: 'Node'):
        if not head:
            return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射(链表节点全部确定下来才知道random指向哪个节点)
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]


print(Solution().copyRandomList(List().head))
