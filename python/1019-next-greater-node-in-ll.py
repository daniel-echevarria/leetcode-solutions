class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head):
        stack = []
        values = []
        res = []
        index = 0
        while head:
            current_val = head.val
            values.append(current_val)
            res.append(0)
            while stack and values[stack[-1]] < current_val:
                idx = stack.pop()
                res[idx] = current_val
            stack.append(index)
            index += 1
            head = head.next
        return res


s = Solution()
head = [2, 1, 5]
print(s.nextLargerNodes(head))
# Create a stack
# Create res array
# create a values array
# Iterate through the linked list and for each node do the following
# add the value to the values array
# add a 0 to the result array
# so long as values at the index popped from the stack are smaller than the current value
# update the index of the res array with the current value
# return the res array
