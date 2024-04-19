class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if len(haystack) < len(needle):
            return -1

        start_haystack_index = 0

        max_haystack_index = len(haystack) - len(needle) + 1
        while start_haystack_index < max_haystack_index:
            current_haystack_index = start_haystack_index

            current_needle_index = 0
            while current_needle_index < len(needle) and \
                    current_haystack_index < len(haystack) and \
                    haystack[current_haystack_index] == needle[current_needle_index]:
                current_needle_index += 1
                current_haystack_index += 1
            if current_needle_index == len(needle):
                return start_haystack_index
            start_haystack_index += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    haystack = "a"
    needle = "a"
    print(s.strStr(haystack, needle))
