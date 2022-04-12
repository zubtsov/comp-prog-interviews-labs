number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_athletes = int(input())
    athletes_strengths = list(map(int, input().split()))
    athletes_strengths.sort()
    result = min([abs(s1 - s2) for s1, s2 in zip(athletes_strengths[1:], athletes_strengths[:-1])])
    print(result)
