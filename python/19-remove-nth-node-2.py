# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        a = b = dummy

        for _ in range(n):
            b = b.next

        while b and b.next:
            a = a.next
            b = b.next

        a.next = a.next.next

        return dummy.next


head = [d, 1, 2, 3, 4, 5]
n = 2
