# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        return arr == list(reversed(arr))


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        prev = None

        if not head or not head.next:
            return True

        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        r = slow.next if fast else slow
        l = prev

        while r:
            if not r.val == l.val:
                return False
            r = r.next
            l = l.next

        return l == r


[1, 2, 2, 1]

# use fast and slow pointers, when moving the slow pointer, reverse the list
# when reaching the middle of the list
# move in both directions and compare the values
