import random


class Solution:
    def reverseBits(self, n: int) -> int:
        rb = 0
        for i in range(32):
            rb |= ((n & (1 << i)) >> i) << (31 - i)
        return rb


if __name__ == '__main__':
    n = random.randint(0, 2 ^ 32)
    print(f"n={n}: {bin(n)}")
    reversed_bits = Solution().reverseBits(n)
    print(f"n={reversed_bits}: {bin(reversed_bits)}")
