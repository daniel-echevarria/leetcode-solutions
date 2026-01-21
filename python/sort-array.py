class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[0:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            res = []
            l = r = 0
            while True:
                if l == len(left):
                    return res + right[r:]
                if r == len(right):
                    return res + left[l:]

                if left[l] < right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

        return merge_sort(nums)


s = Solution()
nums = [5, 2, 3, 1]
print(s.sortArray(nums))

# Use merge sort:
# sort left
# sort right
# merge
