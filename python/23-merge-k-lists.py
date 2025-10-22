from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(float("-inf"))
        if not lists:
            return

        def merge(l1, l2, current):
            if not l1:
                current.next = l2
                return dummy
            if not l2:
                current.next = l1
                return dummy
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
            return merge(l1, l2, current)

        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            res = merge(l1, l2, dummy)
            lists.append(res.next)

        return lists[0]


lists = [ListNode(2), ListNode(), ListNode(-1)]
s = Solution()
s.mergeKLists(lists)


# Brute force
# make a mother list
# for eah list remove first node and place it in the mother list
