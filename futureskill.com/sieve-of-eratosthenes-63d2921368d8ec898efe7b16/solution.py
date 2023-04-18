class Solution:
    def __init__(self, api):
        self.api = api

    def find_next_prime(self, sieve):
        for nextNumber in sieve:
            if nextNumber != 0:
                return nextNumber
        else:
            return -1

    def cross_off_prime(self, sieve, prime):
        for i in range(prime - 1, len(sieve), prime):
            sieve[i] = 0
        return sieve
