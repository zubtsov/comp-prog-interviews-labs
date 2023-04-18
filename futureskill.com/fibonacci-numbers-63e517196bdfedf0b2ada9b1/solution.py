class Solution:
    def __init__(self, api):
        self.api = api
        self.cached_fibonacci_numbers = [0, 1, 1]

    def get_fibonacci_number(self, nth):
        for i in range(len(self.cached_fibonacci_numbers), nth):
            self.cached_fibonacci_numbers.append(
                self.cached_fibonacci_numbers[i - 2] +
                self.cached_fibonacci_numbers[i - 1]
            )

        return self.cached_fibonacci_numbers[nth - 1]
