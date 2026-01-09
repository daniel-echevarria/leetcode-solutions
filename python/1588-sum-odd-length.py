class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = sub_len = len(arr)
        total = sum(arr)
        while sub_len > 2:
            if sub_len % 2 == 0:
                sub_len -= 1
                continue
            l, r = 0, sub_len
            while r <= n:
                total_sub = sum(arr[l:r])
                total += total_sub
                l += 1
                r += 1
            sub_len -= 2
        return total


class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        l = len(arr)
        total = 0

        for i, n in enumerate(arr):
            left = i + 1
            right = l - i

            odd_left = (left + 1) // 2
            even_left = (left) // 2
            odd_right = (right + 1) // 2
            even_right = (right) // 2

            count = (odd_left * odd_right) + (even_left * even_right)
            total += n * count
        return total


s = Solution()
arr = [1, 4, 2, 5, 3]
print(s.sumOddLengthSubarrays(arr))


# Algo
# declare a variable n that get the length of the array
# declare a variable total that gets 0
# loop until n is 0
# if n is even continue
# otherwise traverse the array accumulating the sum of the arrays
# of length n in the total
# return the total
