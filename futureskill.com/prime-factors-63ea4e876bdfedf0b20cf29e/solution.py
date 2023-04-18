class Solution:
    def __init__(self, api):
        self.api = api
        self.prime_numbers = Solution.find_prime_numbers(10000)

    @staticmethod
    def find_prime_numbers(upper_limit):
        primes = [True] * upper_limit
        for i in range(2, upper_limit):
            for j in range(i ** 2, upper_limit, i):
                primes[j] = False
        return set([pn for pn in range(len(primes)) if primes[pn] and pn >= 2])

    def factorize_number(self, n):
        factorized_number = {}

        if n == 1:
            return {1: 1}
        elif n in self.prime_numbers:
            factorized_number = {n: 1}
        else:
            while n != 1:
                for pn in self.prime_numbers:
                    if n % pn == 0:
                        n /= pn
                        if pn in factorized_number:
                            factorized_number[pn] += 1
                        else:
                            factorized_number[pn] = 1
                        break
        return factorized_number

    def get_prime_factors(self, num):
        factorized_number = self.factorize_number(num)
        result = []
        for pn in sorted(factorized_number.keys()):
            result += [pn] * factorized_number[pn]
        return result
