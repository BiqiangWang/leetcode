from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        对于头节点的删除情况其实有两种思路：
            1. 单独拿出来考虑（这里使用了这种方法）
            2. 加一个初始节点进去
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        node = head
        while node is not None:
            if node.val == val:
                node = node.next
            elif node.next is None:
                break
            elif node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head

    def digui(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        head.next = self.digui(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head

