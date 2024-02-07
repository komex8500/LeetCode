class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        d = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(sorted_d)):
            ans += sorted_d[i][0] * sorted_d[i][1]
        return ans