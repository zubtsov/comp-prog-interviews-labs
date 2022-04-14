n = int(input())

k = n // 2
print(k)

if n % 2 == 0:
    print(('2 ' * k).rstrip())
else:
    print('2 ' * (k-1) + '3')
