# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def place_node(head, node):
            while head:
                if node.val >= head.val and node.val <= head.next.val:
                    node.next = head.next
                    head.next = node
                    return
                head = head.next
            head.next = node

        dummy = ListNode(float("-inf"), head)
        current = head
        prev = dummy
        while current:
            if current.val >= prev.val:
                current = current.next
                prev = prev.next
                continue
            prev.next = current.next
            place_node(dummy, current)
            current = prev.next
        return dummy.next


[4, 2, 1, 3]
