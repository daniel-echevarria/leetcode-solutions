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


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))

        swap_position = None
        for i in range(len(n) - 1, 0, -1):
            if n[i] > n[i - 1]:
                swap_position = i - 1
                break

        if swap_position is None:
            return -1

        for i in range(len(n) - 1, -1, -1):
            if n[i] > n[swap_position]:
                n[i], n[swap_position] = n[swap_position], n[i]
                break
        n[swap_position + 1 :] = reversed(n[swap_position + 1 :])
        res = int("".join(n))

        if res > 2147483647:
            return -1
        else:
            return res


# Check the last int in the number
# check if it's bigger than any number to the left
# if it is, swap it directly, otherwise move to the next number

# mark that index as placed
# sort the rest
# return the joined version

s = Solution()
print(s.nextGreaterElement(12))
