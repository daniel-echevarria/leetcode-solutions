class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        read = write = 0

        while read < n:
            count = 0
            char = chars[read]

            while read < n and chars[read] == char:
                count += 1
                read += 1

            num = count if count > 1 else ""
            comp = f"{char}{num}"

            for v in comp:
                chars[write] = v
                write += 1
        return write
