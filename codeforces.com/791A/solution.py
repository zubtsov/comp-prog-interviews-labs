from math import log2, ceil

limak_weight, bob_weight = map(int, input().split())

if limak_weight == bob_weight:
    print(1)
else:
    print(ceil(log2(bob_weight / limak_weight) / (log2(3) - 1)))
