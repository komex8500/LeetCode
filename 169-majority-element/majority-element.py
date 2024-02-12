class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        d = dict()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            ans = n if d[n] > d[ans] else ans
        return ans