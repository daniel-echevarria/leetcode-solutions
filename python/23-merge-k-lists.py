from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class LinkedList:
    def __init__(self):
        self.root = ListNode(float("-inf"))

    def add(self, val, current, previous=None):
        if not current or val < current.val:
            node = ListNode(val, current)
            if previous:
                previous.next = node
            return
        self.add(val, current.next, current)


class Solution:
    def mergeKLists(self, lists):
        mother_list = LinkedList()
        if not lists:
            return
        while lists:
            for i, list in enumerate(lists):
                if not list:
                    del lists[i]
                    continue
                mother_list.add(list.val, mother_list.root)
                lists[i] = list.next
        return mother_list.root.next


# s = Solution()
# s.mergeKLists()


# Brute force
# make a mother list
# for eah list remove first node and place it in the mother list
