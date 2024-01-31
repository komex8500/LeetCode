class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        s = [0]
        for i in range(1, len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                index = s.pop()
                ans[index] = i - index
            s.append(i)
        return ans