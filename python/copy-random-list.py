"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        current = head
        old_new_map = {}

        def create_copy(node):
            if not node:
                return None
            if node in old_new_map:
                return old_new_map[node]
            copy = Node(node.val)
            old_new_map[node] = copy
            copy.next = create_copy(node.next)
            copy.random = create_copy(node.random)
            return copy

        copy = create_copy(current)
        return copy


# Traverse the list once while storing
