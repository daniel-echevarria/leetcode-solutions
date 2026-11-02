# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head.next:
            return True

        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left = prev
        right = slow

        if fast:
            right = slow.next

        while left:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# find the middle of the array with fast and slow pointers
# while moving the slow pointer reverse the left side of the list
# while doing that get the length of the list
# once reached the middle
# place the left pointer based on weather the list is odd or even
# compare all the remaning nodes to see if their values match (palindrome)
