# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        dummy = head

        while head:
            lst.append(head)
            head = head.next

        idx = len(lst) - n

        if idx > 0:
            lst[idx - 1].next = lst[idx].next
        else:
            dummy = dummy.next

        return dummy
