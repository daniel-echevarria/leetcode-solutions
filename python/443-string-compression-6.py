class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write = 0
        read = 0

        while read < n:
            count = 0
            char = chars[read]

            while read < n and chars[read] == char:
                read += 1
                count += 1

            num = count if count > 1 else ""
            comp = f"{char}{num}"

            for c in comp:
                chars[write] = c
                write += 1

        return write


chars = ["a", "a", "b", "b", "c", "c", "c"]
s = Solution()
s.compress(chars)
