class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        result = [nums[0]]

        def binary_replace(num):
            l, r = 0, len(result)

            while l < r:
                mid = (l + r) // 2
                if result[mid] == num:
                    return
                if result[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            result[l] = num

        for i in range(1, len(nums)):
            if nums[i] > result[-1]:
                result.append(nums[i])
            else:
                binary_replace(nums[i])

        return len(result)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
s = Solution()
print(s.lengthOfLIS(nums))

# Algo:
# declare a variable result with initial value of nums[0]
# iterate through the array from index 1
# if the current value is bigger than the previous
# add it to the result array
# otherwise replace with the value that maintains order
