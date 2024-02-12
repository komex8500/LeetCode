class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            if d[n] > len(nums) / 2:
                return n
        return null