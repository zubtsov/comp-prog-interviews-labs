s = input()

count = 1
max_char = s[0]

for i in range(1, len(s)):
    if ascii(s[i]) > ascii(max_char):
        max_char = s[i]
        count = 1
    elif s[i] == max_char:
        count += 1

print(max_char * count)
