class Solution:
    SHIFT = ord('a')
    HASH_MAP_SIZE = ord('z') - SHIFT + 1

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        available_symbols = [0] * self.HASH_MAP_SIZE

        for i in range(len(s)):
            available_symbols[ord(s[i]) - self.SHIFT] += 1
        for i in range(len(t)):
            available_symbols[ord(t[i]) - self.SHIFT] -= 1
        for i in range(self.HASH_MAP_SIZE):
            if available_symbols[i] != 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram('abc', 'cba'))
