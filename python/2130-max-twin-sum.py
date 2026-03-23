# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        my_list = []

        while curr:
            my_list.append(curr.val)
            curr = curr.next
        n = len(my_list)
        maxTwin = 0
        for i in range(n // 2):
            maxTwin = max(maxTwin, my_list[i] + my_list[n - 1 - i])
        return maxTwin


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        maxTwin = 0
        while prev:
            maxTwin = max(maxTwin, prev.val + head.val)
            prev = prev.next
            head = head.next
        return maxTwin


# bruteforce, build an array of the list
# iterate half of the list matching it with the twin and keeping track of the max
