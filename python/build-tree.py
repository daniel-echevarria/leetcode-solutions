class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]):
        def helper(ino):
            if len(ino) == 1:
                return TreeNode(postorder.pop())
            if len(ino) == 0:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)
            root.right = helper(ino[ino.index(root_val) + 1 :])
            root.left = helper(ino[: ino.index(root_val)])
            return root

        return helper(inorder)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
s = Solution()
print(s.buildTree(inorder, postorder))
