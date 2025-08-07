# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        self.current_index = -1

    def next(self) -> int:
        self.current_index += 1
        return self.inorder[self.current_index]

    def hasNext(self) -> bool:
        return self.current_index < len(self.inorder) - 1
