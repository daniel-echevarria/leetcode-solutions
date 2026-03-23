# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_leaves = []
        right_leaves = []

        def helper(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            helper(node.left, leaves)
            helper(node.right, leaves)

        helper(root1, left_leaves)
        helper(root2, right_leaves)

        return left_leaves == right_leaves
