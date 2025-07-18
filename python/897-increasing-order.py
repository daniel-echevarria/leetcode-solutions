class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        fresh_root = TreeNode()

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            placeNode(node, fresh_root)
            dfs(node.right)

        dfs(root)
        return fresh_root.right


def placeNode(node, current):
    if not current.right:
        current.right = TreeNode(node.val)
        return
    placeNode(node, current.right)
