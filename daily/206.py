# This is a sample Python script.
from typing import Optional


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    arr = []
    res = ListNode()
    node = res
    while head is not None:
        arr.append(head.val)
        head = head.next
    for i in range(len(arr) - 1, -1, -1):
        node.next = ListNode(arr[i])
        node = node.next
    return res.next

    """
    当输入head本身为空时，若令res=head，则会造成，本节点为空，没有next节点的情况
    """
    # res = head
    # node = head
    # while head is not None:
    #     arr.append(head.val)
    #     head = head.next
    # for i in range(len(arr) - 1, -1, -1):
    #     node.next = ListNode(arr[i])
    #     node = node.next
    # pp = res.next
    # while pp is not None:
    #     print(pp.val)
    #     pp = pp.next
    # return res.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    li = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverseList(li))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
