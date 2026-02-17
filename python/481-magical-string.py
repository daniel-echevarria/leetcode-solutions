class Solution:
    def magicalString(self, n: int) -> int:
        magic = [1, 2, 2]
        idx = 2

        while len(magic) < n:
            next_num = 3 - magic[-1]
            curr = magic[idx]
            magic += [next_num] * curr
            idx += 1

        return magic[:n].count(1)


s = Solution()
n = 6
print(s.magicalString(n))


# Algo
# build a magical string until the string is of length n
# how to build a magical string
# give the string a value of 1
# start at index 0
# the counter gets the value at index 0
# while the counter add the current to the reflex string
