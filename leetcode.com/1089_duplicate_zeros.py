from collections import deque
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        buffer = deque()

        lastNumberWasZero = False
        for i in range(len(arr)):
            if lastNumberWasZero:
                buffer.append(arr[i])
                arr[i] = 0
                lastNumberWasZero = False
            else:
                if buffer:
                    buffer.append(arr[i])
                    arr[i] = buffer.popleft()
                if arr[i] == 0:
                    lastNumberWasZero = True


if __name__ == '__main__':
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(arr)
    print(arr)
