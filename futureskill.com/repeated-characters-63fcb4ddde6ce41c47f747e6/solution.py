class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_first_non_repeated_char(self, text):
        if text[0] != text[1]:
            return text[0]

        for i in range(1, len(text) - 1):
            if text[i] != text[i - 1] and text[i] != text[i + 1]:
                return text[i]

        if text[-1] != text[-2]:
            return text[-1]

        return ''

    def level_2_first_unique_char(self, text):
        chars_count = {}

        for c in text:
            if c not in chars_count:
                chars_count[c] = 1
            else:
                chars_count[c] += 1

        for character, count in chars_count.items():
            if count == 1:
                return character

        return ''
