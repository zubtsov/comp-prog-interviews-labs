class Solution:
    def __init__(self, api):
        self.api = api

    def generate_pascal_triangle_binomial(self, n):
        from math import factorial

        if n < 1 or n > 12:
            return []

        binomial_coefficients = []
        for i in range(n):
            current_row = []
            for k in range(i + 1):
                current_row.append(str(int(factorial(i) / (factorial(k) * factorial(i - k)))))
            binomial_coefficients.append(' '.join(current_row))
        return binomial_coefficients

    def generate_pascal_triangle_summation(self, n):
        if n < 1 or n > 12:
            return []

        triangle = [[1]]
        for i in range(1, n):
            triangle.append([])
            for k in range(i + 1):
                right_upper = 0 if k >= i else triangle[i - 1][k]
                left_upper = 0 if k <= 0 else triangle[i - 1][k - 1]
                triangle[i].append(right_upper + left_upper)

        return list(map(lambda l: ' '.join(map(str, l)), triangle))
