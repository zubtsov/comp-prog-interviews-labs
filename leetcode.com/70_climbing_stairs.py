class Solution:
    solutions = [None] * 46

    def __init__(self):
        for i in range(46):
            if i <= 3:
                self.solutions[i] = i
            else:
                self.solutions[i] = self.solutions[i - 1] + self.solutions[i - 2]

    def climbStairs(self, n: int) -> int:
        return self.solutions[n]
