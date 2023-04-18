class Solution:
    special_chars_regex = r'[\,|\.|\!|\?]'

    def __init__(self, api):
        self.api = api

    def level_1_word_count(self, sentence):
        return len(sentence.split(' '))

    def level_2_word_sorting(self, sentence):
        import re
        result = re.sub(Solution.special_chars_regex, '', sentence.lower()).split(' ')
        result.sort()
        return result

    def level_3_sort_by_occurrences(self, sentence):
        import re
        words = re.sub(Solution.special_chars_regex, '', sentence.lower()).split(' ')
        words_count = {}
        for word in words:
            if word not in words_count:
                words_count[word] = 1
            else:
                words_count[word] += 1
        sorted_words_count = sorted(words_count.items(), key=lambda t: (-t[1], t[0]))
        return list(map(lambda t: t[0], sorted_words_count))
