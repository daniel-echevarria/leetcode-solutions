# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        current = head
        prev = dummy_head
        post = None
        while current:
            reversing = []
            for _ in range(k):
                if not current:
                    break
                reversing.append(current)
                current = current.next
            if len(reversing) < k:
                prev.next = reversing[0]
                break
            post = current.next if current else None
            prev.next = reversing[-1]
            for _ in range(k):
                node = reversing.pop()
                if not reversing:
                    node.next = post
                    prev = node
                else:
                    node.next = reversing[-1]
        return dummy_head.next
