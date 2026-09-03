# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow
        right_head = mid.next
        mid.next = None
        left_head = head
        sorted_left = self.sortList(left_head)
        sorted_right = self.sortList(right_head)

        dummy = ListNode("#")
        current = dummy
        while sorted_left and sorted_right:
            if sorted_left.val < sorted_right.val:
                current.next = sorted_left
                sorted_left = sorted_left.next
            else:
                current.next = sorted_right
                sorted_right = sorted_right.next

            current = current.next
        current.next = sorted_left or sorted_right
        return dummy.next


[4, 2, 1, 3]
