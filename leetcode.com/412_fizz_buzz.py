from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        for i in range(n):
            shifted = (i + 1)
            if not shifted % 15:
                yield "FizzBuzz"
            elif not shifted % 5:
                yield "Buzz"
            elif not shifted % 3:
                yield "Fizz"
            else:
                yield str(shifted)
