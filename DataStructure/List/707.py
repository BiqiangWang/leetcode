class Node:
    def __init__(self, _val):
        self.val = _val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.he = Node(-1)
        self.ta = Node(-1)
        self.he.next = self.ta
        self.ta.prev = self.he
        self.size = 0

    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node is not None else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.he.next
        node.prev = self.he
        self.he.next.prev = node
        self.he.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.next = self.ta
        node.prev = self.ta.prev
        self.ta.prev.next = node
        self.ta.prev = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            node, cur = Node(val), self.getNode(index)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:
            return
        node = self.getNode(index)
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

    def getNode(self, index: int):
        """
        :return: None or None
        """
        is_left = index < self.size / 2
        if not is_left:
            index = self.size - index - 1
        cur = self.he.next if is_left else self.ta.prev
        while cur != self.he and cur != self.ta:
            if index == 0:
                return cur
            index -= 1
            cur = cur.next if is_left else cur.prev
        return None
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
