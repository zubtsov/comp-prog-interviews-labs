from typing import List


class Solution:
    def calculate_current_cell_perimeter(self, grid: List[List[int]], x: int, y: int) -> int:
        perimeter = 0

        if x == 0 or grid[x - 1][y] == 0:
            perimeter += 1
        if x == len(grid) - 1 or grid[x + 1][y] == 0:
            perimeter += 1

        if y == 0 or grid[x][y - 1] == 0:
            perimeter += 1
        if y == len(grid[x]) - 1 or grid[x][y + 1] == 0:
            perimeter += 1

        return perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_perimeter = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    total_perimeter += self.calculate_current_cell_perimeter(grid, x, y)

        return total_perimeter


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(s.islandPerimeter(grid))
    grid = [[1]]
    print(s.islandPerimeter(grid))
    grid = [[1,0]]
    print(s.islandPerimeter(grid))
