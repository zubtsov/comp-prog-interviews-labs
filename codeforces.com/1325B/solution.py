for i in range(int(input())):
    array_length = int(input())
    elements = map(int, input().split())
    # TODO: improve the performance
    print(len(set(elements)))
