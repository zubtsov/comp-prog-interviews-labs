class Solution:
    def tribonacci(self, n: int) -> int:
        trb = [0, 1, 1]

        if n <= 2:
            return trb[n]

        for i in range(3, n + 1):
            trb[i % 3] = (trb[0] + trb[1] + trb[2])
        return trb[n % 3]


if __name__ == '__main__':
    print(Solution().tribonacci(25))
