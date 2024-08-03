# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = [None] * 128
        t_to_s = [None] * 128

        for sc, tc in zip(s, t):
            sc_ord = ord(sc)
            if s_to_t[sc_ord] is not None:
                if s_to_t[sc_ord] != tc:
                    return False
            else:
                s_to_t[sc_ord] = tc

            tc_ord = ord(tc)
            if t_to_s[tc_ord] is not None:
                if t_to_s[tc_ord] != sc:
                    return False
            else:
                t_to_s[tc_ord] = sc

        return True


if __name__ == '__main__':
    assert (Solution().isIsomorphic('foo', 'bar') is False)
    assert (Solution().isIsomorphic('bar', 'foo') is False)
