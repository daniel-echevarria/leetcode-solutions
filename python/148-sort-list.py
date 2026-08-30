# Definition for singly-linked list.
# class Listhead:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[Listhead]) -> Optional[Listhead]:
        if not head or not head.next:
            return head

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        sorted_left = self.sortList(head)
        sorted_right = self.sortList(mid)
        merged = Listhead(0)
        current = merged
        while sorted_left and sorted_right:
            if sorted_left.val < sorted_right.val:
                current.next = sorted_left
                sorted_left = sorted_left.next
            else:
                current.next = sorted_right
                sorted_right = sorted_right.next

            current = current.next
        current.next = sorted_left or sorted_right
        return merged.next


[4, 2, 1, 3]
