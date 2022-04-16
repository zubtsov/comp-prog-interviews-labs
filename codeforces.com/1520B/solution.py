for i in range(int(input())):
    n_raw = input()
    n = int(n_raw)
    shorter_ordinary_numbers = (len(n_raw) - 1) * 9
    ordinary_numbers_of_same_length = int(n_raw[0]) if n_raw >= n_raw[0] * len(n_raw) else (int(n_raw[0]) - 1)

    print(shorter_ordinary_numbers + ordinary_numbers_of_same_length)
