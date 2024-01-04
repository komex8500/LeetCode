from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        ans = 0
        for count in mp.values():
            if count == 1:
                return -1
            ans += count // 3
            if count % 3:
                ans += 1
        return ans