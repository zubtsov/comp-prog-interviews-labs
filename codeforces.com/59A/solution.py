mixed_case_word = input()

case_score = sum(map(lambda c: 1 if c.isupper() else -1, mixed_case_word))

if case_score > 0:
    print(mixed_case_word.upper())
else:
    print(mixed_case_word.lower())
