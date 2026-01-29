# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        stack = []
        res = []
        idx = 0
        while head:
            while stack and values[stack[-1]] < head.val:
                smaller_idx = stack.pop()
                res[smaller_idx] = head.val
            values.append(head.val)
            stack.append(idx)
            res.append(0)
            head = head.next
            idx += 1
        return res


# Iterate through the linked list while adding the index to a stack
# and creating an array of the met values;
# when adding the indexes, if the stack is empty
# just continue
# otherwise pop until the value is equal or bigger that the current value
# and for each of this popes values add the current value at that index in the answer
