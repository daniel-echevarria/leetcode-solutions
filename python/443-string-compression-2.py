class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        i, j = 0, 1

        while j < n:
            while j < n and chars[j] == chars[i]:
                j += 1
            count = j - i
            num = count if count > 1 else ""
            s = f"{chars[i]}{num}"
            chars[i:j] = list(s)
            i = j
            j += 1
            n -= count - len(s)


class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        i, j = 0, 1
        while j < n:
            count = 0
            while j < n and chars[j] == chars[i]:
                j += 1
                count += 1
            num = count if count > 1 else ""
            s = list(f"{chars[i]}{num}")
            for k in range(i, j):
                chars[k] = s.pop(0) if s else ""
            i = j


class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write, read = 0, 1

        while read < n:
            count = 1
            while read < n and chars[read] == chars[read - 1]:
                count += 1
                read += 1
            if count < 2:
                read += 1
                write += 1
                continue
            s = f"{chars[write]}{count}"
            chars[write : write + len(s)] = list(s)
            write += len(s)


class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write = read = 0

        while read < n:
            count = 0
            char = chars[read]
            while read < n and chars[read] == char:
                read += 1
                count += 1
            num = count if count > 1 else ""
            s = f"{char}{num}"
            for char in s:
                chars[write] = char
                write += 1
        return write


chars = ["a", "b", "b", "c", "c", "c", "b", "b", "b", "b", "b", "b", "b"]
s = Solution()
print(s.compress(chars))
