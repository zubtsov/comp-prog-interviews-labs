class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_end_index = len(s) - 1
        while s[word_end_index] == ' ':
            word_end_index -= 1
        word_start_index = word_end_index
        while word_start_index >= 0 and s[word_start_index] != ' ':
            word_start_index -= 1
        return word_end_index - word_start_index