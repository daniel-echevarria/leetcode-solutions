class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)

        read = write = 0

        while read < n:
            char = chars[read]
            count = 0
            while read < n and char == chars[read]:
                read += 1
                count += 1
            num = count if count > 1 else ""
            s = f"{char}{num}"
            for c in s:
                chars[write] = c
                write += 1
        return write
