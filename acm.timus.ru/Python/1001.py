from sys import stdin, stdout
from math import sqrt

for x in reversed(stdin.read().split()):
    stdout.write('\n%.4f' % sqrt(float(x)))
