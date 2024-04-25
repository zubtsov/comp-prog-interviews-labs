import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        if n == 1:
            return True
        else:
            return False

    def isPowerOfThree2(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 2:
            return False
        log_n_3 = math.log(n, 3)
        return abs(round(log_n_3) - log_n_3) < 1e-14
