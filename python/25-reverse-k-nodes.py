# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        current = head
        prev = dummy_head
        post = None
        while current.next:
            reversing = []
            for _ in range(k):
                if not current:
                    break
                reversing.append(current)
                current = current.next
            if len(reversing) < k:
                break
            post = current.next
            prev.next = reversing[-1]
            for _ in range(k):
                node = reversing.pop()
                if not reversing:
                    node.next = post
                    prev = node
                else:
                    node.next = reversing[-1]
        return dummy_head.next


# Algo
# Keep track of the pre_reversing node and the post_reversing node
# Make a dummy head to be able to return the modified list in the end
# Declare a current var with initial value of head
# prev gets dummy
# launch a loop until current next is null
# inside the loop reverse the nodes as such:
# declare a list of reversing
# launch a for loop pushing the nodes to reversing and updating current
# after the loop post gets current next
# point prev next to the reversing last
# pop them one by one pointing to reversing last
# prev gets current
# current next gets post
# keep going
