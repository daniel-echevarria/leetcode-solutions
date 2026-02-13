import heapq
import itertools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        motherList = ListNode()
        dummy = motherList
        heap = []
        counter = itertools.count()

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, next(counter), l))

        while heap:
            _, _, l = heapq.heappop(heap)
            motherList.next = l
            motherList = motherList.next
            if l.next:
                heapq.heappush(heap, (l.next.val, next(counter), l.next))

        return dummy.next
