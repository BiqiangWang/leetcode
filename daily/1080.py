from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _dfs(self, node, s, limit):
        if node.left is None and node.right is None:
            return s + node.val < limit

        l_delete = True
        r_delete = True

        if node.left:
            l_delete = self._dfs(node.left, s + node.val, limit)
        if node.right:
            r_delete = self._dfs(node.right, s + node.val, limit)

        if l_delete:
            node.left = None
        if r_delete:
            node.right = None

        return l_delete and r_delete

    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        # def dfs(node: Optional[TreeNode], val: int) -> int:
        #     l_r, l_v = 0, 0
        #     if node.left is not None:
        #         l_v = dfs(node.left, val + node.val)
        #         if l_v < limit:
        #             node.left = None
        #     if node.right is not None:
        #         l_r = dfs(node.right, val + node.val)
        #         if l_r < limit:
        #             node.right = None
        #     print(l_v, l_r)
        #     return val + node.val
        # dfs(root, limit)

        root_delete = self._dfs(root, 0, limit)
        return None if root_delete else root


if __name__ == '__main__':
    so = Solution()
