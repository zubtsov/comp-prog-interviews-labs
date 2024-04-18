class Solution:
    CLOSED_TO_OPEN = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    def isValid(self, s: str) -> bool:
        opening_brackets_stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                opening_brackets_stack.append(c)
            else:
                if not opening_brackets_stack:
                    return False
                last_bracket = opening_brackets_stack.pop()
                if last_bracket != self.CLOSED_TO_OPEN[c]:
                    return False

        if not opening_brackets_stack:
            return True


if __name__ == '__main__':
    s = Solution()
    b = "()"
    print(s.isValid(b))
