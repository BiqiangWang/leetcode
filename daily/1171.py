# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        mapper = dict()

        # 第一次遍历建立 节点处链表和--节点  的哈希表
        summary = 0
        d = dummy
        while d is not None:
            summary += d.val
            mapper[summary] = d
            d = d.next

        # 第二次遍历，若当前节点出sum在下一处出现，则说明两节点间的所有节点和为0
        summary = 0
        d = dummy
        while d is not None:
            summary += d.val
            d.next = mapper[summary].next
            d = d.next

        return dummy.next
