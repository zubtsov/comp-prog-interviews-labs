class Solution:
    def __init__(self, api):
        self.api = api
        self.prime_numbers = Solution.find_prime_numbers(50000)

    @staticmethod
    def find_prime_numbers(upper_limit):
        primes = [True] * upper_limit
        for i in range(2, upper_limit):
            for j in range(i ** 2, upper_limit, i):
                primes[j] = False
        return set([pn for pn in range(len(primes)) if primes[pn] and pn >= 2])

    @staticmethod
    def factorize_number(n, prime_numbers):
        factorized_number = {}

        if n == 1:
            return {1: 1}
        elif n in prime_numbers:
            factorized_number = {n: 1}
        else:
            while n != 1:
                for pn in prime_numbers:
                    if n % pn == 0:
                        n /= pn
                        if pn in factorized_number:
                            factorized_number[pn] += 1
                        else:
                            factorized_number[pn] = 1
                        break
        return factorized_number

    def level_1_smallest_multiple(self, int_list):
        factorized_numbers = [Solution.factorize_number(i, self.prime_numbers) for i in int_list]

        def merge_factors_choose_max(fn1, fn2):
            merged_fn = {}
            for pn in fn1.keys() | fn2.keys():
                merged_fn[pn] = max(fn1.get(pn, 0), fn2.get(pn, 0))
            return merged_fn

        from functools import reduce
        def mult(x, y): return x * y
        def pwr(t): return t[0] ** t[1]
        factorized_smallest_multiple = reduce(merge_factors_choose_max, factorized_numbers)
        factors = map(pwr, factorized_smallest_multiple.items())
        smallest_multiple = reduce(mult, factors)

        return smallest_multiple

    def level_2_smallest_multiple(self, int_list):
        return float(self.level_1_smallest_multiple(int_list))
