class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        p, n = 0, 0
        while len(ans) < len(nums):
            while nums[p] < 0:
                p += 1
            while nums[n] > 0:
                n += 1
            ans.append(nums[p])
            ans.append(nums[n])
            p += 1
            n += 1
        return ans