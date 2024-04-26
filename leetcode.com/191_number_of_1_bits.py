class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        number_of_set_bits = 0
        while n > 0:
            number_of_set_bits += (n & mask)
            n >>= 1
        return number_of_set_bits


if __name__ == '__main__':
    print(Solution().hammingWeight(5))
