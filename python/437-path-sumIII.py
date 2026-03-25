# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def helper(node, paths=[]):
            if node is None:
                return 0
            new_paths = [x + node.val for x in paths]
            new_paths.append(node.val)
            local_match = new_paths.count(targetSum)
            return (
                local_match
                + helper(node.left, new_paths.copy())
                + helper(node.right, new_paths.copy())
            )

        return helper(root)
