class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        even = ListNode()
        even_ref = even
        odd = head
        prev = None

        while odd:
            even.next = odd.next
            if odd.next:
                odd.next = odd.next.next
            prev = odd
            odd = odd.next
            even = even.next

        prev.next = even_ref.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        og_even = even
        prev = None
        while odd and even:
            if odd.next:
                prev = odd
                odd.next = odd.next.next
                odd = odd.next
            if even.next:
                even.next = even.next.next
                even = even.next
        if odd:
            odd.next = og_even
        else:
            prev.next = og_even
        return head


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        head_even = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = head_even
        return head
