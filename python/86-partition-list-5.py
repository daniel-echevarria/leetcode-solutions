# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        left_dummy = ListNode()
        right_dummy = ListNode()
        left = left_dummy
        right = right_dummy
        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next

        right.next = None
        left.next = right_dummy.next
        return left_dummy.next
