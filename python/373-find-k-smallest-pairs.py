class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        current_min = 0
        current_array = nums1 if nums1[0] <= nums2[0] else nums2
        iterating_array = nums2 if current_array == nums1 else nums1
        l, r = 0, 0
        pairs = []
        while True:
            if len(pairs) == k:
                return pairs
            if r == len(iterating_array):
                l += 1
                r = 0
            current_min = current_array[l] + iterating_array[r]
            if (
                l < len(current_array) - 1
                and current_min > current_array[l + 1] + iterating_array[0]
            ):
                temp = current_array
                current_array = iterating_array
                iterating_array = temp
                l, r = 0, l + 1
            pairs.append((current_array[l], iterating_array[r]))
            r += 1


s = Solution()
# nums1 = [1, 7, 11]
# nums2 = [2, 4, 6]
nums1 = [1, 2, 4, 5, 6]
nums2 = [3, 5, 7, 9]
k = 7
print(s.kSmallestPairs(nums1, nums2, k))


# Algo
# Define a variable current_min with initial value of 0
# Declare a variable current_array that gets the array with the smallest value
# Declare a variable iterating_array that gets the other array
# Iterate while the sum is smaller than the sum of the first iterating + the next of the current
# Then switch
