class Solution:
    
    def _square(self, c):
        x = int(c)
        return x * x

    def _sum_of_digits(self, n: int):
        return sum(map(self._square, str(n)))

    def isHappy(self, n: int) -> bool:
        looped = {n}

        s = self._sum_of_digits(n)
        while s != 1:
            if s in looped:
                return False
            else:
                n = s
            looped.add(s)
            s = self._sum_of_digits(n)
        return True


if __name__ == '__main__':
    print(Solution().isHappy(7))
