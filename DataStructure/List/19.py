from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        virtual_head = ListNode()
        virtual_head.next = head
        pren, cur = virtual_head, head
        while cur is not None:  # 这里的循环结构实际上可以优化成更简洁的形式，效果类似
            while n > 0:
                if cur is None:
                    break
                cur = cur.next
                n -= 1
            cur = cur.next
            pren = pren.next
        pren.next = pren.next.next
        return virtual_head.next


if __name__ == '__main__':
    z = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    v = 2
    so = Solution()
    print(so.removeNthFromEnd(z, 2))
