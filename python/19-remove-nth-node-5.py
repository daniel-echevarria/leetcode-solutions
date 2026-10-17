# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode("#", head)
        a = b = dummy

        for _ in range(n):
            b = b.next

        while b.next:
            b = b.next
            a = a.next

        a.next = a.next.next
        return dummy.next
