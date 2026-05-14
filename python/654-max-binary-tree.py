# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]):
        if not nums:
            return
        val = max(nums)
        idx = nums.index(val)

        node = TreeNode(val)
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1 :])
        return node


nums = [3, 2, 1, 6, 0, 5]
s = Solution()
print(s.constructMaximumBinaryTree(nums))


# Algo make an array including the index as the second number
# recursively construct the maxBinaryTree
