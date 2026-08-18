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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        slow = fast = head
        s_pos = f_pos = 0
        while fast:
            fast = fast.next
            f_pos += 1
            if f_pos % n == 0:
                slow = slow.next
                s_pos += 1

        goal = f_pos - n
        while slow:
            if s_pos == goal - 1:
                slow.next = slow.next.next
                return dummy
            slow = slow.next
            s_pos += 1
        return dummy
