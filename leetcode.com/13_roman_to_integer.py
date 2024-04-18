class Solution:
    ROMAN_TO_DECIMAL = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000}

    def romanToInt(self, s: str) -> int:
        result = 0
        l = len(s)

        i = 0
        while i < l - 1:
            next_digit = s[i + 1]
            current_digit = s[i]

            if (current_digit == "I" and (next_digit == "V" or next_digit == "X")) or \
                    (current_digit == "X" and (next_digit == "L" or next_digit == "C")) or \
                    (current_digit == "C" and (next_digit == "D" or next_digit == "M")):
                result -= self.ROMAN_TO_DECIMAL[current_digit]
            else:
                result += self.ROMAN_TO_DECIMAL[current_digit]
            i += 1
        result += self.ROMAN_TO_DECIMAL[s[++i]]

        return result
