from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
        环形链表要求我们考虑两个问题：
            1. 怎么判断有环     -> 快慢指针
            2. 若有环，怎么判断入口     -> 相遇节点和头节点到环入口步数相等（数学推导）
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next and head.next.next:
            fast, slow = head.next.next, head.next
        else:
            return None
        while fast is not None and fast != slow:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        if fast is None:   # 判断是否有环
            return None
        node = head
        while node != fast:
            node = node.next
            fast = fast.next
        return node

