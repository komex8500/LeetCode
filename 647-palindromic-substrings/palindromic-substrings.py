class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        ans += 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        ans += 1
        return ans
