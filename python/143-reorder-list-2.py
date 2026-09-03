# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        right_head = mid.next
        mid.next = None

        # reverse right part
        prev = None
        while right_head:
            temp = right_head
            right_head = right_head.next
            temp.next = prev
            prev = temp
        left = head
        right = prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        return head


head = [1, 2, 3, 4, 5]
