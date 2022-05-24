from math import floor, sqrt


def sieve_of_eratosthenes(n):
    prime_numbers = [True] * n
    for i in range(2, floor(sqrt(n)) + 1):
        if prime_numbers[i]:
            for j in range(i * i, n, i):
                prime_numbers[j] = False
    return prime_numbers


primes_flags = sieve_of_eratosthenes(50000)

for t in range(int(input())):
    d = int(input())

    prime_divisors = [1]
    i = 1 + d
    while i < len(primes_flags):
        if primes_flags[i]:
            prime_divisors.append(i)
            i += (d - 1)
            if len(prime_divisors) >= 3:
                print(prime_divisors[1] * prime_divisors[2])
                break
        i += 1
