from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head
        pre = new_head
        while pre.next and pre.next.next:
            cur1, cur2, after = pre.next, pre.next.next, pre.next.next.next
            pre.next = cur2
            cur2.next = cur1
            cur1.next = after
            pre = cur1
        return new_head.next


if __name__ == '__main__':
    z = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    so = Solution()
    print(so.swapPairs(z))
