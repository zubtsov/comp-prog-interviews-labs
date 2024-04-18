class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        l = len(n)
        for i in range(l // 2):
            if n[i] != n[l - i - 1]:
                return False
        return True
