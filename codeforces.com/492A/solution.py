available_number_of_cubes = int(input())

required_number_of_cubes = 0
# TODO: is it possible to get the answer using analytical solution (formula/inequation), not loop?
for k in range(1, 10000):
    s = (1 + k) * k // 2
    if required_number_of_cubes + s > available_number_of_cubes:
        print(k - 1)
        break
    else:
        required_number_of_cubes += s
