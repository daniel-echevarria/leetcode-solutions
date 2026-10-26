# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        left, right = head, prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        return head
