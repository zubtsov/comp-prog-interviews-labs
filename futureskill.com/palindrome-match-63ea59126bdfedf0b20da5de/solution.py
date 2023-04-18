class Solution:
    def __init__(self, api):
        self.api = api
        self.palindromes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def level_1_is_palindrome(self, num):
        num_str = str(num)
        left_half = num_str[:len(num_str) // 2]
        right_half_reversed = num_str[len(num_str):len(num_str) // 2 + (len(num_str) % 2 - 1):-1]
        return left_half == right_half_reversed

    def level_2_list_of_palindromes(self, from_n, to_n):
        next_potential_palindrome = self.palindromes[-1] + 1
        while len(self.palindromes) < to_n:
            if self.level_1_is_palindrome(next_potential_palindrome):
                self.palindromes.append(next_potential_palindrome)
            next_potential_palindrome += 1
        return self.palindromes[from_n - 1:to_n]
