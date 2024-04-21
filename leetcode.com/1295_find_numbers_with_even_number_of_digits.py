from typing import List
from math import log10


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        foundNumbers = 0

        for n in nums:
            foundNumbers += int(log10(n)) % 2

        return foundNumbers

    def findNumbers2(self, nums: List[int]) -> int:
        foundNumbers = 0

        for n in nums:
            if n >= 10 and n < 100 or \
                    n >= 1000 and n < 10000 or \
                    n == 100000:
                foundNumbers += 1

        return foundNumbers
