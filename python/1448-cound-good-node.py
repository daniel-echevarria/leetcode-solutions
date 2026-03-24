# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxSeen):
            if not node:
                return 0
            local_good = 1 if node.val >= maxSeen else 0
            maxSeen = max(maxSeen, node.val)
            return local_good + helper(node.left, maxSeen) + helper(node.right, maxSeen)

        return helper(root, float("-inf"))


# Algo traverse the tree with dfs while passing the largest node met so far
# return the local good + the left and right good ones
