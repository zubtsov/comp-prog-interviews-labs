word = input()
translated_word = input()

word_len = len(word)
translated_word_len = len(translated_word)

translation_is_correct = True

for i in range(word_len):
    if word[i] != translated_word[translated_word_len - i - 1]:
        translation_is_correct = False

if translation_is_correct:
    print('YES')
else:
    print('NO')
