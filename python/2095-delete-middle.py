# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        idx = len(nodes) // 2
        if idx == 0:
            return None
        prev = nodes[idx - 1]
        middle = nodes[idx]
        prev.next = middle.next
        return dummy.next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        dummy = ListNode(next=head)
        prev_slow = ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev_slow = prev_slow.next
        if slow == fast:
            return None
        prev_slow.next = slow.next
        return dummy.next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head


# Traverse the linked list while keeping track of the nodes in an array
# after traversing the list check the length
# remove the middle node
# return the linked list
