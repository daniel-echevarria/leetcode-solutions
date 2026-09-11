# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        currA = headA
        currB = headB
        loopA = 0
        loopB = 0
        while currA != currB:
            currA = currA.next
            currB = currB.next
            if not currA:
                currA = headB
                loopA += 1
            if not currB:
                currB = headA
                loopB += 1
            if loopA and loopB and (loopA > 1 or loopB > 1):
                return None
        return currA


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
