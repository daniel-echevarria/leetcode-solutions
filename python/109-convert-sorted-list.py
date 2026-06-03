# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        my_list = []
        while head:
            my_list.append(head.val)
            head = head.next

        def build_tree(l):
            if not l:
                return
            mid = len(l) // 2
            root = TreeNode(l[mid])
            root.left = build_tree(l[:mid])
            root.right = build_tree(l[mid + 1 :])
            return root

        return build_tree(my_list)


# Algo, find the middle (fast slow)
# split into left and right,
# recurse
