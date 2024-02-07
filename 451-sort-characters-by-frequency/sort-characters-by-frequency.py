class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        d = dict(Counter(s))
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for count in sorted_d:
            ans += count[0] * count[1]
        return ans