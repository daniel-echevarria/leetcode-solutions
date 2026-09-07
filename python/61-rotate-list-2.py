# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if not k:
            return head

        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head


[1, 2, 3, 4, 5]
