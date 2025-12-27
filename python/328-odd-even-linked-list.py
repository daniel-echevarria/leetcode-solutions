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
