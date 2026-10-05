class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write = read = 0

        while read < n:
            char = chars[read]
            count = 0
            while read < n and char == chars[read]:
                read += 1
                count += 1
            num = count if count > 1 else ""

            s = f"{char}{num}"
            for v in s:
                chars[write] = v
                write += 1
        return write
