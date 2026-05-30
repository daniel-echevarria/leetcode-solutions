# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        queue = deque(preorder)

        def builder(inorder_list):
            if not inorder_list:
                return
            root_val = queue.popleft()
            idx = inorder_list.index(root_val)
            root = TreeNode(root_val)
            root.left = builder(inorder_list[:idx])
            root.right = builder(inorder_list[idx + 1 :])
            return root

        return builder(inorder)


# Algo, make the preorder a queue,
# define a helper that given an array (inorder)
# if popsleft from preorder, finds the index of the value in itself
# make a node out of it, and recurses with the left and right part
