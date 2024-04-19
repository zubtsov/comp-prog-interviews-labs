class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        start = 2;
        end = x / 2 + 1;
        new_point = 2 + (x / 2 - 2)

        while int(end) != int(start):
            d = end - start
            new_point = start + d / 2
            estimation = new_point * new_point
            if estimation > x:
                end -= d / 2
            elif estimation < x:
                start += d / 2
            else:
                return int(new_point)
        return int(new_point)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(25))
