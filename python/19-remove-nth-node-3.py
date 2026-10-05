# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        a = b = head

        for _ in range(n):
            a = a.next

        while a:
            a = a.next
            b = b.next

        b.next = b.next.next

        return head
