from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n: int) -> List[Optional[TreeNode]]:

    def getAns(start: int, end: int):
        if start > end:
            return [None,]
        allTree = []
        for i in range(start, end + 1):
            leftTree = getAns(start, i - 1)
            rightTree = getAns(i + 1, end)
            for a in leftTree:
                for b in rightTree:
                    cur_node = TreeNode(i)
                    cur_node.left = a
                    cur_node.right = b
                    allTree.append(cur_node)
        return allTree

    print(getAns(1, n))


if __name__ == '__main__':
    z = 3
    print(generateTrees(z))
