class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        double = [2 * x for x in nums] + [float("inf")]
        total = 0
        for i, n in enumerate(nums):
            for v in double[i + 1 :]:
                if v < n:
                    total += 1
        return total


class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        total = 0

        def merge(arr1, arr2):
            res = []
            l = r = 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l] < arr2[r]:
                    res.append(arr1[l])
                    l += 1
                else:
                    res.append(arr2[r])
                    r += 1
            return res + arr1[l:] + arr2[r:]

        def merge_sort(arr):
            nonlocal total
            if len(arr) < 2:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                total += j

            return merge(left, right)

        merge_sort(nums)
        return total


s = Solution()
# nums = [-5, -5]
nums = [2, 4, 3, 5, 1]
print(s.reversePairs(nums))

# Bruteforce:
# create an array of the double of nums
# iterate through nums and for each num check from that num on
# If there is a value in the double that  is smaller than the current one
# keep track of the count and return it

# Merge sort:
# Do a merge sort, any time there is a swap, if the left is bigger than twice the value on the left
# add 1 to total
