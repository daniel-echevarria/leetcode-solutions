from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return

        def merge(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l2.next, l1)
                return l2

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                res = merge(l1, l2)
                merged.append(res)
            lists = merged

        return lists[0]


lists = [ListNode(2), ListNode(), ListNode(-1)]
s = Solution()
s.mergeKLists(lists)


# Brute force
# make a mother list
# for eah list remove first node and place it in the mother list
