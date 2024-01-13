class Solution:
    def minSteps(self, s: str, t: str) -> int:
        result = 0
        s_dict = dict()
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        for c in t:
            if c in s_dict and s_dict[c] > 0:
                s_dict[c] -= 1
            else:
                result += 1
        return result