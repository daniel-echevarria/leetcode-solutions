# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth=0):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left_depth = 1 + helper(node.left)
            right_depth = 1 + helper(node.right)
            return max(left_depth, right_depth)

        return helper(root)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
