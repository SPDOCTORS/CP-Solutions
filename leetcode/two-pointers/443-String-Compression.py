class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        write = 0

        while i < len(chars):
            start = i

            while i < len(chars) and chars[i] == chars[start]:
                i += 1

            count = i - start

            chars[write] = chars[start]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write

        