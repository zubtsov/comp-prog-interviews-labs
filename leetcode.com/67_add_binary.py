from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return f"{(int(a, 2) + int(b, 2)):b}"

        smaller_n, bigger_n = (a, b) if len(a) < len(b) else (b, a)

        shift = 0
        res = deque(maxlen=len(bigger_n) + 1)
        si = len(smaller_n) - 1
        bi = len(bigger_n) - 1

        while si >= 0:
            current_sum = 0
            if smaller_n[si] == '1':
                current_sum += 1
            if bigger_n[bi] == '1':
                current_sum += 1
            current_sum += shift

            res.appendleft(current_sum % 2)
            shift = current_sum // 2

            si -= 1
            bi -= 1

        while bi >= 0:
            current_sum = 0
            if bigger_n[bi] == '1':
                current_sum += 1
            current_sum += shift

            res.appendleft(current_sum % 2)
            shift = current_sum // 2
            bi -= 1

        if shift == 1:
            res.appendleft(1)

        return ''.join([str(x) for x in res])


if __name__ == '__main__':
    s = Solution()
    a = '11'
    b = '1'
    print(s.addBinary(a, b))
