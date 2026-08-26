# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        right = ListNode(0)
        left_head = ListNode(0, left)
        right_head = ListNode(0, right)

        while head:
            if head.val < x:
                head = head
                head = head.next
                left.next = head
                left = left.next
                left.next = None
            else:
                head = head
                head = head.next
                right.next = head
                right = right.next
                right.next = None
        left.next = right_head.next.next
        return left_head.next.next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        right = ListNode(0)
        left_head = left
        right_head = right

        while head:
            next_node = head.next

            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = next_node

        left.next = right_head.next
        right.next = None
        return left_head.next


head = [1, 4, 3, 2, 5, 2]
x = 3
