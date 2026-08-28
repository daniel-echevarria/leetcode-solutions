# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        fast = head

        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head_copy = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        fast = head_copy

        while True:
            if fast == slow:
                return slow
            fast = fast.next
            slow = slow.next


# [3, 2, 0, -4]
[1, 2]
