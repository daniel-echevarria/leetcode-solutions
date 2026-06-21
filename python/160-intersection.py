# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        nodeA, nodeB = headA, headB

        countA = 0
        countB = 0

        while nodeA or nodeB:
            if nodeA == nodeB:
                return nodeA
            if nodeA:
                countA += 1
                nodeA = nodeA.next
            if nodeB:
                countB += 1
                nodeB = nodeB.next

        bigger = headA if countA > countB else headB
        smaller = headA if bigger == headB else headB

        diff = abs(countA - countB)

        while diff and bigger:
            bigger = bigger.next
            diff -= 1

        while bigger and smaller:
            if bigger == smaller:
                return bigger
            bigger = bigger.next
            smaller = smaller.next


# make both traversals, if one is finish, start counting how much longer the other one is
# start from that point on with the second one, return the moment they are the same
