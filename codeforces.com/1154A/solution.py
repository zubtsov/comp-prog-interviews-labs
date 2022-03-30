numbers = list(map(int, input().split()))

numbers.sort()


def solve_linear_equations_system(x, y, z):
    return -0.5 * x + 0.5 * y + 0.5 * z, 0.5 * x - 0.5 * y + 0.5 * z, 0.5 * x + 0.5 * y - 0.5 * z


print(' '.join(list(map(lambda x: str(int(x)), solve_linear_equations_system(*numbers[:-1])))))
