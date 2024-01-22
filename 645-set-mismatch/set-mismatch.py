class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expect = int((1+n)*(n/2))
        sum_set = sum(set(nums))
        return [sum(nums) - sum_set, expect - sum_set]
