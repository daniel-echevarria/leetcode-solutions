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
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = slow
        prev = None
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp

        top = head
        bot = prev
        while bot.next:
            temp = top.next
            top.next = bot
            temp2 = bot.next
            bot.next = temp
            top = temp
            bot = temp2


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        # find mid
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while mid:
            temp = mid
            mid = mid.next
            temp.next = prev
            prev = temp

        left = head
        right = prev
        hold = right

        while left and right:
            temp = left.next
            left.next = right
            left = temp
            hold = right.next
            right.next = left
            right = hold
        return head


[1, 2, 3, 4]
