# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode("#")
        dummy_l = left
        right = ListNode("#")
        dummy_r = right

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = dummy_r.next
        right.next = None
        return dummy_l.next


head = [1, 4, 3, 2, 5, 2]
x = 3
