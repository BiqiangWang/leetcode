from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def digui(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []

        def f(node: Optional[ListNode], i: int) -> None:
            if node is None:
                nonlocal ans
                ans = [0] * i
                return
            f(node.next, i + 1)
            while st and st[-1] <= node.val:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(node.val)

        f(head, 0)
        return ans

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
            反向遍历： （与递归同效果）
            先反转链表，最后反向输出

        :param head:
        :return:
        """
        head = self.reverseList(head)
        ans = []
        st = []
        while head:
            while st and st[-1] <= head.val:
                st.pop()
            ans.append(st[-1] if st else 0)
            st.append(head.val)
            head = head.next
        return ans[::-1]

    def fromHeadToEnd(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []  # （节点值，节点下标）    由于记录答案需要元素的下标，所以栈中除了保存元素值以外，还需要保存元素的下标。
        while head:
            while st and st[-1][0] < head.val:
                ans[st.pop()[1]] = head.val
            st.append((head.val, len(ans)))
            ans.append(0)
            head = head.next
        return ans


