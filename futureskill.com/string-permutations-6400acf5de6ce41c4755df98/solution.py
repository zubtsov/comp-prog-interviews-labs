class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_common_letters(self, list_of_strings):
        letters_count = {}
        for s in list_of_strings:
            letters_count_local = {}
            for c in s:
                if c in letters_count_local:
                    letters_count_local[c] += 1
                else:
                    letters_count_local[c] = 1
            for letter, count in letters_count_local.items():
                if letter not in letters_count or letters_count[letter] < count:
                    letters_count[letter] = count

        return ''.join(map(lambda t: t[0] * t[1], sorted(letters_count.items())))
