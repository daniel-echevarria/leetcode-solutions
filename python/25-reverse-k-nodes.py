# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

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

