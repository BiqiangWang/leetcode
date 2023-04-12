from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        多种方法：
            1. 遍历一遍提前存储值，再重新构造链表
            2. 双指针原地翻转
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        res = ListNode()
        ans = res
        while head is not None:
            arr.append(head.val)
            head = head.next
        for i in range(len(arr) - 1, -1, -1):
            res.next = ListNode(arr[i])
            res = res.next

        return ans

    def doublePoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    li = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    so = Solution()
    print(so.reverseList(li))
