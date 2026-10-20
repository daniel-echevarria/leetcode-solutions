# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode("#", head)
        curr = prev = dummy

        while curr:
            count = 1
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                count += 1

            if count == 1:
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode("#", head)
        curr = prev = dummy

        while curr:
            if curr.next and curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next
        return dummy.next
