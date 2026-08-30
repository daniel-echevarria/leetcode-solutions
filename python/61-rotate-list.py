# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        pointer1 = head
        if not pointer1 or not pointer1.next or not k:
            return dummy.next

        for _ in range(k):
            if not pointer1.next:
                pointer1 = dummy.next
                continue
            pointer1 = pointer1.next

        if not pointer1.next:
            pointer1.next = dummy.next

        pointer2 = new_head = pointer1.next
        pointer1.next = None
        while pointer2.next:
            pointer2 = pointer2.next
        pointer2.next = dummy.next

        return new_head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        fast = slow = dummy
        length = 0
        while fast and fast.next:
            fast = fast.next
            length += 1

        if length < 2:
            return head

        remainder = k % length

        fast = dummy
        for _ in range(remainder):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        if not new_head:
            return head
        slow.next = None
        fast.next = dummy.next
        return new_head


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

        if k == 0:
            return head

        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        tail.next = head
        new_head = new_tail.next
        new_tail.next = None

        return new_head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        length = 1
        tail = head
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
        tail.next = head
        new_tail.next = None
        return new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if not k:
            return head

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


# [1, 2, 3, 4, 5]
[0, 1, 2]
