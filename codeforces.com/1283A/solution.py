for i in range(int(input())):
    hours, minutes = map(int, input().split())
    print(24*60 - (hours*60+minutes))
