class Solution:
    SHIFT = ord('a')
    NUMBER_OF_LOWERCASE_ENGLISH_LETTERS = 26

    def equalFrequency(self, word: str) -> bool:
        frequencies = [0] * self.NUMBER_OF_LOWERCASE_ENGLISH_LETTERS
        for c in word:
            frequencies[ord(c) - self.SHIFT] += 1

        frequencies_counts = dict()

        for f in frequencies:
            if f == 0:
                continue

            frequencies_counts[f] = frequencies_counts.get(f, 0) + 1

            if len(frequencies_counts) > 2:
                return False

        freqs = frequencies_counts.keys()
        max_freq = max(freqs)
        max_freq_count = frequencies_counts[max_freq]
        min_freq = min(freqs)
        min_freq_count = frequencies_counts[min_freq]

        return min_freq == 1 and min_freq_count == 1 or \
            max_freq - min_freq == 1 and max_freq_count == 1 or \
            max_freq == min_freq and (1 == max_freq or 1 == max_freq_count)


if __name__ == '__main__':
    print(Solution().equalFrequency("abbba"))
