from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        current_round = deque([root])
        next_round = deque()

        if not root:
            return []

        while current_round or next_round:
            if not current_round:
                current_round = next_round
                next_round = deque()
                continue
            elif len(current_round) == 1:
                res.append(current_round[0].val)
            node = current_round.popleft()
            if node.left:
                next_round.append(node.left)
            if node.right:
                next_round.append(node.right)
        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


# Algo:
# declare a current round and a next round queues
# dequeue from the current round while adding the childrent nodes to the next round
# the moment there is only one in the current round, push it's value to the result
# when the current round is empty move the next round up and empty the next round
# do that so long as at least one of the rounds has nodes
