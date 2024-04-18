from typing import List


class Solution:
    def equal_at_index(self, strs: List[str], ind) -> bool:
        for i in range(len(strs) - 1):
            if ind == len(strs[i]) or \
                    ind == len(strs[i + 1]) or \
                    strs[i][ind] != strs[i + 1][ind]:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        i = 0
        while self.equal_at_index(strs, i):
            i += 1

        return strs[0][:i]


if __name__ == '__main__':
    s = Solution()
    strs = ["flower","flow","flight"]
    print(s.longestCommonPrefix(strs))