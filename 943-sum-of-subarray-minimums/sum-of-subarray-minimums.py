class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        result = 0
        dp = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                j = stack[-1]
                dp[i] = dp[j] + arr[i] * (i-j)
            else:
                dp[i] = arr[i] * (i+1)
            stack.append(i)
            result = (result+dp[i]) % mod
        return result