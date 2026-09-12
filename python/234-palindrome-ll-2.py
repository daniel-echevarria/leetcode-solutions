# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None

        while fast.next.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast.next:

