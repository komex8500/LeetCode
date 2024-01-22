class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        for n in range(1, len(nums) + 1):
            count = nums.count(n)
            if count == 0:
                ans[1] = n
            elif count == 2:
                ans[0] = n
        return ans