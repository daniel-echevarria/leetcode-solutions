class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return
        main_queue = deque([node])
        new_root = Node(node.val)
        copy_queue = deque([new_root])
        visited = set()

        while main_queue:
            for _ in range(len(main_queue)):
                original = main_queue.popleft()
                copy = copy_queue.popleft()
                for n in original.neighbors:
                    if n not in visited:
                        visited.add(n)
                        neighbor_copy = Node(n.val)
                        copy.neighbors.append(neighbor_copy)
                        copy_queue.append(neighbor_copy)
                        main_queue.append(n)
        return new_root
