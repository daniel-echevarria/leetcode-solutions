# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        pStack = None
        qStack = None

        def helper(node, stack=[]):
            nonlocal pStack, qStack
            if not node or (pStack and qStack):
                return

            stack.append(node)
            if node.val == p.val:
                pStack = stack
            elif node.val == q.val:
                qStack = stack
            helper(node.left, stack.copy())
            helper(node.right, stack.copy())

        helper(root)
        if len(pStack) > len(qStack):
            pStack, qStack = qStack, pStack
        while len(qStack) > len(pStack):
            qStack.pop()
        while qStack and pStack:
            pAncestor = pStack.pop()
            qAncestor = qStack.pop()
            if pAncestor == qAncestor:
                return pAncestor


# Algo, build a stack as we go down the tree
# the moment we meet the target we update the stack
# the moment we meet both targets we return early
# then we pop from the biggest stack until the size matches
# then we pop until the value matches, that's our LCA
