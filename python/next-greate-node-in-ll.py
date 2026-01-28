# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        values = [head.val]
        next_bigger = [0]
        current = head.next
        while current:
            head = head.next


# Bruteforce:
# Iterate through the ll
# keep track of the first_non_assigned index
# the moment the slope goes up, compare all the non assigned indexes from the forst one and update them if the value
# is smaller than the current value
