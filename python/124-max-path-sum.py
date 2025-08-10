# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return float("-inf")
            if not node.left and not node.right:
                return node.val
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            self.max_sum = max(
                node.val,
                max_left,
                max_right,
                (max_left + max_right + node.val),
                self.max_sum,
            )
            return max(max(max_left, max_right) + node.val, node.val)

        root_max = dfs(root)
        return max(self.max_sum, root_max)
