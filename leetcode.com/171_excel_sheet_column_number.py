class Solution:
    SHIFT = 64
    POWERS_OF_26 = [1,
                    26,
                    26 * 26,
                    26 * 26 * 26,
                    26 * 26 * 26 * 26,
                    26 * 26 * 26 * 26 * 26,
                    26 * 26 * 26 * 26 * 26 * 26
                    ]

    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        return sum([
            self.POWERS_OF_26[l - i - 1] * \
            (ord(columnTitle[i]) - self.SHIFT)
            for i in range(l)
        ])


if __name__ == '__main__':
    print(Solution().titleToNumber('AA'))
