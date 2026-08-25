# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy
        a = b = head
        more_than_one = False

        while b and b.next:
            if a.val == b.next.val:
                b = b.next
                more_than_one = True
                continue
            if more_than_one:
                prev.next = b.next
                more_than_one = False
            else:
                prev = a
            a = b.next
            b = b.next
        if more_than_one:
            prev.next = b.next
        return dummy.next


head = [1, 2, 3, 3, 4, 4, 5]
