for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))

    s = sum(array)
    if s % n != 0:
        print(-1)
        continue

    avg = s / n

    friends_with_extra_candies = 0
    extra_candies = 0
    missing_candies = 0

    for i in range(n):
        if array[i] > avg:
            extra_candies += array[i] - avg
            friends_with_extra_candies += 1
        elif array[i] < avg:
            missing_candies += avg - array[i]

    if extra_candies == missing_candies:
        print(friends_with_extra_candies)
    else:
        print(-1)
