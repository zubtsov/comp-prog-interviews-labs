class Solution:
    def __init__(self, api):
        self.api = api

    @staticmethod
    def level_2_mapper(n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)

    def level_1_fizz(self, int_list):
        return list(map(lambda n: str(n) if n % 3 != 0 else "Fizz", int_list))

    def level_2_fizzbuzz(self, int_list):
        return list(map(Solution.level_2_mapper, int_list))
