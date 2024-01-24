class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0

        dp = [[False] * n for _ in range(n)]
        for k in range(n):
            dp[k][k] = True
            for j in range(k):
                if (k-j < 2 or dp[j+1][k-1]) and s[j] == s[k]:
                    dp[j][k] = True
                    if k-j+1 > max_len:
                        max_len = k-j+1
                        begin = j
        return s[begin:begin+max_len] 