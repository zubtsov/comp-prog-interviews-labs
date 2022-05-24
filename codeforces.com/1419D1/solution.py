number_of_ice_spheres = int(input())
ice_spheres_prices = list(map(int, input().split()))

ice_spheres_prices.sort()

result = []
for i in range(number_of_ice_spheres // 2):
    result.append(ice_spheres_prices[-i - 1])
    result.append(ice_spheres_prices[i])

if number_of_ice_spheres % 2 == 1:
    result.append(ice_spheres_prices[number_of_ice_spheres // 2])
    print(number_of_ice_spheres // 2)
else:
    print((number_of_ice_spheres - 1) // 2)

print(' '.join(map(str, result)))
