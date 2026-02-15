# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        turtle = head
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                return True
        return False


# Algo:
# Iterate through the list while keeping track of the visited nodes in a set
# if the next node is in the set return true else after traversin the list return false
