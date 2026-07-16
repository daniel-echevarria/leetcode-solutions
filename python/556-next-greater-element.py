class Solution:
    def nextGreaterElement(self, n: int) -> int:
        string_version = list(str(n))
        swaps = 0
        swap_idx = 0
        for i in range(len(str(n)) - 1, -1, -1):
            if swaps:
                break
            j = i - 1
            while j >= 0:
                if string_version[i] > string_version[j]:
                    temp = string_version[i]
                    string_version[i] = string_version[j]
                    string_version[j] = temp
                    swap_idx = j
                    swaps += 1
                    break
                j -= 1
        if not swaps:
            return -1

        return int(
            "".join(
                string_version[: swap_idx + 1]
                + sorted((string_version[swap_idx + 1 :]))
            )
        )


s = Solution()
print(s.nextGreaterElement(1342))

# Check the last int in the number
# check if it's bigger than any number to the left
# if it is, swap it directly, otherwise move to the next number

# mark that index as placed
# sort the rest
# return the joined version

32413
