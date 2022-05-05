from math import log2, floor

for t in range(int(input())):
    i = int(input())
    print((1 << floor(log2(i))) - 1)
