class Solution:
    def firstUniqChar(self, s: str) -> int:

        ignore = set()
        first_time_met = {}

        for i in range(len(s)):
            c = s[i]
            if c in ignore:
                continue
            if c in first_time_met:
                ignore.add(c)
                del first_time_met[c]
            else:
                first_time_met[c] = i

        for ind in first_time_met.values():
            return ind
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("loveleetcode"))
