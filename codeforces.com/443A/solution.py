letters = input()

letters_without_curly_brackets = letters[1:-1]

if len(letters_without_curly_brackets) == 0:
    print(0)
else:
    print(len(set(letters_without_curly_brackets.split(', '))))
