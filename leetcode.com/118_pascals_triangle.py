from typing import List


class Solution:
    def __init__(self):
        self.triangle = [[1], [1, 1]]

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= len(self.triangle):
            return self.triangle[:numRows]

        for current_row_index in range(len(self.triangle), numRows):
            current_row = [1]
            num_elems = current_row_index + 1
            for j in range(1, num_elems - 1):
                current_row.append(self.triangle[current_row_index - 1][j - 1] +
                                   self.triangle[current_row_index - 1][j])
            current_row.append(1)
            self.triangle.append(current_row)
        return self.triangle


if __name__ == '__main__':
    print(Solution().generate(10))
