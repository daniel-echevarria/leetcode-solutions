# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def helper(node, direction=None, currentLength=0):
            if not node:
                return
            nonlocal longest
            longest = max(longest, currentLength)

            helper(node.left, "left", 1 if direction == "left" else currentLength + 1)
            helper(
                node.right,
                "right",
                1 if direction == "right" else currentLength + 1,
            )

        helper(root)
        return longest


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def helper(node, left_len=0, right_len=0):
            if not node:
                return
            nonlocal longest
            longest = max(longest, left_len, right_len)

            helper(node.left, 1, right_len + 1)
            helper(node.right, left_len + 1, 1)

        helper(root)
        return longest


# Algo
# Traverse the tree in a dfs fashion keeping track of the previous direction
# if the direction changes keep with the count of length
# otherwise restart the count
# keep track of the longest length in an external variable
