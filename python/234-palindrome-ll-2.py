# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None

        while fast.next and fast.next.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast == slow:
            return True if not fast.next else fast.val == fast.next.val

        right = slow.next
        slow.next = prev

        if not fast.next:
            slow = slow.next
        left = slow

        while left or right:
            if not left or not right or left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast:
            slow = slow.next

        left, right = prev, slow

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


[1, 2, 2, 1]
[0, 0]
