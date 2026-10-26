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

        if not fast.next or not fast.next.next:
            return head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        right = prev
        left = head

        while right:
            right_next = right.next
            left_next = left.next

            left.next = right
            right.next = left_next
            left = left_next
            right = right_next

        return head
