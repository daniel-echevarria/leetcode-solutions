class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        rest_idx = {}
        curr_sum = 0
        rest_idx[0] = -1
        for i, n in enumerate(nums):
            curr_sum += n
            rest = curr_sum % k
            if rest in rest_idx:
                if rest_idx[rest] < i - 1:
                    return True
            else:
                rest_idx[rest] = i
        if curr_sum % k == 0:
            return True
        return False


# nums = [23, 2, 4, 6, 7]
# nums = [23, 2, 4, 6, 6]
nums = [2, 4, 3]
k = 6
s = Solution()
print(s.checkSubarraySum(nums, k))
# Algo make a prefix sum  and a modulo k list
# make map of the indexes for each value found in the modulo list, if two indexes are found are are further than 2 indexes
# apart return true, else after iteration return false
