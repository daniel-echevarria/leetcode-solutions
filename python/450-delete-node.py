# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummyRoot = TreeNode(float("inf"), root, None)

        def cherryPickNextSmallest(root):
            node = root
            while node.left:
                node = node.left
            if node.right:
                return node.right
            if node == root:
                return None
            else:
                return node

        def helper(node):
            if not node:
                return
            if node.left and node.left.val == key:
                nextSmallest = cherryPickNextSmallest(node.left)
                print(nextSmallest)
                if not nextSmallest:
                    node.left = node.left.left
                    return
                else:
                    tempLeft = node.left.left
                    tempRight = node.right.right
                    node.left = nextSmallest
                    nextSmallest.left = tempLeft
                    nextSmallest.right = tempRight
                    return
            if node.right and node.right.val == key:
                nextSmallest = cherryPickNextSmallest(node.right)
                if not nextSmallest:
                    node.right = None
                    return
                else:
                    tempLeft = node.right.left
                    tempRight = node.right.right
                    node.right = nextSmallest
                    nextSmallest.left = tempLeft
                    nextSmallest.right = tempRight
                    return
            if node.val < key:
                helper(node.right)
            else:
                helper(node.left)

        helper(dummyRoot)
        return dummyRoot.left


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right and not root.left:
                return None
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val

            root.right = self.deleteNode(root.right, root.val)
        return root


# Algo if the root val matches the key
# look for the next bigger node
# pick that node and make it the new root
